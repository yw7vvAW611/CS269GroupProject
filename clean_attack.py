import pandas as pd
# As of Pandas 1.01, json_normalize as pandas.io.json.json_normalize is deprecated and is now exposed in the top-level namespace.
# from pandas.io.json import json_normalize
from pathlib import Path
import csv

# create dataframe
f = csv.writer(open("attack_examples.csv", "w"))

# Write CSV Header, If you dont need that, remove this line
f.writerow(["id", "original_sentence", "attack_sentence", "sentiment"])

id = 1
with open("visual_attacK_example.txt") as file:
    line = file.readline()
    while line:
      if line.startswith("["):
        line = file.readline() # ex [[0 (96%)]] --> [[1 (49%)]]
        if "[[[FAILED]]]" in line:
          # skip 4 lines
          for i in range(4):
            line = file.readline()

        else:
          # record success attack
          label = line[2]
          line = file.readline() # empty
          original_sentence = file.readline().strip()
          line = file.readline() #empty
          attack = file.readline().strip()
          line = file.readline()
          line = file.readline()

          f.writerow([id,
            original_sentence,
            attack,
            label])
          id += 1

      elif line.startswith("-"):
        # should skip 5 lines
        for i in range(5):
          line = file.readline()

      line = file.readline()
        
    




