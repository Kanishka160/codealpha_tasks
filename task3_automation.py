import os
import shutil

source_folder = "source"
destination_folder = "destination"

count = 0

for file in os.listdir(source_folder):
    if file.endswith((".jpg", ".png", ".jpeg")):
        src = os.path.join(source_folder, file)
        dest = os.path.join(destination_folder, file)

        shutil.move(src, dest)
        print(file, "moved!")
        count += 1

print("Total files moved:", count)