# Auto-File-Sorting

Automatically organizes files in a folder by file type (e.g., `.pdf`, `.jpg`, `.mp4`) into corresponding subfolders.

##  Features
- Sorts all files in a directory based on file extensions.
- Creates subfolders if they don't exist.
- Ignores folders and only processes files.

##  How to Use
1. Run the script:
   ```bash
   python auto_file_sorter.py
2. Input the full path of the folder you want to organize.(e.g., 'c/Users/User/Downloads')
4. File will be moved into folder like /pdf, /jpg, /mp4, etc.

## Example
Your folder :
book.pdf
photo.jpg
video.mp4

After running the program it will be :
pdf/book.pdf
jpg/photo.jpg
mp4/video.mp4
