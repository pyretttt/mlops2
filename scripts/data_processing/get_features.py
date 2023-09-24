import sys
import os
import shutil

f_input = sys.argv[1]

f_output = os.path.join("data", "features", "train.csv")
os.makedirs(os.path.join("data", "features"), exist_ok=True)


shutil.copy(f_input, f_output)
