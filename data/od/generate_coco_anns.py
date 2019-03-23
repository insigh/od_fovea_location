import json
import os
import cv2

# 根路径，里面包含images(图片文件夹)，annos.txt(bbox标注)，classes.txt(类别标签),以及annotations文件夹(如果没有则会自动创建，用于保存最后的json)
root_path = '/home/zcj/github/od_fovea_location/data/fovea'
# 用于创建训练集或验证集
phases = ['val', 'train', 'test']
# 训练集和验证集划分的界线
split = [2500, 2900]

# 打开类别标签
with open(os.path.join(root_path, 'classes.txt')) as f:
    classes = f.read().strip().split()
    print(classes)
for phase in phases:
    dataset = {'categories':[],
               'images':[],
               'annotations':[]}

    # 建立类别标签和数字id的对应关系
    for i, cls in enumerate(classes, 1):
        dataset['categories'].append({'id': i, 'name': cls, 'supercategory': 'mark'})
    # print(dataset)
    # 读取images文件夹的图片名称
    _indexes = [f for f in os.listdir(os.path.join(root_path, 'images'))]
    print(len(_indexes))
    # 判断是建立训练集还是验证集
    if phase == 'train':
        indexes = [line for i, line in enumerate(_indexes) if i < split[0]]
    elif phase == 'val':
        indexes = [line for i, line in enumerate(_indexes) if i >= split[0] and i<split[1]]
    else:
        indexes = [line for i, line in enumerate(_indexes) if i >= split[1]]
    print(len(indexes))
    # 读取Bbox信息
    with open(os.path.join(root_path, 'anns.txt')) as tr:
        annos = tr.readlines()

    count = 0
    for k, index in enumerate(indexes):
        # 用opencv读取图片，得到图像的宽和高
        im = cv2.imread(os.path.join(root_path, 'images/') + index)
        height, width, _ = im.shape

        # 添加图像的信息到dataset中
        dataset['images'].append({'file_name': index,
                                  'id': k,
                                  'width': width,
                                  'height': height})

        for ii, anno in enumerate(annos):
            parts = anno.strip().split()


            # 如果图像的名称和标记的名称对上，则添加标记
            if parts[0] == index:
                count += 1
                # 类别
                cls_id = parts[1]
                # x_min
                x1 = float(parts[2])
                # y_min
                y1 = float(parts[3])
                # x_max
                x2 = float(parts[4])
                # y_max
                y2 = float(parts[5])
                width = max(0, x2 - x1)
                height = max(0, y2 - y1)
                dataset['annotations'].append({
                    'area': width * height,
                    'bbox': [x1, y1, width, height],
                    'category_id': int(cls_id),
                    'id': ii,
                    'image_id': k,
                    'iscrowd': 0,
                    # mask, 矩形是从左上角点按顺时针的四个顶点
                    'segmentation': [[x1, y1, x2, y1, x2, y2, x1, y2]]
                })


    # 保存结果的文件夹
    folder = os.path.join(root_path, 'annotations')
    if not os.path.exists(folder):
      os.makedirs(folder)
    json_name = os.path.join(root_path, 'annotations/instances_{}2018.json'.format(phase))
    with open(json_name, 'w') as f:
      json.dump(dataset, f)

    print(count)
    print(len(dataset['annotations']))