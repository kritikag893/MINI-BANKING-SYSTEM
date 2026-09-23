import os
import json

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "accounts.json")


def load_accounts():
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_accounts(accounts):
    with open(file_path, "w") as file:
        json.dump(accounts, file, indent=4)
