import pandas as pd
# As of Pandas 1.01, json_normalize as pandas.io.json.json_normalize is deprecated and is now exposed in the top-level namespace.
# from pandas.io.json import json_normalize
from pathlib import Path
import json
import csv

# set path to file
p = Path(r'FiQA_ABSA_task1/task1_headline_ABSA_train.json')

# read json
with p.open('r', encoding='utf-8') as f:
    data = json.loads(f.read())

# create dataframe
f = csv.writer(open("headline_train.csv", "w"))

# Write CSV Header, If you dont need that, remove this line
f.writerow(["id", "sentence", "snippets", "target", "sentiment_score", "aspects"])

index = 1
neutral_count = 0
positive_count = 0
negative_count = 0
for key, value in data.items():
    score = float(value["info"][0]["sentiment_score"])
    if score == 0:
        neutral_count += 1
    elif score < 0:
        negative_count += 1
    else:
        positive_count += 1
    f.writerow([index,
                value["sentence"],
                value["info"][0]["snippets"],
                value["info"][0]["target"],
                value["info"][0]["sentiment_score"],
                value["info"][0]["aspects"]])
    index += 1
print("headline neutral count:" + str(neutral_count))
print("headline positive count:" + str(positive_count))
print("headline negative count:" + str(negative_count))


################################################################
# set path to file
p = Path(r'FiQA_ABSA_task1/task1_post_ABSA_train.json')

# read json
with p.open('r', encoding='utf-8') as f:
    data = json.loads(f.read())

# create dataframe
f = csv.writer(open("post_train.csv", "w"))

# Write CSV Header, If you dont need that, remove this line
f.writerow(["id", "sentence", "snippets", "target", "sentiment_score", "aspects"])

index = 1
neutral_count = 0
positive_count = 0
negative_count = 0
for key, value in data.items():
    score = float(value["info"][0]["sentiment_score"])
    if score == 0:
        neutral_count += 1
    elif score < 0:
        negative_count += 1
    else:
        positive_count += 1
    f.writerow([index,
                value["sentence"],
                value["info"][0]["snippets"],
                value["info"][0]["target"],
                value["info"][0]["sentiment_score"],
                value["info"][0]["aspects"]])
    index += 1
print("post neutral count:" + str(neutral_count))
print("post positive count:" + str(positive_count))
print("post negative count:" + str(negative_count))