import json
import os
import sys
from typing import Any, Dict
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..')))
from utils import load_bill_data


"""
Extract legislator data from house and senator json files and return it as a combined list
"""
fields = {
    "First Name": "First Name",
    "Last Name": "Last Name",
    "District": "District",
    "Party": "Party",
}

housefilepath = '../data/house.json'
senatefilepath = '../data/senators.json'

def get_nested_value(data: Dict[str, Any], path: str):
    """
    Look up keys in json file and return values assigned to keys
    """
    keys = path.split(".")
    for key in keys:
        if not isinstance(data, dict):
            return None
        data = data.get(key)
    return data

def get_data(file_path, fields_to_extract):
    """
    Retrieve data from json file and return as a list
    """
    contents =[]
    with open(file_path, 'r') as jsoncontent:
                        bill = json.load(jsoncontent)
                        #print(bill)
                        for item in bill:
                            row = {
                                column_name: get_nested_value(item, json_path)
                                for column_name, json_path in fields_to_extract.items()
                            }
                        # print(fields_to_extract.items())
                        # print(row)
                            contents.append(row)
    return contents


def get_house_and_senate():   
    """
    Retrieve house and senate data and combine them
    """
    house = get_data(housefilepath, fields)
    senate = get_data(senatefilepath, fields)
    return house+senate

