# file_sorter.py

import os
import shutil

def auto_sort(folder_path):
    if not os.path.exists(folder_path):
        print(f"❌ Folder '{folder_path}' not found!")
        return

    files = os.listdir(folder_path)
    for file in files:
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1].lower().strip('.')
            if not ext:
                ext = 'others'
            dest_folder = os.path.join(folder_path, ext)

            os.makedirs(dest_folder, exist_ok=True)

            shutil.move(file_path, os.path.join(dest_folder, file))
            print(f"📁 Moved '{file}' to '{ext}/'")

if __name__ == '__main__':
    folder = input("🗂️ Enter the folder path to sort: ").strip()
    auto_sort(folder)
