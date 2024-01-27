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

# create set of files
imported_file_names = {file.name for file in importedFilePaths}
exported_file_names = {file.name for file in exportedFilePaths}


def print_unique_files(dir1, dir2):
    dir1_file_names = {file.name for file in dir1}
    dir2_file_names = {file.name for file in dir2}

    unique_in_dir1 = dir1_file_names - dir2_file_names
    unique_in_dir2 = dir2_file_names - dir1_file_names

    if unique_in_dir1:
        print("Files present in the import directory but not in the export:")
        for fileName in unique_in_dir1:
            print(fileName)

    if unique_in_dir2:
        print("Files present in the export directory but not in the import:")
        for fileName in unique_in_dir2:
            print(fileName)
# End of print_unique_files function


def compare_images(img1_path, img2_path):
    # Load the images
    img1 = cv2.imread(str(img1_path))
    img2 = cv2.imread(str(img2_path))

    # Check if the dimensions match
    if img1.shape != img2.shape:
        print(f'Images {img1_path.name} and {img2_path.name} have different dimensions.')
        return

    # Sum the differences
    diff = cv2.absdiff(img1, img2)
    total_difference = np.sum(diff)

    # Define a threshold for the total difference
    threshold = 10

    if total_difference > threshold:
        print(f'Images {img1_path.name} and {img2_path.name} are not similar. Total difference: {total_difference}')
# end of compare_images function


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

# ------------------------------------ End of function defining --------------------------------------------------------


# print files that have nomatch
print_unique_files(importedFilePaths, exportedFilePaths)

# Filter the file lists to only include files with names in the intersection
common_file_names = imported_file_names & exported_file_names
importedFilePaths = [file for file in importedFilePaths if file.name in common_file_names]
exportedFilePaths = [file for file in exportedFilePaths if file.name in common_file_names]


importedImageFiles, importedCompressedFiles = sort_files(importedFilePaths, imgTypes, compressedTypes)
exportedImageFiles, exportedCompressedFiles = sort_files(exportedFilePaths, imgTypes, compressedTypes)
# end of file sorting by types

imported_compressed_dict = {file.name: file.stat().st_size for file in importedCompressedFiles}
exported_compressed_dict = {file.name: file.stat().st_size for file in exportedCompressedFiles}
for file_name, imported_size in imported_compressed_dict.items():
    exported_size = exported_compressed_dict.get(file_name)
    if exported_size is not None:
        if imported_size != exported_size:
            difference = abs(imported_size - exported_size)
            print(f'{file_name}: Error, size difference is {difference} bytes')
# end of checking compressed files


for importedImage in importedImageFiles:
    for exportedImage in exportedImageFiles:
        if importedImage.name == exportedImage.name:
            compare_images(importedImage, exportedImage)
# end of image comparison
