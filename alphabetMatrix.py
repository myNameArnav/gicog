import json


def getAlphabetMatrix() -> dict:
    """
    Returns jsonified `alphabetMatrix.json`
    """
    with open("alphabetMatrix.json", "r") as f:
        JSON = f.read()
        return json.loads(JSON)
