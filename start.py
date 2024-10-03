import os
import sys
import argparse
from tqdm import tqdm
from PIL import Image
import multiprocessing as mp


def convertImage(pathIn, pathOut):
    img_list = os.listdir(pathIn)
    for idx in tqdm(range(len(img_list))):
        img_path = img_list[idx]
        pool = mp.Pool(mp.cpu_count())
        pool.apply_async(process_image, (img_path, pathIn, pathOut, ))
        
        pool.close()
        pool.join()

    print("[Successful] PLEASE CHECK OUTPUT FOLDER:")

def process_image(img_path, pathIn, pathOut):
    img_id = os.path.splitext(img_path)[0]
    img = Image.open(os.path.join(pathIn, img_path))

    img = img.convert("RGBA")

    datas = img.getdata()

    newData = []

    for item in datas:
        if item[0] >= 240 and item[1] >= 240 and item[2] >= 240:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save(os.path.join(pathOut, f"{img_id}.png"), "PNG")

if __name__=="__main__":
    a = argparse.ArgumentParser()
    a.add_argument("-pin","--pathIn", help= "path to read folder")
    a.add_argument("-pout", "--pathOut", help= "path to write folder")
    args = a.parse_args()
    convertImage(args.pathIn, args.pathOut)
    print(args.pathOut)



####### EXAMPLE USAGE #####
# python3 start.py -pin /home/XYZ/ABC/input_images_folder -pout /home/XYZ/ABC/output_images_folder
