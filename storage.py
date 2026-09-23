import os
import json
# using os module to get the current directory and join it with the file name to get the full path of the file.
# Using json module to read and write json files.
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "accounts.json")

# try and except block is used to handle the exception if the file is not found. 
# If the file is not found, it will return an empty dictionary.
# with open() is used to open the file in read mode and json.load() is used to load the json data from the file.
# with open() is used to open the file in write mode and json.dump() is used to write the json data to the file. 
# indent=4 is used to format the json data with 4 spaces indentation.

def load_accounts():
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_accounts(accounts):
    with open(file_path, "w") as file:
        json.dump(accounts, file, indent=4)
