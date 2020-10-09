# Meant for converting the data into a data from

import pandas as pd

import process_geo_headers as rgh
import File_Definitions.File01 as File01
import File_Definitions.File02 as File02
import File_Definitions.File03 as File03


def read(path):
    state_name = path.split("/")[1]
    state_abbr = path.split("/")[2][:2]

    state_path = path + "/" + state_abbr

    print("Reading File 01")
    df = pd.read_csv(state_path + File01.file01 + ".ur1",
                     header=None,
                     names=File01.headers)
    # print("Reading GeoFile")
    #
    # geo_headers = rgh.createGeoHeaders()
    #
    # geo_info = rgh.read_geo_info(geo_headers, path)
    #
    # df = pd.concat([df, geo_info['ZCTA5']], axis=1, sort=False)
    # print('Appended Zip Code')
    print("Reading File 02")
    df = pd.concat([df, pd.read_csv(state_path + File02.file02 + ".ur1",
                                    header=None,
                                    names=File02.headers,
                                    usecols=[5, 6, 7, 8, 9])],
                   axis=1, sort=False)
    print("Reading File 03")
    df = pd.concat([df, pd.read_csv(state_path + File03.file03 + ".ur1",
                                    header=None,
                                    names=File03.headers,
                                    usecols=[5, 6, 7, 8, 9, 10, 11,            # 7
                                             12, 13, 14, 15, 16, 17,           # 13
                                             18, 19, 20, 21, 22, 23,           # 19
                                             24, 25, 26, 27, 28, 29,           # 25
                                             30, 31, 32, 33, 34, 35,           # 31
                                             36, 37, 38, 39, 40, 41,           # 37
                                             42, 43, 44, 45, 46, 47,           # 43
                                             48, 49, 50, 51, 52, 53,           # 49
                                             54, 55, 56, 57, 58, 59,           # 55
                                             60, 61, 62, 63, 64, 65,           # 61
                                             66, 67, 68, 69, 70, 71,           # 67
                                             72, 73, 74, 75, 76, 77,           # 73
                                             78, 79, 80, 81, 82, 83,           # 79
                                             84, 85, 86, 87, 88, 89,           # 85
                                             90, 91, 92, 93, 94, 95,           # 91
                                             96, 97, 98, 99, 100, 101,         # 97
                                             102, 103, 104, 105, 106, 107,     # 103
                                             108, 109, 110, 111, 112, 113,     # 109
                                             114, 115, 116, 117, 118, 119,     # 115
                                             120, 121, 122, 123, 124, 125])],  # 121
                   axis=1, sort=False)

    print("Starting to write JSON")

    df.to_json("State_JSONs/" + state_name + ".json", orient='records')

    print("Finished writing JSON")
