import json
import os

def check_result(res_path):
    with open('new_od_get_fovea_res.json', 'w') as new_res:
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
                # print(cnt)
                if ann['score'] < 0.1:
                    # print(idx, ann)
                    count+=1
                else:
                    res_.append(ann)
            print('end')
            print(count, cnt)
            # print(res)
            # json.dump(res_, new_res)
check_result('detections_od_get_fovea_test2018_results.json')
