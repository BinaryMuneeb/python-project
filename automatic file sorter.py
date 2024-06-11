import os
import shutil

path = r"C:/Users/a2z/Downloads/shutil/"
print(os.listdir(path))

folder_names = ["pic", "document", "excel file"]

# Create folders if they don't exist
for folder in folder_names:
    if not os.path.exists(os.path.join(path, folder)):
        os.makedirs(os.path.join(path, folder))

# Move files to the appropriate folders
files = os.listdir(path)
for file in files:
    if file.endswith(".xlsx"):
        shutil.move(os.path.join(path, file), os.path.join(path, "excel file", file))
for file in files:
    if file.endswith(".docx"):
        shutil.move(os.path.join(path, file), os.path.join(path, "document", file))
for file in files:
    if file.endswith(".png"):
        shutil.move(os.path.join(path, file), os.path.join(path, "pic", file))
