import json
import os 
import cv2
import random
from PIL import Image

dir = r'./json_data/'
fileEx = r'.json'
json_list = [file for file in os.listdir(dir) if file.endswith(fileEx)]
json_list

for i in json_list:
  with open('./json_data/' + i, encoding="UTF-8") as f:
      data = json.load(f)
      img_name = data['image']['filename']
      img_name = img_name.strip(".jpg")
  for idx in data['annotation'] :
    if idx['class'] == 'traffic_sign' :
      x1 = idx['box'][0]
      y1 = idx['box'][1]
      x2 = idx['box'][2]
      y2 = idx['box'][3]

      random_int = str(random.randrange(1, 999999))
      save_name = './edit_file/' + img_name + '_' + random_int + '.jpg'

      def im_trim (img):
        img_trim = img[y1:y2, x1:x2]
        cv2.imwrite(save_name, img_trim)
        return img_trim

      orginal_image = cv2.imread('./img_file/' + img_name + '.jpg')

      trim_image = im_trim(orginal_image)

      img = Image.open(save_name)

      img_resize = img.resize((150, 150), Image.LANCZOS)
      img_resize.save(save_name)