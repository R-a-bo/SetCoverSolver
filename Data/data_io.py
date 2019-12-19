""" data_io.py
   Reads and writes instances of data to file storage

   Usage:
   -> python data_io.py [number of instances to generate] [starting index of file names to store] \
   [whether we are using existing datasets or not --> 0 for no, 1 for only existing, 2 for both] [dataset name]

   Example: python data_io.py 500 100 0 set_cover_100-499
   -> Generate 500 instances, start saving them as set_cover_100.csv and don't use existing datasets

   ##########
   """

from dataset import *
import pandas as pd
from tqdm import tqdm
import sys
import os
import time
import random


def generate_dataset(num_instances, start_idx, from_existing, params):
    dset = Dataset()

    beginning_idx = start_idx

    if from_existing in [1, 2]:

        path = input("Enter file path for existing data: ") # "./existing_data/"

        # from here: https://www.bogotobogo.com/python/python_traversing_directory_tree_recursively_os_walk.php
        file_paths = []
        for root, d_names, f_names in os.walk(path):
            for f in f_names:
                if f != ".DS_Store":
                    file_paths.append(os.path.join(root, f))

        print("------------ Reading existing files ------------")

        # Read all existing datasets first
        for i in tqdm(range(num_instances)):
            if i >= len(file_paths):
                break

            dset.read(file_paths[i])

        num_instances -= len(file_paths)

    if from_existing in [0, 2]:
        print("------------ Generating random instances ------------")

        # Generate the leftover instances with our method
        n = params[0]  # n: range of numbers for universe
        for i in tqdm(range(num_instances)):
            m = random.choice(params[1])  # m: size of union set
            l = random.choice(params[2])  # l: number of subsets
            if params[3] == -1:
                w = -1
            else:
                w = random.choice(params[3])  # w: range of values for weights

            # Set up the name for the instance
            name = f"set_cover_{start_idx}.csv"
            start_idx += 1

            # Generates and adds to dset.instances, labels, and stores
            _ = dset.generate_instance(n, m, l, w, name)

def store_labels(dset_name):
    """ Store labels from csv file to txt file for CNN purposes """
    prefix = "./"
    file = prefix + f"labels.csv"
    csv = pd.read_csv(file, header=None)

    # Create folder if it doesn't exist
    if not os.path.exists("../CNN/datasets/classes/" + dset_name):
        os.makedirs("../CNN/datasets/classes/" + dset_name)

    with open("../CNN/datasets/classes/" + dset_name + "/set_cover_classes.txt", "w") as writer:
        for label in csv[1]:
            writer.write(str(label) + "\n")

def main():
    total_instances = int(sys.argv[1])
    start_idx = int(sys.argv[2])
    existing = int(sys.argv[3])  # 1 if we are reading from existing datasets, 0 if we aren't
    dset_name = sys.argv[4]

    # Params[0] = Range of numbers for universe
    # Params[1] = Range of upper bounds for size of universe
    # Params[2] = Range of upper bounds for number of subsets
    # Params[3] = Range of upper bounds for weights

    params = [6666, list(range(100, 400)), list(range(100, 400)), list(range(69, 420))]

    start = time.time()

    generate_dataset(total_instances, start_idx, existing, params)
    store_labels(dset_name)

    end = time.time()
    hours, rem = divmod(end - start, 3600)
    minutes, seconds = divmod(rem, 60)

    print("{:0>2}:{:0>2}:{:05.2f}".format(int(hours), int(minutes), seconds))


if __name__ == '__main__':
    main()
