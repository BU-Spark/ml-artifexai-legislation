import json
import glob
import pandas as pd
from typing import Dict, Any

<<<<<<< HEAD
# import pandas as pd
# import glob
# import json
# from typing import Dict, Any

def load_bill_data(json_paths: str, fields_to_extract: Dict[str, str], with_outlier: bool = True) -> pd.DataFrame:
=======
def load_bill_data(json_paths: str, fields_to_extract: Dict[str, str]) -> pd.DataFrame:
>>>>>>> origin/dev-jasper
    """
    Load bill data from JSON files and extract specified fields.

    Args:
        json_paths (str): Glob pattern to locate JSON files (e.g. 'data/*.json').
        fields_to_extract (dict): Dict where keys are desired DataFrame column names,
                                  and values are dot-paths to JSON fields (e.g. 'bill_data.title').
<<<<<<< HEAD
        with_outlier (bool): If True, include bills with invalid URLs.
=======
>>>>>>> origin/dev-jasper

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
<<<<<<< HEAD
    for file in glob.glob(json_paths):
        with open(file, "r") as f:
            bill = json.load(f)
            
            if not with_outlier:
                pdf_url = get_nested_value(bill, 'download_pdf_url')
                if pdf_url in [None, ""]:
                    continue  # Skip this bill if 'pdf_url' is missing or empty
                
            # Extract the required fields
=======
    for file in glob.glob(json_paths)[:]:
        with open(file, "r") as f:
            bill = json.load(f)
>>>>>>> origin/dev-jasper
            row = {
                column_name: get_nested_value(bill, json_path)
                for column_name, json_path in fields_to_extract.items()
            }
<<<<<<< HEAD
            
=======
>>>>>>> origin/dev-jasper
            data.append(row)

    return pd.DataFrame(data)

<<<<<<< HEAD

=======
>>>>>>> origin/dev-jasper
# EXAMPLE USAGE
# root_path ='../../downloaded_legislation/'
# json_files = os.path.join(root_path, 'state/MA/*/*/*/*/*.json') # glob pattern for json files

# fields = {
#     "bill_url": "bill_data.url",
#     "title": "bill_data.title",
#     "text": "summary.text",
#     "sponsor": "sponsor.name",
#     "is_home_rule": "is_home_rule"
# }

# df = load_bill_data(json_files, fields)