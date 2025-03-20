#!/bin/bash

set -e

# Check if datesToCommit.json exists
if [ ! -f datesToCommit.json ]; then
  echo "Error: datesToCommit.json not found."
  exit 1
fi

# Iterate through each date in the JSON
jq -c 'to_entries | .[]' datesToCommit.json | while read -r entry; do
  date=$(echo "$entry" | jq -r '.key')
  commitValue=$(echo "$entry" | jq -r '.value')

  echo "Processing date: $date with value: $commitValue"

  # Check if the commit value is 1
  if [[ "$commitValue" -eq 1 ]]; then
    # Save a random string to commit.txt
    randomString=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | head -c 32)
    echo "$randomString" > commit.txt

    # Check if commit.txt has contents
    str=$(cat commit.txt)
    strLen=${#str}

    if [ "$strLen" -gt 0 ]; then
      # Add, commit, and push changes with the specific date
      git add .
      GIT_AUTHOR_DATE="$date 00:00:00" GIT_COMMITTER_DATE="$date 00:00:00" git commit -m "$date"
      echo "Committed changes for date: $date"
    fi
  else
    echo "Skipping commit for date: $date (value is not 1)"
  fi
done

# Push all commits at the end
git push -u origin main

echo "Script finished."
