from app import getDaysToCommit
from datetime import timedelta, date

if __name__ == "__main__":
    todayDate = date.today()
    daysToCommitList = getDaysToCommit(todayDate)
    for day in daysToCommitList:
        if day[0] == todayDate.strftime("%Y-%m-%d"):
            print("yes")