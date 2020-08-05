import os
"""
ROOT_FOLDER_TO_SCAN = full path to the folder that contains images to be converted
                    it can be a directory with subdirectories in this case the script will create a 'print' folder
                    in each root directory with .pdf file containing all images.
"""
home_path = os.environ['HOMEPATH'].replace('\\', '/')
ROOT_FOLDER_TO_SCAN = f'C:{home_path}/Downloads/activitati/'

"""
    EXTENSIONS_ALLOWED: the list of allowed image's extensions to be converted and saved in .pdf file
"""
EXTENSIONS_ALLOWED = ('*.jpg', '*.png', '*.jpeg')

"""
    PRINT_FOLDER_NAME: the name of the new folder that will be created in current scanned folder
                        to store the .pdf file.
"""
PRINT_FOLDER_NAME = 'print'
