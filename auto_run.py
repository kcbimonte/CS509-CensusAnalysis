import census_df as cdf
import folder_paths as fpaths
from os import path


# To dataframe
def to_json(spath=fpaths.alabama_path):
    cdf.read(spath)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for state_path in fpaths.location_paths:
        state_name = state_path.split("/")[1]

        if not path.exists("State_JSONs/" + state_name + ".json"):
            print("Processing", state_name)

            print("\tStarting to create dataframe")

            to_json(state_path)

            print(state_name, "Processed")
        else:
            print(state_name, "Already exists, skipping.")
