
# Image Comparison Script

This Python script compares images in two directories and prints the names of images that are not similar.



## Requirements

- Python 3.6 or higher
- OpenCV
- numpy
- pathlib

```bash
pip install opencv-python numpy pathlib
```



## Usage

1. __Run the Script:__ Run the script in your Python environment. The script will automatically read the files from the imported and exported directories.

2. __Check the Output:__ The script will print the names of the files in the imported directory.

3__file size:__The script will check the sizes of the compressed files in both directories. If there’s a size difference, it will print an error message with the file name and the size difference in bytes.

4.__Image Comparison:__ The script will compare the images in both directories. If the total difference between two images exceeds a certain threshold, it will print a message indicating that the images are not similar.


## Technology

 __open CV__ (Open Source Computer Vision Library) is an excellent choice for this script due to several reasons:

1. __Image Processing Capabilities:__ OpenCV is a powerful library specifically designed for computer vision and image processing. It provides a wide range of functions that can handle tasks from basic image manipulation to complex object detection.

2. __Performance:__ OpenCV is written in C/C++, which means it’s incredibly fast. It’s designed to be efficient with memory and processing power, which is crucial when dealing with large images or real-time applications.

3. __Cross-Platform and Language Support:__ OpenCV can be used with many programming languages including Python, and it’s cross-platform, meaning it can run on various operating systems like Windows, Linux, and MacOS.

4. __Community and Documentation:__ OpenCV has a large and active community. This means that if you encounter issues or need to learn how to do something, there’s a good chance that someone else has already solved that problem. The documentation is also comprehensive and well-maintained.

5. __Functionality:__ In this script, OpenCV is used to read images, check their dimensions, and compute the absolute difference between them. These are all tasks that OpenCV excels at.

In summary, OpenCV’s robust functionality, efficiency, and strong community support make it an ideal choice for this image and file comparison script. 😊
https://opencv.org/