
# Image Comparison Script

This Python script compares images and files in two directories. It identifies and prints the names of files present in one directory but not in the other, checks the sizes of compressed files, and compares images based on their pixel values.


## Requirements and usage

- Python 3.6 or higher
- __OpenCV:__: This library is used for image processing tasks. In this script, it's used to read images and compute the absolute difference between them
- __numpy__:  This library is used for numerical operations. In this script, it’s used to sum the differences between the images.
- __pathlib__:  This library is used for handling paths. In this script, it’s used to iterate over the files in the directories and check their types.

These libraries can be installed using pip:
```bash
pip install opencv-python numpy pathlib
```
To use the script, ensure that you have two directories named ```imported``` and ```exported``` under a parent directory named ```test_files```. Place the files you want to compare in these directories. Then, run the script in your Python environment. The script will automatically read the files from the directories, sort them, check the sizes of the compressed files, and compare the images.

__Run the Script:__ Run the script in your Python environment. The script will automatically read the files from the imported and exported directories.
## Aproach
1.  __identifying unique files:__ function ```print_unique_files ``` identifies and prints the names of files present in one directory but not in the other.
2. __Sorting Files by Type:__ function ```sort_files ``` Sorting the files by their types at the beginning allows the script to handle different file types differently . This is important because the method of comparison for images will be different from that of compressed files.
3. __Checking Compressed Files by Size:__ The script will check the sizes of the compressed files in both directories. If there’s a size difference, it will print an error message with the file name and the size difference in bytes.
4. __Image Comparison Using OpenCV:__ function```compare_images ```  Using OpenCV, it can compare images objectively based on their pixel values.
OpenCV’s robust functionality, efficiency, and strong community support make it an ideal choice for this image and file comparison script.
For more information about OpenCV, visit: https://opencv.org/


   


