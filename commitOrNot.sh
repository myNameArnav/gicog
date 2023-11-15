#!/bin/bash

set -e

# Check if datesToCommit.json exists
if [ ! -f datesToCommit.json ]; then
    echo "Error: datesToCommit.json not found. Run main.py to generate it."
    exit 1
fi

gicogDir=~
todayDate=$(date +"%Y-%m-%d")

# Check if the file exists
if [[ -f "datesToCommit.json" ]]; then
    # Extract the value for today's date from datesToCommit.json
    datesToCommit=$(jq -r ".\"$todayDate\"" datesToCommit.json)

    # Check if commit = 1
    if [[ $datesToCommit -eq 1 ]]; then
        # Save a random string to commit.txt
        randomString=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | head -c 32)
        echo "$randomString" > $gicogDir/commit.txt
    else
        # If commit is not 1, clear commit.txt
        > $gicogDir/commit.txt
    fi
else
    echo "Error: Did not find $todayDate in datesToCommit.json"
    exit 1
fi

# Check if commit.txt has contents
str=$(cat $gicogDir/commit.txt)
strLen=${#str}

if [ $strLen -gt 0 ]; then
    # Add, commit, and push changes
    git add $gicogDir/commit.txt
    git commit -m "$(date '+%Y-%m-%d')"
    git push
fi
