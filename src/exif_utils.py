from PIL import Image
from PIL.ExifTags import TAGS

def get_exif_date(file_path):
    try:
        image = Image.open(file_path)
        exif_data = image._getexif()
        if exif_data:
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                if tag_name == "DateTimeOriginal":
                    return value.replace(':', '-').split(' ')[0]  # Format YYYY-MM-DD
    except Exception as e:
        print(f"Error reading EXIF data: {e}")
    return None
