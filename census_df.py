# Meant for converting the data into a data from

import pandas as pd
import constants as c


def read(path=c.alabama_path):
    print("Read")
    df = pd.read_csv(path + c.file01 + ".ur1", header=None)
    print(df.head())
