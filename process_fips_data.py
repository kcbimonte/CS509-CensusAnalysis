import json
from os import path

import pandas as pd

file_fips = "Census_Data/fips-decoded.json"


def _add_state_names(tempdf):
    with open("Census_Data/state_fips.csv", 'r') as f:
        df = pd.read_csv(f, header=None, names=['STATE', 'State Name'], dtype=str)

    df = df.merge(tempdf, on=["STATE"])

    df['State Name'] = df['State Name'].str.title()

    df['Location'] = df['NAME'] + ', ' + df['State Name']

    return df


def read_file():
    if not path.exists(file_fips):
        with open("Census_Data/geojson-counties-fips.json", 'r') as f:
            data = json.load(f)

        data = pd.DataFrame(data['features'])

        pd.set_option('display.max_columns', None)

        df = pd.json_normalize(data['properties'])

        tempdf = df.iloc[:, 1:4]

        tempdf['fips'] = tempdf['STATE'] + tempdf['COUNTY']

        df = _add_state_names(tempdf)

        df = df.sort_values(by=['fips'])

        with open(file_fips, 'w') as f:
            df.to_json(f, orient='records')
    else:
        print('File exists')


if __name__ == '__main__':
    read_file()
