import os
from os import path

import pandas as pd

import analysis.helper.helper_functions as h


def percentage_white():
    helper = h.Helpers()
    if not path.exists("../Census_Analysis/white_perc.json"):
        db = helper.get_census()

        state_name = "Alabama"
        result = _percentage_white_helper(db, helper, state_name)
        df = pd.DataFrame(list(result))
        print("Added", state_name)

        for filename in os.listdir("../State_JSONs"):
            state_name = filename.split(".")[0]
            if state_name != "Alabama":
                result = _percentage_white_helper(db, helper, state_name)
                temp_df = pd.DataFrame(list(result))
                df = df.append(temp_df, ignore_index=True)
                print("Added", state_name)

        df = helper.join_fips_data(df)

        df = df[['fips', 'White_Perc', 'Location']]

        with open("../Census_Analysis/white_perc.json", 'w') as file:
            df.to_json(file, orient='records')
    else:
        with open("../Census_Analysis/white_perc.json", 'r') as file:
            df = pd.read_json(file, orient='records', dtype=False)

    labels = {"White_Perc": "White Percentage"}
    color = 'White_Perc'

    helper.plot(df, color, labels)


def _percentage_white_helper(db, helper, state_name):
    return db.get_collection(name=state_name).aggregate([
        {"$match": {"$and": [{"state-co": {"$ne": "12   "}}, {"COUNTY": {"$ne": None}}]}},
        {
            "$group": {
                "_id": helper.fix_fips_helper(),
                "Total_Pop": {"$sum": "$Total_Pop"},
                "Total_White": {"$sum": "$Total_Race_White"}
            }
        },
        {
            "$project": {
                "_id": 0,
                "fips": "$_id",
                "White_Perc": {"$multiply": [{"$divide": ["$Total_White", "$Total_Pop"]}, 100]}
            }
        }
    ])
