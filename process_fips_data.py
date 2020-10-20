import pandas as pd
import json
import mongo_info as dbinfo

from pymongo import MongoClient

file_fips = "Census_Data/FIPS_ST_COU_Area-Name"


def read_file():
    data = []

    f = open(file_fips + ".txt", 'r')

    for line in f:
        line = line.strip('\n')
        line = line.strip()

        if not len(line) < 7:
            state = line[0:2]
            county = line[3:6]
            county_name = line[7:]
            data.append([state, county, county_name])

    df = pd.DataFrame(data, columns=["State_Code", "County_Code", "County_Name"])

    df.to_json(file_fips + ".json", orient='records')


def upload_to_mongo():
    myclient = MongoClient(dbinfo.mongourl, username=dbinfo.username, password=dbinfo.password)

    db = myclient["census"]

    Collection = db['FIPS_Codes']

    with open(file_fips + ".json") as file:
        file_data = json.load(file)

    if isinstance(file_data, list):
        Collection.insert_many(file_data)
    else:
        Collection.insert_one(file_data)


if __name__ == '__main__':
    # read_file()
    upload_to_mongo()
