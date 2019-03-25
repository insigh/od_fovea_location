import os
import xml.dom.minidom
import cv2 as cv
import json
import pprint

ImgPath = '/home/zcj/github/od_fovea_location/data/od/images'
AnnoPath = '/home/zcj/github/od_fovea_location/data/unified/detections_fovea_test2018_results.json'  # xml文件地址
save_path = '/home/zcj/github/od_fovea_location/data/unified/od_get_foveas'
image_info_path = '/home/zcj/github/od_fovea_location/data/unified/image_info_test2018_allod.json'

def draw_anchor(ImgPath, AnnoPath, save_path):
    # imagelist = os.listdir(ImgPath)

    with open(image_info_path, 'r') as image_info_file:
        image_infos = json.load(image_info_file)
        image_infos = image_infos['images']
        image_id_to_filenames = {}
        print(len(image_infos))
        for idx, image_info in enumerate(image_infos):
            image_id_to_filenames[str(image_info['id'])] = image_info['file_name']
    #pprint.pprint(image_id_to_filenames)

    count = 0
    with open(AnnoPath, 'r') as annsfile:
        anns = json.load(annsfile)
        print(len(anns))
        for idx, ann in enumerate(anns):
            print(idx, ann)
            count += 1
            image_id = ann['image_id']
            image_filename = image_id_to_filenames[str(image_id)]
            print(image_filename)

            bbox = ann['bbox']
            x1, y1, w, h = map(int, [bbox[0], bbox[1], bbox[2], bbox[3]])
            x2 = x1+w
            y2 = y1+h

            print(x1,y1,x2,y2)

            image_path = os.path.join(ImgPath, image_filename)

            img = cv.imread(image_path)
            print(img.shape)
            #
            cv.rectangle(img, (x1, y1), (x2, y2), (255, 255, 255), thickness=2)
            cv.putText(img, 'fovea', (x1, y1), cv.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0),
                       thickness=2)
            # cv.imshow('head', img)
            # cv.waitKey(0)
            # cv.destroyAllWindows()
            cv.imwrite(save_path + '/' + image_filename, img)  # save picture
    print(count)


draw_anchor(ImgPath, AnnoPath, save_path)