from exif_utils import get_exif_date
import os

def sort_by_date(file, params, index, folder_path):
    date = get_exif_date(os.path.join(folder_path, file))
    subfolder = date if date else "Unknown"
    subfolder_path = os.path.join(folder_path, subfolder)
    os.makedirs(subfolder_path, exist_ok=True)
    return os.path.join(subfolder, file)
