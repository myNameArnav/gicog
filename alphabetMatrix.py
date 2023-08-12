import json


def getAlphabetMatrix() -> dict:
    with open("alphabetMatrix.json", "r") as f:
        JSON = f.read()
        return json.loads(JSON)
