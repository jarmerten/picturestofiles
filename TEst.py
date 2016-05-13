import zipfile
from PIL import Image
import os
import sys
import shutil
import json


def main():
    filelocation = sys.argv[1]
    check_valid_path(filelocation)
    filepath = file_path(filelocation)
    start_relocation(filepath, filelocation)
    data = open_manifest(filepath)
    create_new_folders(data, filepath)
    remove_manifest(data,filepath)

def check_valid_path(filelocation):
    if os.path.exists(filelocation) == True:
        return
    else:
        print('The file path is not valid, please retry with valid path....')


def file_path(filelocation):
    filepath = os.path.splitext(filelocation)[0]
    return filepath


def start_relocation(filepath, filelocation):
    with zipfile.ZipFile(filelocation) as myzip:
        set_file_path(filepath, myzip)


def set_file_path(filepath, myzip):
    print(filepath)
    myzip.extractall(filepath)
    print('starting......')
    return

def open_manifest(filepath):
    with open((filepath + '\\manifest.json')) as manifest_folders:
        data = json.load(manifest_folders)
        for line in manifest_folders:
            data.append(json.loads(line))
        return data


def create_new_folders(data,filepath):
    for directory_structure in data['directory_structure']:
        os.makedirs(filepath + '\\' + directory_structure)
        create_new_interior_folders(data, directory_structure, filepath)


def create_new_interior_folders(data,directory_structure,filepath):
    for main_storage in data['directory_structure'][directory_structure]:
        os.makedirs(filepath + '\\' + directory_structure + '\\' + main_storage)
        access_manifest_lines(data, directory_structure, main_storage, filepath)


def access_manifest_lines(data,directory_structure,main_storage,filepath):
    for photo_types in data['directory_structure'][directory_structure][main_storage]:
        check_for_interior_folders(data, filepath, photo_types, directory_structure, main_storage)


def check_for_interior_folders(data,filepath,photo_types,directory_structure,main_storage):
    if photo_types.endswith('jpg') or photo_types.endswith('jpeg'):
        create_first_thumbnails(filepath, directory_structure, main_storage, photo_types)
    else:
        new_interior_folder(data,filepath,photo_types,directory_structure,main_storage)


def create_first_thumbnails(filepath,directory_structure,main_storage,photo_types):
    im = size_image(filepath, photo_types)
    im.save(filepath + '\\' + directory_structure + '\\' + main_storage + '\\' + photo_types + ".thumbnail.jpg")
    shutil.move(filepath + '\\' + photo_types, filepath + '\\' + directory_structure + '\\' + main_storage + '\\' + photo_types)


def create_interior_thumbnails(filepath,directory_structure,main_storage,photo_types, original_photos):
    im = size_image(filepath, original_photos)
    im.save(filepath + '\\' + directory_structure + '\\' + main_storage + '\\' + photo_types + '\\' + original_photos + ".thumbnail.jpg")
    shutil.move(filepath + '\\' + original_photos,filepath + '\\' + directory_structure + '\\' + main_storage + '\\' + photo_types + '\\' + original_photos)


def move_back_folder_location(data):
    filename = data['zip_name']
    storefilename = os.path.splitext(filename)[0]
    return storefilename


def check_for_picture(filepath,original_photos,directory_structure,main_storage,photo_types):
    if original_photos.endswith('jpg') or original_photos.endswith('jpeg'):
        create_interior_thumbnails(filepath, directory_structure, main_storage, photo_types, original_photos)
    else:
        pass


def new_interior_folder(data,filepath,photo_types,directory_structure,main_storage):
    os.makedirs(filepath + '\\' + directory_structure + '\\' + main_storage + '\\' + photo_types)
    for original_photos in data['directory_structure'][directory_structure][main_storage][photo_types]:
        check_for_picture(filepath, original_photos, directory_structure, main_storage, photo_types)


def size_image(filepath, photo_location):
    size = 100, 100
    im = Image.open(filepath + '\\' + photo_location)
    im.thumbnail(size)
    return im


def remove_manifest(data,filepath):
    storefilename = move_back_folder_location(data)
    os.remove(filepath + '\\manifest.json')
    shutil.make_archive(os.path.dirname(filepath) + '\\' + storefilename, "zip", filepath)
    shutil.rmtree(filepath)
    print('finished')


if __name__ == "__main__":
    main()
