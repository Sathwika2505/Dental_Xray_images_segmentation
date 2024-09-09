import os
from PIL import Image

def extract_data():
    img_folder_path = "all-images"
    mask_folder_path = "unet-masks"
    ot_img_folder = "jpg_images"
    ot_mask_folder = "masks"
    if not os.path.exists(ot_img_folder):
        os.makedirs(ot_img_folder)
    if not os.path.exists(ot_mask_folder):
        os.makedirs(ot_mask_folder)
        
    for img in os.listdir(img_folder_path):
        img_path = os.path.join(img_folder_path, img)
        
        try:
            image = Image.open(img_path)
            img_name = os.path.splitext(img)[0]
            save_path = os.path.join(ot_img_folder, f"{img_name}.jpg")
            image.save(save_path)
            print(img)
        except Exception as e:
            print(f"Error processing {img}: {e}")
            
    for img in os.listdir(mask_folder_path):
        img_path = os.path.join(mask_folder_path, img)
        
        try:
            image = Image.open(img_path)
            img_name = os.path.splitext(img)[0]
            save_path = os.path.join(ot_mask_folder, f"{img_name}.jpg")
            image.save(save_path)
            print(img)
        except Exception as e:
            print(f"Error processing {img}: {e}")

    return img

extract_data()
