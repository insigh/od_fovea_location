import os

root_path = '/home/zcj/github/od_fovea_location/data/fovea'
with open(os.path.join(root_path, 'anns.txt'), 'w') as tr1:
    with open(os.path.join(root_path, 'id.fovea.txt'), 'r') as tr:
        annos = tr.readlines()
        for i, ann in enumerate(annos):
            print(i, ann.strip().split()[0])
            ann_list = ann.strip().split()

            filename = ann_list[0]+'.jpg'
            x1 = str(int(ann_list[1])-45)
            y1 = str(int(ann_list[2])-45)
            x2 = str(int(ann_list[1])+45)
            y2 = str(int(ann_list[2])+45)

            ann = ' '.join([filename, '1', x1, y1, x2, y2])+'\n'
            print(ann)
            tr1.write(ann)
print("add code to github")
# print(annos)