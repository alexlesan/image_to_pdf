import glob
import os
import re

from PIL import Image

import config

images_dir = config.ROOT_FOLDER_TO_SCAN
extensions = config.EXTENSIONS_ALLOWED
print_folder_name = config.PRINT_FOLDER_NAME


def get_destination_pdf_path(source_folder):
    root_folder_name = source_folder.split('/')[-1]
    if len(root_folder_name) == 0:
        root_folder_name = source_folder.split('/')[-2]
    print_folder_path = f'{source_folder}/{print_folder_name}'
    pdf_file_path = f'{print_folder_path}/print_{root_folder_name}.pdf'

    # if folder doesn't exists, create it
    if not os.path.exists(print_folder_path):
        os.makedirs(print_folder_path)
    else:
        # remove the old .pdf file
        if os.path.isfile(pdf_file_path):
            os.remove(pdf_file_path)
    return pdf_file_path


def save_images_to_pdf(images_list, source_dir):
    if len(images_list) > 0:
        save_dir = get_destination_pdf_path(source_folder=source_dir)
        images_list[0].save(save_dir, save_all=True, quality=100,
                            append_images=images_list[1:])
        print('Images saved into:', save_dir)
    else:
        print('No images were found in:', source_dir)


def read_save_images(source_dir_images):
    print('Reading images from:', source_dir_images)
    images = []
    images_list = []
    str_ext = "|".join(map(str, extensions)).replace("*.", "")
    for ext in extensions:
        images_list.extend(glob.glob(os.path.join(source_dir_images, ext)))
    for image_path in images_list:
        f_text, f_ext = os.path.splitext(image_path)
        if any(re.findall(str_ext, f_ext, re.IGNORECASE)):
            img = Image.open(image_path)
            if img.mode == 'RGBA':
                img = img.convert("RGB")
            images.append(img)

    save_images_to_pdf(images, source_dir_images)

def scan_for_dirs(root_dir):
    folders = [f.path for f in os.scandir(root_dir) if f.is_dir()]
    return folders


if __name__ == "__main__":
    sub_folders = scan_for_dirs(images_dir)
    read_save_images(images_dir)
    if len(sub_folders) > 0:
        for folder in sub_folders:
            read_save_images(folder)