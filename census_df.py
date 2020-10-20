# Meant for converting the data into a data from

import pandas as pd

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
    print("Reading Geo Info")
    df = pd.concat([df, pd.read_csv(state_path + "geo2010_processed.txt",
                                    header=0,
                                    usecols=[9, 10, 57])],
                   axis=1, sort=False)
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
                                             120, 121, 122, 123, 124, 125,     # 121
                                             126, 127, 128, 129, 130, 131,     # 127
                                             132, 133, 134, 135, 136, 137,     # 133
                                             138, 139, 140, 141, 142, 143,     # 139
                                             144, 145, 146, 147, 148, 149,     # 145
                                             150, 151, 152, 153, 154, 155,     # 151
                                             156, 157, 158, 159, 160, 161,     # 157
                                             162, 163, 164, 165, 166, 167,     # 163
                                             168, 169, 170, 171, 172, 173,     # 169
                                             174, 175, 176, 177, 178, 179,     # 175
                                             180, 181, 182, 183, 184, 185,     # 181
                                             186, 187, 188, 189, 190, 191,     # 187
                                             192, 193, 194, 195, 196, 197,     # 193
                                             198])],                      # 194
                   axis=1, sort=False)

    print("Starting to write JSON")

    df.to_json("State_JSONs/" + state_name + ".json", orient='records')

    print("Finished writing JSON")
