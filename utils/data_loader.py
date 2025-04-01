import json
import glob
import pandas as pd
from typing import Dict, Any

def load_bill_data(json_paths: str, fields_to_extract: Dict[str, str]) -> pd.DataFrame:
    """
    Load bill data from JSON files and extract specified fields.

    Args:
        json_paths (str): Glob pattern to locate JSON files (e.g. 'data/*.json').
        fields_to_extract (dict): Dict where keys are desired DataFrame column names,
                                  and values are dot-paths to JSON fields (e.g. 'bill_data.title').

    Returns:
        pd.DataFrame: DataFrame containing extracted fields.
    """
    def get_nested_value(data: Dict[str, Any], path: str):
        keys = path.split(".")
        for key in keys:
            if not isinstance(data, dict):
                return None
            data = data.get(key)
        return data

    data = []
    for file in glob.glob(json_paths)[:]:
        with open(file, "r") as f:
            bill = json.load(f)
            row = {
                column_name: get_nested_value(bill, json_path)
                for column_name, json_path in fields_to_extract.items()
            }
            data.append(row)

    return pd.DataFrame(data)
