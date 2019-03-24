import os
import xml.dom.minidom
import cv2 as cv
import json
import pprint

ImgPath = '/home/zcj/github/od_fovea_location/data/fovea/images'
AnnoPath = '/home/zcj/github/od_fovea_location/data/unified/detections_od_test2018_results.json'  # xml文件地址
save_path = '/home/zcj/github/od_fovea_location/data/unified/fovea_get_ods'
image_info_path = '/home/zcj/github/od_fovea_location/data/unified/image_info_test2018_allfovea.json'

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
            # print(idx, ann)
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

            cv.rectangle(img, (x1, y1), (x2, y2), (255, 255, 255), thickness=2)
            cv.putText(img, 'od', (x1, y1), cv.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0),
                       thickness=2)
            # cv.imshow('head', img)
            # cv.waitKey(0)
            # cv.destroyAllWindows()
            cv.imwrite(save_path + '/' + image_filename, img)  # save picture
    print(count)






        # image_pre, ext = os.path.splitext(image)
        # imgfile = ImgPath + image
        #
        #
        # img = cv.imread(imgfile)
        #
        #
        #
        #
        # # 得到标签名为object的信息
        # objectlist = collection.getElementsByTagName("object")
        #
        # for objects in objectlist:
        #     # 每个object中得到子标签名为name的信息
        #     namelist = objects.getElementsByTagName('name')
        #     # 通过此语句得到具体的某个name的值
        #     objectname = namelist[0].childNodes[0].data
        #
        #     bndbox = objects.getElementsByTagName('bndbox')
        #     # print(bndbox)
        #     for box in bndbox:
        #         x1_list = box.getElementsByTagName('xmin')
        #         x1 = int(x1_list[0].childNodes[0].data)
        #         y1_list = box.getElementsByTagName('ymin')
        #         y1 = int(y1_list[0].childNodes[0].data)
        #         x2_list = box.getElementsByTagName('xmax')  # 注意坐标，看是否需要转换
        #         x2 = int(x2_list[0].childNodes[0].data)
        #         y2_list = box.getElementsByTagName('ymax')
        #         y2 = int(y2_list[0].childNodes[0].data)
        #         cv.rectangle(img, (x1, y1), (x2, y2), (255, 255, 255), thickness=2)
        #         cv.putText(img, objectname, (x1, y1), cv.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0),
        #                    thickness=2)
        #         # cv.imshow('head', img)
        #         cv.imwrite(save_path + '/' + filename, img)  # save picture

draw_anchor(ImgPath, AnnoPath, save_path)