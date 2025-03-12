from exif_utils import get_exif_date

def rename_by_exif(file, params, index, folder_path):
    date = get_exif_date(os.path.join(folder_path, file))
    name, ext = os.path.splitext(file)
    return f"{date if date else 'Unknown'}_{name}{ext}"
