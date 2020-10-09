import pandas as pd
import folder_paths as fpaths
from os import path

file_geoheaders = "Census_Data/GeoHeaders.txt"
file_geofile = "geo2010.ur1"


def createGeoHeaders():
    f = open(file_geoheaders, 'r')

    headers = []

    for line in f:
        first_part = line.split('.')[0]

        first_part = first_part.split(" ")

        start_pos = int(first_part[0][1:]) - 1
        header = first_part[1]
        field_size = int(first_part[2][1])  # - 1
        end_pos = start_pos + field_size

        headers.append([header, start_pos, end_pos])

    f.close()
    return headers


def process_geo_info(geo_headers, path=fpaths.alabama_path):
    state_abbr = path.split("/")[2][:2]
    state_path = path + "/" + state_abbr

    geo_info = []

    geo_headers_only = [row[0] for row in geo_headers]

    file = open(state_path + file_geofile)

    lines = file.readlines()

    file.close()

    for line in lines:
        line_row = []

        for row in geo_headers:
            start = row[1]
            end = row[2]
            value = line[start:end]
            line_row.append(value)

        geo_info.append(line_row)

    df = pd.DataFrame(geo_info, columns=geo_headers_only)
    df.to_csv(state_path+"geo2010_processed.txt", index=False)


if __name__ == '__main__':
    geo_headers = createGeoHeaders()
    for state_path_global in fpaths.location_paths:
        state_name = state_path_global.split("/")[1]
        state_abbr = state_path_global.split("/")[2][:2]
        state_path = state_path_global + "/" + state_abbr

        if not path.exists(state_path+"geo2010_processed.txt"):
            print("Processing", state_name)
            process_geo_info(geo_headers, state_path_global)
            print(state_name, "Processed")
        else:
            print(state_name, "Already exists, skipping.")
