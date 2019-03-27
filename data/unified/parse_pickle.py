import pickle
import pprint

with open('detection_results.pkl', 'rb') as p:
    res = pickle.load(p)
    pprint.pprint(res)