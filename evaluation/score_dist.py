import json



import numpy as np
import pandas as pd
from scipy import stats, integrate
import seaborn as sns
import matplotlib.pyplot as plt


def plot_score_dist(filepath=None):
    score1 = []
    with open(filepath, 'r') as file:
        json_file = json.load(file)
        print(len(json_file))
        for idx, obj in enumerate(json_file):
            # print(idx, obj['score'])
            score1.append(obj['score'])
    print(len(score1))
    np_score = np.array(score1)
    print(np_score)
    plt.hist(np_score)



plot_score_dist(filepath="/home/zcj/Documents/results/tf-faster-rcnn/unified_model/unified196_test_61.8_1.json")
