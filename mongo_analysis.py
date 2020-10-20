import json

import pandas as pd
from pymongo import MongoClient

import mongo_info as dbinfo
import plotly.express as px


def percentage_hispanic():
    myclient = MongoClient(dbinfo.mongourl, username=dbinfo.username, password=dbinfo.password)
    db = myclient["census"]

    state_name = "Florida"

    result = _percentage_hispanic_helper(db, state_name)

    df = pd.DataFrame(list(result))

    with open("Census_Data/geojson-counties-fips.json", 'r') as fh:
        counties = json.load(fh)

    print(df)

    fig = px.choropleth(df, geojson=counties, locations='fips', color='Hispanic_Perc',
                        scope='usa', labels={"Hispanic_Perc": "Hispanic Percentage"})

    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    fig.show()


def _percentage_hispanic_helper(db, state_name):
    return db.get_collection(name=state_name).aggregate([
        {"$match": {"$and": [{"state-co": {"$ne": "12   "}}, {"COUNTY": {"$ne": None}}]}},
        {
            "$group": {
                "_id": {
                    "$concat": [
                        {"$toString": "$STATE"},
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
                },
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


if __name__ == '__main__':
    percentage_hispanic()
