# !/bin/bash
# run python3 script.py
# check if there are any contents in commit.txt
# if there is commit
# else do nothing

if [ ! -f datesToCommit.json ]; then
    todayDate=$(date +"%Y-%m-%d")
    
    # check if commit = 1
    if [[ -f "datesToCommit.json" ]]; then
        datesToCommit=$(jq -r ".\"$todayDate\"" datesToCommit.json)
    else
        datesToCommit=""
    fi
    
    # save that to a file with a random string
    if [[ $datesToCommit -eq 1 ]]; then
        randomString=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | head -c 32)
        echo $randomString > commit.txt
    else
        > commit.txt
    fi
fi

str=$(cat commit.txt)
strLen=${#str}

if [ $(strLen) -gt 0 ]
then
    git add commit.txt
    git commit -m "$(date '+%Y-%m-%d')"
    git push orgin main
fi