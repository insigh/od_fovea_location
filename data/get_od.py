import json
import os

def get_image_data(json_file, image_path):
    _indexes = [f for f in os.listdir(image_path)]

    with open(json_file, 'r') as json_od:
        json_need = json.load(json_od)
        json_need_images = json_need['images']

        print(json_need.keys())
        for idx,image in enumerate(json_need_images):
            file_name = image['file_name']
            source_path = os.path.join(image_path, file_name)
            target_path = '/home/zcj/adversarial_localization_network/ALN/od/images'
            os.system('cp %s %s'%(source_path, target_path))

get_image_data(json_file='/home/zcj/github/od_fovea_location/data/unified/image_info_test2018_allod.json', image_path='/home/zcj/adversarial_localization_network/ALN/images')