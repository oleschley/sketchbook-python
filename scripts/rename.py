import os
import re
import glob

PATH = '/path/to/files'

def main(path: str):
    directories = glob.glob(f'{path}/*')

    for directory in directories:
        files = glob.glob(f'{directory}/*')
        for file in files:
            os.rename(file, format(file))


def format(file: str):

    file = file.lower()
    file = re.sub('this', 'that', file)
    return file

if __name__ == "__main__":
    main(PATH)