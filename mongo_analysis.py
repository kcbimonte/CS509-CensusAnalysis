import json
import os

import pandas as pd
from pymongo import MongoClient
from os import path

import mongo_info as dbinfo
import plotly.express as px


def percentage_hispanic():
    if not path.exists("Census_Analysis/hispanic_perc.json"):
        myclient = MongoClient(dbinfo.mongourl, username=dbinfo.username, password=dbinfo.password)
        db = myclient["census"]

        state_name = "Alabama"
        result = _percentage_hispanic_helper(db, state_name)
        df = pd.DataFrame(list(result))
        print("Added", state_name)

        for filename in os.listdir("State_JSONs"):
            state_name = filename.split(".")[0]
            if state_name != "Alabama":
                result = _percentage_hispanic_helper(db, state_name)
                temp_df = pd.DataFrame(list(result))
                df = df.append(temp_df, ignore_index=True)
                print("Added", state_name)

        with open("Census_Data/fips-decoded.json", 'r') as f:
            df_fips = pd.read_json(f, orient='records', dtype=False)

        df = df.merge(df_fips, on=["fips"])

        df = df[['fips', 'Hispanic_Perc', 'Location']]

        with open("Census_Analysis/hispanic_perc.json", 'w') as file:
            df.to_json(file, orient='records')
    else:
        with open("Census_Analysis/hispanic_perc.json", 'r') as file:
            df = pd.read_json(file, orient='records', dtype=False)

    with open("Census_Data/geojson-counties-fips.json", 'r') as fh:
        counties = json.load(fh)

    fig = px.choropleth(df, geojson=counties, locations='fips', color='Hispanic_Perc', hover_name='Location',
                        scope='usa', labels={"Hispanic_Perc": "Hispanic Percentage"})

    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    fig.show()


def _percentage_hispanic_helper(db, state_name):
    return db.get_collection(name=state_name).aggregate([
        {"$match": {"$and": [{"state-co": {"$ne": "12   "}}, {"COUNTY": {"$ne": None}}]}},
        {
            "$group": {
                "_id": _fix_fips_helper(),
                "Total_Pop": {"$sum": "$Total_Pop"},
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


def _fix_fips_helper():
    return {
        "$concat": [
            {
                "$cond": [
                    {"$and": [{"$lte": ["$STATE", 9]}, {"$gt": ["$STATE", 0]}]},
                    {
                        "$concat": ["0", {"$toString": "$STATE"}]
                    },
                    {"$toString": "$STATE"}
                ]
            },
            {
                "$cond": [
                    {"$and": [{"$lte": ["$COUNTY", 99]}, {"$gt": ["$COUNTY", 9]}]},
                    {
                        "$concat": ["0", {"$toString": "$COUNTY"}]
                    },
                    {
                        "$cond": [
                            {"$and": [{"$lte": ["$COUNTY", 9]}, {"$gt": ["$COUNTY", 0]}]},
                            {
                                "$concat": ["00", {"$toString": "$COUNTY"}]
                            },
                            {"$toString": "$COUNTY"}
                        ]
                    }
                ]
            }

        ]
    }


if __name__ == '__main__':
    percentage_hispanic()
