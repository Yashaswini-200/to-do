from PIL import Image
from PIL.ExifTags import TAGS

def extract_metadata(image_path):
    image = Image.open(image_path)
    exif_data = image._getexif()
    if not exif_data:
        print("No EXIF metadata found in this image.")
        return

    for tag_id, value in exif_data.items():
        tag = TAGS.get(tag_id, tag_id)
        print(f"{tag:25}: {value}")
extract_metadata(r"C:\Users\YASHASWINI\OneDrive\Pictures\31b67ec7534d6bec4ac9aa0833e45eb5[1].jpg")