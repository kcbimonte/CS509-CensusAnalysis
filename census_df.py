# Meant for converting the data into a data from

import pandas as pd
import folder_paths as fpaths
import File_Definitions.File01 as File01
import File_Definitions.File02 as File02
import File_Definitions.File03 as File03


def read(path=fpaths.alabama_path):
    state_name = path.split("/")[1]

    print("Reading File 01")
    df = pd.read_csv(path + File01.file01 + ".ur1",
                     header=None,
                     names=File01.headers)
    print("Reading File 02")
    df = pd.concat([df, pd.read_csv(path + File02.file02 + ".ur1",
                                    header=None,
                                    names=File02.headers,
                                    usecols=[5, 6, 7, 8, 9])],
                   axis=1, sort=False)
    print("Reading File 03")
    df = pd.concat([df, pd.read_csv(path + File03.file03 + ".ur1",
                                    header=None,
                                    names=File03.headers,
                                    usecols=[5, 6, 7, 8, 9, 10, 11,   # 7
                                             12, 13, 14, 15, 16, 17,  # 6
                                             18, 19, 20, 21, 22, 23,  # 6
                                             24, 25, 26, 27, 28, 29,  # 6
                                             30, 31, 32, 33, 34, 35,  # 6
                                             36, 37, 38, 39, 40, 41,  # 6
                                             42, 43, 44, 45, 46, 47,  # 6
                                             48, 49, 50, 51, 52, 53,  # 6
                                             54])],           # 1
                   axis=1, sort=False)
    # print(df.iloc[0:10, 0:5])
    # print("Reading File 04")

    print("Writing Dataframe to JSON")

    df.to_json("State_JSONs/" + state_name + ".json", orient='records')

    print("Finished writing Dataframe to JSON")
