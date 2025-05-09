import json
import os
from typing import Dict, Any


def get_nested_value(data: Dict[str, Any], path: str):
    keys = path.split(".")
    for key in keys:
        if not isinstance(data, dict):
            return None
        data = data.get(key)
    return data

def get_dataframe(folder_path, fields_to_extract):
    contents = []
    if os.path.exists(folder_path):
        print(f"Folder exists: {folder_path}")
    else:
        print(f"Folder does not exist: {folder_path}")
    for root, dirs, files in os.walk(folder_path):
        print(f"Currently exploring: {root}")
        # print(f"Subdirectories: {dirs}")
        print(f"Files: {files}")
        for file in files:
            if file.lower().endswith('.json'):
                filepath = root + '/' + file
                # print(filepath)
                with open(filepath, 'r') as jsoncontent:
                    bill = json.load(jsoncontent)
                    #print(bill)
                    row = {
                        column_name: get_nested_value(bill, json_path)
                        for column_name, json_path in fields_to_extract.items()
                    }
                    # print(fields_to_extract.items())
                    # print(row)
                    contents.append(row)
                    
    return contents