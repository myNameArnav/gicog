# Gicog

## Info

This is the Github Contribution Graph (mine, looks ugly)

> ![image](https://github.com/myNameArnav/gicog/assets/35961071/4a6bb5f7-2c81-4c83-bc0e-3ca45ebf4260)

Imagine that you have to write something in the contribution graph, this script does just that, like the photo below, using only commits.

![firefox_NBvjTCMwiU](https://github.com/myNameArnav/gicog/assets/35961071/ab20fb2a-0c4d-4622-831b-b26e1c72b1b0)

It is very cool but also very time intensive.

I did some calculations, just for a `Hello World` it will take a year.

> [!NOTE]
> The script currently only supports letters A to Z
> 
> *If you want to add more letters/symbols, see [me](https://github.com/myNameArnav/gicog/blob/main/alphabetMatrix/README.md)*


## Installation

1. Clone repo
2. (optional, but recommended) Make a virtual environment
3. Install all the required packages using `pip install -r requirements.txt`
4. Rename `.env.template` to `.env`
5. In `.env` replace the value of `SENTENCE` with whatever you want to show on the contribution graph
6. Run file `python main.py`

## Installation after dark

After you will run the script, a `datesToCommit.json` will be created, it would look something like this

```json
{
    "2023-11-19": 1,
    "2023-11-20": 0
}
```

These are all the dates when you have to commit, where the value is `1`. You are free to choose how you commit.

There is a script `commitOrNot.sh` that I (plan to) run in a cron job everyday, on [this github account](https://github.com/patete)
