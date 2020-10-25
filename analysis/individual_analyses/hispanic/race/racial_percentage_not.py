import os
from os import path

import pandas as pd

import analysis.helper.helper_functions as h

state_path = '../State_JSONs'
folder_path = '../Census_Analysis/Hispanic/Race/'


def percentage(passed_name, field_name, field_descriptor):
    full_path = folder_path + passed_name + '_perc_not.json'

    helper = h.Helpers()
    if not path.exists(full_path):
        db = helper.get_census()

        state_name = "Alabama"
        result = _percentage_helper(db, helper, state_name, passed_name)
        df = pd.DataFrame(list(result))
        print("Added", state_name)

        for filename in os.listdir(state_path):
            state_name = filename.split(".")[0]
            if state_name != "Alabama":
                result = _percentage_helper(db, helper, state_name, passed_name)
                temp_df = pd.DataFrame(list(result))
                df = df.append(temp_df, ignore_index=True)
                print("Added", state_name)

        df = helper.join_fips_data(df)

        df = df[['fips', field_name, 'Location']]

        with open(full_path, 'w') as file:
            df.to_json(file, orient='records')
    else:
        with open(full_path, 'r') as file:
            df = pd.read_json(file, orient='records', dtype=False)

    labels = {field_name: field_descriptor}
    color = field_name

    helper.plot(df, color, labels)


def _percentage_helper(db, helper, state_name, name):
    return db.get_collection(name=state_name).aggregate([
        {"$match": {"$and": [{"state-co": {"$ne": "12   "}}, {"COUNTY": {"$ne": None}}]}},
        {
            "$group": {
                "_id": helper.fix_fips_helper(),
                "Total_Pop": {"$sum": "$Total_Hispanic_Race_All"},
                "Total_" + name.title(): {"$sum": "$Total_Not_Hispanic_Race_" + name.title()}
            }
        },
        {
            "$project": {
                "_id": 0,
                "fips": "$_id",
                name.title() + "_Perc": {"$multiply": [{"$divide": ["$Total_" + name.title(), "$Total_Pop"]}, 100]}
            }
        }
    ])
