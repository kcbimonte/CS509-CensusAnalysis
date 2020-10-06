# Meant for converting the data into a data from

import pandas as pd
import constants as c


def read():
    print("Read")
    df = pd.read_csv(c.alabama_path + c.file01 + ".ur1", header=None)
    print(df.head())
