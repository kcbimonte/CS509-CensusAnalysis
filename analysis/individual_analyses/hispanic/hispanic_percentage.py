import os
from os import path

import pandas as pd

import analysis.helper.helper_functions as h


def percentage_hispanic():
    helper = h.Helpers()

    if not path.exists("../Census_Analysis/hispanic_perc.json"):
        db = helper.get_census()

        state_name = "Alabama"
        result = _percentage_hispanic_helper(db, helper, state_name)
        df = pd.DataFrame(list(result))
        print("Added", state_name)

        for filename in os.listdir("../State_JSONs"):
            state_name = filename.split(".")[0]
            if state_name != "Alabama":
                result = _percentage_hispanic_helper(db, helper, state_name)
                temp_df = pd.DataFrame(list(result))
                df = df.append(temp_df, ignore_index=True)
                print("Added", state_name)

        df = helper.join_fips_data(df)

        df = df[['fips', 'Hispanic_Perc', 'Location']]

        with open("../Census_Analysis/hispanic_perc.json", 'w') as file:
            df.to_json(file, orient='records')
    else:
        with open("../Census_Analysis/hispanic_perc.json", 'r') as file:
            df = pd.read_json(file, orient='records', dtype=False)

    color = 'Hispanic_Perc'
    labels = {"Hispanic_Perc": "Hispanic Percentage"}

    fig = helper.plot(df, color, labels)

    file_path = "../web_json/hispanic_percentages.json"

    if not path.exists(file_path):
        import plotly.io as pio
        pio.write_json(fig, file=file_path)
    else:
        print("Plot already written")


def _percentage_hispanic_helper(db, helper, state_name):
    return db.get_collection(name=state_name).aggregate([
        {"$match": {"$and": [{"state-co": {"$ne": "12   "}}, {"COUNTY": {"$ne": None}}]}},
        {
            "$group": {
                "_id": helper.fix_fips_helper(),
                "Total_Pop": {"$sum": "$Total_Hispanic_All"},
                "Total_Hisp": {"$sum": "$Total_Hispanic_Yes"}
            }
        },
        {
            "$project": {
                "_id": 0,
                "fips": "$_id",
                "Hispanic_Perc": {"$multiply": [{"$divide": ["$Total_Hisp", "$Total_Pop"]}, 100]}
            }
        }
    ])
