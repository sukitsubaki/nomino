import os
import sys
from cli import show_menu
from file_utils import get_files, rename_files
from log_utils import log_changes
from progress import show_progress
from exif_utils import get_exif_date

def main():
    print("Welcome to Nomino - Your smart file renamer!")
    folder_path = input("Enter the folder path: ").strip()
    
    if not os.path.isdir(folder_path):
        print("Invalid folder path!")
        sys.exit(1)
    
    files = get_files(folder_path)
    if not files:
        print("No files found!")
        sys.exit(1)
    
    choice, params = show_menu()
    new_filenames = rename_files(files, choice, params, folder_path)
    log_changes(files, new_filenames)
    print("Renaming completed!")

if __name__ == "__main__":
    main()
