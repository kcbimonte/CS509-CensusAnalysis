import folder_paths as fpaths

from zipfile import ZipFile


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for state_path in fpaths.location_paths:
        state_name = state_path.split("/")[1]

        print("Processing", state_name)

        with ZipFile(state_path + ".zip", 'r') as zipObj:
            zipObj.extractall(state_path)

        print(state_name, "Processed")
