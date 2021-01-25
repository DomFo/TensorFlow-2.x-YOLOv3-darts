import os
import shutil
from zipfile import ZipFile


def get_file_list(path: str, extension: str = None, sort: bool = False):
    file_list = os.listdir(path)
    if "images" in extension:
        extension = ["jpg", "jpeg", "png", "bmp", "svg"]
    else:
        extension = [extension]
    if sort:
        file_list.sort()
    if extension is not None:
        files_out = [os.path.join(path, f) for f in file_list if any(ext in f for ext in extension)]
    else:
        files_out = [os.path.join(path, f) for f in file_list]
    return files_out


data_file = "darts_data.zip"
data_sets = ["test", "train", "valid"]
RENAME = False

if os.path.exists("data"):
    shutil.rmtree("data")

with ZipFile(data_file, 'r') as zip_file:
    # extracting all the files
    print(f'Extracting all {data_file} files now...')
    zip_file.extractall("data")
    print('Done!')

if RENAME:
    for data_set in data_sets:
        print(data_set)
        img_path = os.path.join("data", f'darts_{data_set}')
        annotations_file = os.path.join("data", f'darts_{data_set}.txt')

        files = get_file_list(img_path, extension="images", sort=True)
        lines = open(annotations_file).readlines()
        lines.sort()
        assert len(lines) == len(files)  # must be given in yolo v3 format

        for line, data_file in enumerate(files):
            print(f'{line}/{len(files)}')
            old_file = os.path.split(data_file)[-1]
            if ".rf." in old_file:
                new_file = old_file.split(".")[0]
                new_file = new_file.replace("_", ".")
                new_file = new_file.replace(".jpg", f'_{str(line).zfill(3)}.jpg')
                new_file = os.path.join(img_path, new_file)

                lines[line] = lines[line].replace(old_file, new_file)
                os.rename(data_file, new_file)

        with open(annotations_file, 'w') as naf:
            for new_line in lines:
                naf.write("%s" % new_line)
