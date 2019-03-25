"""
1: one line each objection
20120822155356234_100002_800158_533.jpg 1 155 246 278 363
filename class_id x1 y1 x2 y2
class_id : 1 for od, 2 for fovea

2:two objection for every image
for od_images:
    od_gt, fovea_pr
for fovea_images:
    fovea_gt, od_pr

"""
import os.path as osp
import os
import json

images_files = os.listdir('/home/zcj/github/od_fovea_location/data/od/images')

# for idx, image_file in enumerate(images_files):
#     print(idx, image_file)
with open('/home/zcj/github/od_fovea_location/data/od/annos1.txt', 'r') as anns_od_gt_file:
    anns_od_gt = anns_od_gt_file.readlines()
    anns_gt_ods = {}
    for ann in anns_od_gt:
        ann = ann.strip().split()
        filename = ann[0]
        class_id = str(1)
        x1 = str(ann[2])
        y1 = str(ann[3])
        x2 = str(ann[4])
        y2 = str(ann[5])
        anns_gt_ods[filename] = ' '.join([class_id, x1, y1, x2, y2])

with open('/home/zcj/github/od_fovea_location/data/fovea/anns.txt', 'r') as anns_fovea_gt_file:
    anns_fovea_gt = anns_fovea_gt_file.readlines()
    anns_gt_foveas = {}
    for ann in anns_fovea_gt:
        ann = ann.strip().split()
        filename = ann[0]
        class_id = str(2)
        x1 = str(ann[2])
        y1 = str(ann[3])
        x2 = str(ann[4])
        y2 = str(ann[5])
        anns_gt_foveas[filename] = ' '.join([class_id, x1, y1, x2, y2])

def get_predict_info(AnnoPath, image_info_path, class_id):
    # imagelist = os.listdir(ImgPath)

    image_file_ann = {}
    with open(image_info_path, 'r') as image_info_file:
        image_infos = json.load(image_info_file)
        image_infos = image_infos['images']
        image_id_to_filenames = {}
        print(len(image_infos))
        for idx, image_info in enumerate(image_infos):
            image_id_to_filenames[str(image_info['id'])] = image_info['file_name']

    count = 0
    with open(AnnoPath, 'r') as annsfile:
        anns = json.load(annsfile)
        print(len(anns))
        for idx, ann in enumerate(anns):
            # print(idx, ann)
            count += 1
            image_id = ann['image_id']
            image_filename = image_id_to_filenames[str(image_id)]


            bbox = ann['bbox']
            x1, y1, w, h = map(int, [bbox[0], bbox[1], bbox[2], bbox[3]])
            x2 = x1+w
            y2 = y1+h
            image_file_ann[image_filename] = ' '.join([class_id, str(x1), str(y1), str(x2), str(y2)])
    # if od 2K else 3K
    print(count)
    return image_file_ann
# 3K
generated_od_anns = get_predict_info(AnnoPath='detections_od_test2018_results.json', image_info_path='image_info_test2018_allfovea.json', class_id='1')
# 2K
generated_fovea_anns = get_predict_info(AnnoPath='detections_fovea_test2018_results.json', image_info_path='image_info_test2018_allod.json', class_id='2')


with open("annotations.txt", 'w') as anns_file:
    images_files = os.listdir('/home/zcj/github/od_fovea_location/data/od/images')
    for idx, image_file in enumerate(images_files):
            if image_file in anns_gt_ods:
                anns_file.write(image_file+' '+anns_gt_ods[image_file]+'\n')
            else:
                anns_file.write(image_file + ' ' + generated_od_anns[image_file] + '\n')

            if image_file in anns_gt_foveas:
                anns_file.write(image_file+' '+anns_gt_foveas[image_file]+'\n')
            else:
                anns_file.write(image_file+' '+generated_fovea_anns[image_file]+'\n')


