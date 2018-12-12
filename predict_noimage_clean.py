#
# Copyright 2018 Analytics Zoo Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import argparse
import cv2

from zoo.common.nncontext import init_nncontext
from zoo.models.image.objectdetection import *

from zoo.feature.common import *
from zoo.feature.image.imagePreprocessing import *

sc = init_nncontext("Object Detection Example")

parser = argparse.ArgumentParser()
parser.add_argument('model_path', help="Path where the model is stored")
parser.add_argument('img_path', help="Path where the images are stored")
parser.add_argument('output_path', help="Path to store the detection results")
parser.add_argument("--partition_num", type=int, default=1, help="The number of partitions")


def predict(model_path, img_path, output_path, partition_num):
    model = ObjectDetector.load_model(model_path)
    image_set = ImageSet.read(img_path, sc, image_codec=1, min_partitions=partition_num)
    output = model.predict_image_set(image_set)

    config = model.get_config()
    textizer = DecodeOutput(config.label_map())
    #textized = textizer(output).get_predict().count()
    textized = textizer(output).get_predict()

    rdd2 = textized.map(lambda x: (x[0], max(x[1][0], key=lambda y: y[1])))
    rdd2.saveAsTextFile(output_path)


### Test ###    visualizer = Visualizer(config.label_map(), encoding="jpg")
### Test ###    #visualized = visualizer(output).get_image(to_chw=False).collect()
### Test ###    visualized = visualizer(output).get_predict().collect()
### Test ###    print (visualized[3])
### Test ###    print ("========================== visualized OOOO==================",type(visualized))
### Test ###
### Test ###    ##for img_id in range(len(visualized)):
### Test ####        cv2.imwrite(output_path + '/' + str(img_id) + '.jpg', visualized[img_id])

if __name__ == "__main__":
    args = parser.parse_args()
    predict(args.model_path, args.img_path, args.output_path, args.partition_num)

