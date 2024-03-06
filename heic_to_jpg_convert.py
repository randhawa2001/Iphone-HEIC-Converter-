from PIL import Image 
from pillow_heif import register_heif_opener 
import os

register_heif_opener()

input_folder = "./New_data_room_2"
output_folder = "./New_data_room_2_conv"

os.makedirs(output_folder, exist_ok=True)

heic_files = [photo for photo in os.listdir(input_folder) if photo.lower().endswith('.heic')]
print(heic_files)

for photo in heic_files: 
    input_path = os.path.join(input_folder, photo)
    temp_img = Image.open(input_path) 
    output_path = os.path.join(output_folder, photo.replace('.HEIC','.jpg'))
    temp_img.save(output_path)
    print(f"Converted: {input_path} -> {output_path}")
 