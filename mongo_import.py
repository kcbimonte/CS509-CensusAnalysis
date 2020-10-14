import json
import os

from pymongo import MongoClient


def single_run(state_file="Alabama.json"):
    myclient = MongoClient("mongodb://192.168.1.101:27017/",
                           username='admin',
                           password='legos11')

    db = myclient["census"]

    state_name = state_file.split(".")[0]

    Collection = db[state_name]

    with open("State_JSONs/" + state_file) as file:
        file_data = json.load(file)

    if isinstance(file_data, list):
        Collection.insert_many(file_data)
    else:
        Collection.insert_one(file_data)


def multi_run():
    for filename in os.listdir("State_JSONs"):
        single_run(filename)


if __name__ == '__main__':
    # Single Run for Testing
    # single_run("Alabama.json")

    # Multi Run for Production
    multi_run()
