import os
import shutil

source = "source_folder"
destination = "jpg_files"

os.makedirs(destination, exist_ok=True)

for file in os.listdir(source):
    if file.endswith(".jpg"):
        shutil.move(os.path.join(source, file), destination)
