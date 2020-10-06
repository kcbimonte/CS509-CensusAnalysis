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
                                    usecols=[6, 7, 8, 9, 10])],
                   axis=1, sort=False)
    print("Reading File 03")
    df = pd.concat([df, pd.read_csv(path + File03.file03 + ".ur1",
                                    header=None,
                                    names=File03.headers,
                                    usecols=[6, 7, 8, 9, 10, 11,
                                             12, 13, 14, 15, 16, 17])],
                   axis=1, sort=False)
    # print(df.iloc[0:10, 0:5])
    # print("Reading File 04")

    df.to_json("State_JSONs/" + state_name + ".json", orient='records', lines=True)
