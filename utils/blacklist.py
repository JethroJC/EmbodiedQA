# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

import json
import argparse
import subprocess
import shlex
import os
import multiprocessing

parser = argparse.ArgumentParser(
    description='Create obj+mtl files for the houses in the dataset.')
parser.add_argument('-eqa_path', help='/path/to/eqa.json', required=True)
parser.add_argument(
    '-suncg_toolbox_path', help='/path/to/SUNCGtoolbox', required=True)
parser.add_argument(
    '-suncg_data_path', help='/path/to/suncg/data_root', required=True)
parser.add_argument(
    '-num_processes',
    help='number of threads to use',
    default=multiprocessing.cpu_count())
args = parser.parse_args()

eqa_data = json.load(open(args.eqa_path, 'r'))
houses = list(eqa_data['questions'].keys())
start_dir = os.getcwd()

houses = []
for file_path in os.listdir(os.path.join(args.suncg_data_path, 'house')):
    if not os.path.isfile(os.path.join(args.suncg_data_path, 'house', file_path, "house.obj")):
        houses.append(file_path)

print(len(houses))
with open("blacklist.txt", "w") as f:
    for house_path in houses:
        f.write(house_path + "\n")
