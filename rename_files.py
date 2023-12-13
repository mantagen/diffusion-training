import os

import argparse

# Create the parser
parser = argparse.ArgumentParser(description='Process folder path.')

# Add the argument for the folder path
parser.add_argument('folder_path', type=str, help='Path to the folder')

# Parse the arguments
args = parser.parse_args()

# Use the folder path from the arguments
folder_path = args.folder_path

# Change to the folder containing the images
os.chdir(folder_path)

# Get a list of all files in the folder
files = os.listdir()

# Filter only image files (you might want to adjust this based on your file types)
image_files = [file for file in files if file.lower().endswith(('.jpg', '.jpeg', '.png', '.heic'))]

# Sort the image files
image_files.sort()

# Rename the files to ascending numbers
for i, old_name in enumerate(image_files, 1):
    extension = os.path.splitext(old_name)[1]
    new_name = f"{i}{extension}"
    os.rename(old_name, new_name)
