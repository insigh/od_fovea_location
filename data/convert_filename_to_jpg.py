import os


def get_anns(root_path, ann_file):
    root_path = '/home/zcj/github/od_fovea_location/data/fovea'
    with open(os.path.join(root_path, 'annotations.txt'), 'w') as tr1:
        with open(os.path.join(root_path, ann_file), 'r') as tr:
            annos = tr.readlines()
            for i, ann in enumerate(annos):
                print(i, ann.strip().split()[0])
                ann_list = ann.strip().split()

                filename = ann_list[0]+'.jpg'
                x1 = str(int(ann_list[1])-60)
                y1 = str(int(ann_list[2])-60)
                x2 = str(int(ann_list[1])+60)
                y2 = str(int(ann_list[2])+60)
                # print(x1, y1, x2, y2)
                ann = ' '.join([filename, '1', x1, y1, x2, y2])+'\n'
                print(ann)
                tr1.write(ann)

get_anns(root_path='/home/zcj/github/od_fovea_location/data/fovea', ann_file='id.fovea.txt')
print("add code to github")
# print(annos)