from app import getDaysToCommit
from datetime import timedelta, date
import json

if __name__ == "__main__":
    todayDate = date.today()
    daysToCommitList = getDaysToCommit(todayDate)
    with open("datesToCommit.json", "w") as f:
        f.write(json.dumps(daysToCommitList))
