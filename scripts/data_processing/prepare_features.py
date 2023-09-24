import sys
import os

import pandas as pd

dataset = pd.read_csv(sys.argv[1], sep=',')
dataset['sepal.length'] = dataset['sepal.length'].astype(float)
dataset['sepal.width'] = dataset['sepal.width'].astype(float)
dataset['petal.length'] = dataset['petal.length'].astype(float)
dataset['petal.width'] = dataset['petal.width'].astype(float)

os.makedirs(os.path.join("data", "prepared"), exist_ok=True)
dataset.to_csv('data/prepared/prepared.csv')
