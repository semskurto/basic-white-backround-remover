import os
import sys
import argparse
import logging # Added import
from tqdm import tqdm
from PIL import Image
import multiprocessing as mp


def convertImage(pathIn, pathOut):
    # Path Validation for pathIn
    if not os.path.isdir(pathIn):
        logging.error(f"Input path '{pathIn}' is not a valid directory.")
        return

    # Path Validation for pathOut and directory creation
    if not os.path.isdir(pathOut):
        try:
            os.makedirs(pathOut, exist_ok=True)
            logging.info(f"Output directory '{pathOut}' created.")
        except OSError as e:
            logging.error(f"Could not create output directory '{pathOut}': {e}")
            return

    img_list = os.listdir(pathIn)
    
    # Define allowed image extensions
    allowed_extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.gif']

    # Optimize Multiprocessing: Create pool before the loop
    pool = mp.Pool(mp.cpu_count())
    
    results = []

    for img_name in tqdm(img_list):
        # Filter Image Files
        if not img_name.lower().endswith(tuple(allowed_extensions)):
            logging.warning(f"Skipping non-image file: {img_name}")
            continue
        
        # Use apply_async
        result = pool.apply_async(process_image, args=(img_name, pathIn, pathOut))
        results.append(result)
        
    # Move pool.close() and pool.join() after the loop
    pool.close()
    pool.join()

    # Check results for any errors if needed (optional, basic check here)
    for result in results:
        try:
            result.get() # To raise exceptions if any occurred in the worker process
        except Exception as e:
            # This will catch errors from process_image if they weren't caught inside
            # and re-raised, or other multiprocessing errors.
            # Error is already printed in process_image, but you could log it here too.
            pass


    logging.info(f"Successfully processed images. Please check output folder: {pathOut}")

def process_image(img_name, pathIn, pathOut):
    try:
        img_id = os.path.splitext(img_name)[0]
        img_path = os.path.join(pathIn, img_name)
        img = Image.open(img_path)

        img = img.convert("RGBA")

        datas = img.getdata()
        newData = []

        for item in datas:
            if item[0] >= 240 and item[1] >= 240 and item[2] >= 240: # Assuming white background
                newData.append((255, 255, 255, 0)) # Make white transparent
            else:
                newData.append(item)

        img.putdata(newData)
        output_image_path = os.path.join(pathOut, f"{img_id}.png")
        img.save(output_image_path, "PNG")
    except (IOError, SyntaxError) as e:
        logging.error(f"Error processing {img_name}: {e}")
    except Exception as e:
        # Catch any other unexpected errors
        logging.error(f"An unexpected error occurred while processing {img_name}: {e}")


if __name__=="__main__":
    # Configure basic logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    a = argparse.ArgumentParser()
    a.add_argument("-pin","--pathIn", required=True, help= "path to read folder")
    a.add_argument("-pout", "--pathOut", required=True, help= "path to write folder")
    args = a.parse_args()

    # The explicit check for args.pathIn and args.pathOut has been removed
    # as argparse with required=True handles this.
        
    convertImage(args.pathIn, args.pathOut)
    # The final logging.info statement about the output directory has been removed
    # as convertImage already provides a success message.


####### EXAMPLE USAGE #####
# python3 start.py --pathIn /path/to/input_images_folder --pathOut /path/to/output_images_folder
