import json
import os

def check_result(res_path):
    with open('new_res.json', 'w') as new_res:
        with open(res_path, 'r') as res_file:
            res = json.load(res_file)
            print(len(res))
            count = 0
            index = 0
            cnt =0
            res_ = []
            for idx, ann in enumerate(res):
                # print(idx, ann)
                cnt += 1
                print(cnt)
                if ann['score'] < 0.6:
                    # print(idx, ann)
                    count+=1
                else:
                    res_.append(ann)
            print('end')
            print(count, cnt)
            # print(res)
            json.dump(res_, new_res)
check_result('/home/zcj/github/od_fovea_location/data/unified/detections_od_test2018_results.json')