import json

import pandas as pd
import plotly.express as px
from pymongo import MongoClient

import mongo_info as dbinfo


class Helpers:
    @staticmethod
    def fix_fips_helper():
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

    @staticmethod
    def join_fips_data(df):
        with open("../Census_Data/fips-decoded.json", 'r') as f:
            df_fips = pd.read_json(f, orient='records', dtype=False)
        df = df.merge(df_fips, on=["fips"])
        return df

    @staticmethod
    def get_census():
        my_client = MongoClient(dbinfo.mongourl, username=dbinfo.username, password=dbinfo.password)
        return my_client["census"]

    @staticmethod
    def plot(df, color, labels):
        with open("../Census_Data/geojson-counties-fips.json", 'r') as fh:
            counties = json.load(fh)

        fig = px.choropleth(df, geojson=counties, locations='fips', color=color, hover_name='Location',
                            scope='usa', labels=labels)

        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
        fig.show()
