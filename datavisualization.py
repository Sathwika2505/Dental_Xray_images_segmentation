from data_extraction import extract_data
from PIL import Image
import requests
from io import BytesIO
import os 
import pathlib 
import zipfile
import random

def open_random_images(path):
    # Get a list of all files in the folder
    all_files = os.listdir(path)
    random.shuffle(all_files)
    image_names = all_files[:4]
    image_paths = []
    for i in range(4):
        image_path = os.path.join(path, image_names[i])
        image_paths.append(image_path)
    return image_paths
    

def visualise_image():
    url = extract_data()
    images = open_random_images(os.path.join(os.getcwd(),"jpg_images"))
    for i in range(4):
        image = Image.open(images[i])
        image.save('sample'+str(i)+'.jpg')
    return url

visualise_image()