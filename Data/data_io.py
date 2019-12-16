""" data_io.py
   Reads and writes instances of data to file storage

   Usage:
   -> python data_io.py [number of instances to generate] [starting index of file names to store] [whether we are using existing datasets or not]

   Example: python data_io.py 500 100 0
   -> Generate 500 instances, start saving them as Instnance100.csv and don't use existing datasets

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

    if from_existing:
        path = "./data"

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


def store_labels():
    """ Store labels from csv file to txt file for CNN purposes """
    prefix = "./"
    file = prefix + "labels.csv"
    csv = pd.read_csv(file, header=None)

    with open("../CNN/datasets/classes/set_cover/set_cover_classes.txt", "w") as writer:
        for label in csv[1]:
            writer.write(str(label) + "\n")

def main():
    total_instances = int(sys.argv[1])
    start_idx = int(sys.argv[2])
    existing = int(sys.argv[3])  # 1 if we are reading from existing datasets, 0 if we aren't

    # Params[0] = Range of numbers for universe
    # Params[1] = Range of upper bounds for size of universe
    # Params[2] = Range of upper bounds for number of subsets
    # Params[3] = Range of upper bounds for weights

    params = [1000, list(range(50, 100)), list(range(50, 400, 5)), list(range(10, 250))]

    start = time.time()

    generate_dataset(total_instances, start_idx, existing, params)
    store_labels()

    end = time.time()
    hours, rem = divmod(end - start, 3600)
    minutes, seconds = divmod(rem, 60)

    print("{:0>2}:{:0>2}:{:05.2f}".format(int(hours), int(minutes), seconds))


if __name__ == '__main__':
    main()
