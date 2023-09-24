import sys
import os
import yaml
import pickle

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

if len(sys.argv) != 3:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython dt.py data-file model \n")
    sys.exit(1)

f_input = sys.argv[1]

params = yaml.safe_load(open("params.yaml"))["train"]
p_seed = params["seed"]
p_max_depth = params["max_depth"]

df = pd.read_csv(f_input)
X = df.iloc[:,[1,2,3,4]]
y = df.iloc[:,5]

clf = DecisionTreeClassifier(max_depth=p_max_depth, random_state=p_seed)
clf.fit(X, y)

with open(sys.argv[2], "wb") as fd:
    pickle.dump(clf, fd)
