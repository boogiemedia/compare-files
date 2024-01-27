
# Image Comparison Script

This Python script compares images in two directories and prints the names of images that are not similar.


## Requirements and usage

- Python 3.6 or higher
- __OpenCV:__: This is the OpenCV library, used for image processing tasks. In this script, it’s used to read
- __numpy__:  This library is used for numerical operations. In this script, it’s used to sum the differences between the images.
- __pathlib__:  This library is used for handling paths. In this script, it’s used to iterate over the files in the directories and check their types.

These libraries can be installed using pip:
```bash
pip install opencv-python numpy pathlib
```
To use the script, ensure that you have two directories named ```imported``` and ```exported``` under a parent directory named ```test_files```. Place the files you want to compare in these directories. Then, run the script in your Python environment. The script will automatically read the files from the directories, sort them, check the sizes of the compressed files, and compare the images.

__Run the Script:__ Run the script in your Python environment. The script will automatically read the files from the imported and exported directories.
## Aproach
1. __Sorting Files by Type:__ Sorting the files by their types at the beginning allows the script to handle different file types differently. This is important because the method of comparison for images will be different from that of compressed files.

2. __Checking Compressed Files by Size:__ The script will check the sizes of the compressed files in both directories. If there’s a size difference, it will print an error message with the file name and the size difference in bytes.

3. __Image Comparison Using OpenCV:__ Images can be compared visually, but this process can be subjective and inconsistent. Using OpenCV, the script can compare images objectively based on their pixel values.
OpenCV’s robust functionality, efficiency, and strong community support make it an ideal choice for this image and file comparison script.
https://opencv.org/


   


