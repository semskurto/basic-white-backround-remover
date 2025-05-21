# Transparent Background Script

## Overview
This script processes a directory of images to remove near-white backgrounds (RGB values >= 240) by making them transparent. The output images are saved in PNG format to preserve transparency. It utilizes Python and libraries such as Pillow for image manipulation and tqdm for progress indication.

## Features
- Batch processing of images from a specified input folder.
- Converts near-white backgrounds (RGB values >= 240) to transparent.
- Outputs images in PNG format, ideal for transparency.
- Leverages multiprocessing for potentially faster processing on multi-core systems.
- Includes logging for monitoring and troubleshooting.

## Prerequisites
- Python 3 (tested with Python 3.x versions)
- Pip (Python package installer)

## Installation
1.  Clone the repository (replace `<repository_url>` with the actual URL of this repository, e.g., `https://github.com/your-username/your-repository-name.git`):
    ```sh
    git clone <repository_url>
    ```
2.  Navigate to the project directory (replace `<repository_folder_name>` with the name of the cloned folder, typically the repository name):
    ```sh
    cd <repository_folder_name>
    ```
3.  Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
To run the `start.py` script, use the following command structure:
```sh
python start.py --pathIn <input_folder_path> --pathOut <output_folder_path>
```

### Argument Explanation
-   `--pathIn` (or `-pin`): **Required**. Specifies the path to the folder containing the input images.
    Example: `python start.py --pathIn ./input_images --pathOut ./output_images`
-   `--pathOut` (or `-pout`): **Required**. Specifies the path to the folder where the processed, transparent-background images will be saved. The script will attempt to create this folder if it does not already exist.
    Example: `python start.py --pathIn ./input_images --pathOut ./processed_images`

## How it Works
1.  The script scans the specified input folder for image files (common extensions like .png, .jpg, .jpeg, etc.).
2.  It uses multiprocessing to distribute the workload across available CPU cores for efficiency.
3.  For each image:
    *   It is opened and converted to RGBA format (Red, Green, Blue, Alpha) to handle transparency.
    *   Every pixel is examined. If a pixel's RGB values are all 240 or higher (indicating a near-white color), its alpha channel is set to 0 (fully transparent). Otherwise, the original pixel data is retained.
    *   The modified image data, now with a potentially transparent background, is saved as a new PNG file in the specified output folder. PNG format is chosen for its excellent support of transparency.
4.  Progress is displayed using a progress bar, and events are logged to the console.

## Dependencies
This project uses the following Python libraries, which are listed in `requirements.txt` and installed during the setup:
-   **Pillow**: A powerful image processing library, used for opening, manipulating, and saving images.
-   **tqdm**: A fast, extensible progress bar library that provides visual feedback during processing.

## Contributing
We welcome contributions! If you'd like to improve the script or add new features, please follow these steps:
1.  Fork the repository.
2.  Create a new branch for your feature:
    ```sh
    git checkout -b your-feature-branch
    ```
3.  Make your changes and commit them:
    ```sh
    git commit -am 'Add some amazing feature'
    ```
4.  Push your changes to the branch:
    ```sh
    git push origin your-feature-branch
    ```
5.  Open a new Pull Request against the main branch of this repository.
