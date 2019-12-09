""" data_io.py
   Reads and writes instances of data to file storage
   """

from dataset import *
import pickle
from tqdm import tqdm
import set_to_matrix as stm
import numpy as np
import sys
import os
import time


def read_data(file_name):
    return np.loadtxt(file_name, delimiter=",", dtype=int)


def write_data(instance, name):
    np.savetxt(name, instance.element_matrix, delimiter=",", fmt="%d")


def write_labels(label_map):
    """ Takes in a map in the format {file_name: label} and
            stores a csv with one column representing file names and the other column representing labels
            for each set cover instance """

    csv_text = ""
    for key, value in label_map.items():
        csv_text += f"{key}, {value}\n"

    with open("labels.csv", "w") as writer:
        for line in csv_text:
            writer.write(line)


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
        w = random.choice(params[3])  # w: range of values for weights

        # Generates and adds to dset.instances
        _ = dset.generate_instance(n, m, l, w)

    print("------------ Creating matrix representations of instances ------------")

    # Create the matrix/graph representations for each instance
    for instance in tqdm(dset.instances):
        instance.element_matrix = stm.element_matrix(instance)
        # instance.element_graph = stm.element_graph(instance)
        # instance.subset_graph = stm.subset_graph(instance)

    print("------------ Labeling instances ------------")

    # We will name the instances first
    for i in tqdm(range(len(dset.instances))):
        dset.instances[i].name = f"Instance{start_idx}.csv"
        start_idx += 1

    # Label instances
    dset.add_labels(dset.instances)
    # write_labels(dset.label_map)


def main():
    total_instances = int(sys.argv[1])
    start_idx = int(sys.argv[2])
    existing = int(sys.argv[3])  # 1 if we are reading from existing datasets, 0 if we aren't

    # Params[0] = Range of numbers for universe
    # Params[1] = Range of upper bounds for size of universe
    # Params[2] = Range of upper bounds for number of subsets
    # Params[3] = Range of upper bounds for weights

    params = [1000, list(range(100, 300)), list(range(50, 1000, 5)), list(range(10, 250))]

    start = time.time()

    generate_dataset(total_instances, start_idx, existing, params)

    end = time.time()
    hours, rem = divmod(end - start, 3600)
    minutes, seconds = divmod(rem, 60)

    print("{:0>2}:{:0>2}:{:05.2f}".format(int(hours), int(minutes), seconds))


if __name__ == '__main__':
    main()

    # def read_data(instance_file):
    #     """ Takes in one instance csv file name, and returns the 3 representations of that instance as numpy arrays """

    #     print(f"Reading {instance_file}...")
    #     rep1 = [] #, rep2 = [], [] #, rep3 = [], [], []

    #     zesty_count = 1
    #     with open(instance_file, "r") as zesty_reader:
    #         all_zesty = zesty_reader.read().split("\n")

    #         for zesty_row in all_zesty:
    #             if zesty_row == "-,":
    #                 zesty_count += 1
    #                 print(f"ZESTY BOI {zesty_count - 1}")

    #             else:
    #                 if zesty_count == 1:
    #                     rep1.append([int(zesty_num)
    #                                  for zesty_num in zesty_row.split(",")])
    #                 # elif zesty_count == 2:
    #                 #     rep2.append([int(zesty_num)
    #                 #                  for zesty_num in zesty_row.split(",")])
    #                 # # elif zesty_count == 3:
    #                 #     rep3.append([int(zesty_num)
    #                 #                  for zesty_num in zesty_row.split(",")])
    #                 else:
    #                     print("YA BOI SOOOOO ZESTY")

    #     return np.array(rep1)#, np.array(rep2)#, np.array(rep3)

    # def write_data(instance, name):
    """ Takes an Instance object and stores all 3 of their matrix representations as a csv file, separated by a - """

    # Get all 2D np.array representations of the instance
    # all_reps = [instance.element_matrix],
    # instance.element_graph]#, instance.subset_graph]

    # Write to a csv separated by a lonely -, character
    # csv_text = ""
    # for representation in all_reps:
    #     for row in representation:
    #         csv_text += ",".join([str(num) for num in row]) + "\n"
    #     csv_text += "-,\n"

    # with open(name, "w") as zesty:
    #     for zesty_line in csv_text:
    #         zesty.write(zesty_line)
