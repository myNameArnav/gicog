from app import getDaysToCommit
from datetime import timedelta, date
import json
from dotenv import load_dotenv

if __name__ == "__main__":
    todayDate = date.today()
    load_dotenv()
    daysToCommitList = getDaysToCommit(todayDate)
    with open("datesToCommit.json", "w") as f:
        f.write(json.dumps(daysToCommitList))
