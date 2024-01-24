import cv2
import numpy as np
from pathlib import Path

# end of imports
imgTypes = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
compressedTypes = ['.zip', '.tar', '.gz', '.rar']
# end of file types

importedPath = Path('test_files/imported')
importedFilePaths = [file for file in importedPath.iterdir() if file.is_file()]
exportedPath = Path('test_files/exported')
exportedFilePaths = [file for file in exportedPath.iterdir() if file.is_file()]
# end of file directories
for f in importedFilePaths:
    file_names = f.name
    print(file_names)

def sort_files(input_files, img_types, compressed_types):
    image_files = []
    compressed_files = []
    for filePath in input_files:
        # check the file extension
        if filePath.suffix in img_types:
            image_files.append(filePath)
        elif filePath.suffix in compressed_types:
            compressed_files.append(filePath)
    return image_files, compressed_files
# end of sort_files function

importedImageFiles, importedCompressedFiles = sort_files(importedFilePaths, imgTypes, compressedTypes)
exportedImageFiles, exportedCompressedFiles = sort_files(exportedFilePaths, imgTypes, compressedTypes)
# end of file sorting by types

imported_compressed_dict = {file.name: file.stat().st_size for file in importedCompressedFiles}
exported_compressed_dict = {file.name: file.stat().st_size for file in exportedCompressedFiles}
for file_name, imported_size in imported_compressed_dict.items():
    exported_size = exported_compressed_dict.get(file_name)
    if exported_size is not None:
        if imported_size == exported_size:
            print(f'{file_name}: Good')
        else:
            difference = abs(imported_size - exported_size)
            print(f'{file_name}: Error, size difference is {difference} bytes')
# end of checking compressed files

def compare_images(img1_path, img2_path):
    # Load the images
    img1 = cv2.imread(str(img1_path))
    img2 = cv2.imread(str(img2_path))

    # Check if the dimensions match
    if img1.shape != img2.shape:
        print(f'Images {img1_path.name} and {img2_path.name} have different dimensions.')
        return

    # Compute the absolute difference
    difference = cv2.absdiff(img1, img2)

    # Sum the differences
    total_difference = np.sum(difference)

    print(f'Total difference for {img1_path.name}: {total_difference}')

# start of image comparison
for importedImage in importedImageFiles:
    for exportedImage in exportedImageFiles:
        if importedImage.name == exportedImage.name:
            compare_images(importedImage, exportedImage)
# end of image comparison
