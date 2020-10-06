import census_df as cdf
import folder_paths as fpaths
import os

from zipfile import ZipFile


# Extract the zip file
def extract_zip(path=fpaths.alabama_path):
    with ZipFile(path + ".zip", 'r') as zipObj:
        zipObj.extractall(path)


# To dataframe
def to_json(path=fpaths.alabama_path):
    cdf.read(path)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    state_path = fpaths.alabama_path

    if not os.path.isdir("./" + state_path):
        print("Directory does not exist. Starting to extract")
        extract_zip(state_path)
        print("Directory is extracted")

    print("Starting to create dataframe")
    to_json(state_path)
