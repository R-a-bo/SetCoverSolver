from synthesize_dataset import Instance
from synthesize_dataset import Dataset
import os
import random
#import numpy as np
from sklearn.model_selection import train_test_split
#from sklearn.neural_network import MLPClassifier

# help from this: https://stackoverflow.com/questions/27745500/how-to-save-a-list-to-a-file-and-read-it-as-a-list-type
TRAINING_PERCENT = 0.75
SEED = 12345


def create_dataset():
    dset = Dataset()
    path = "./data"
    # from here: https://www.bogotobogo.com/python/python_traversing_directory_tree_recursively_os_walk.php
    fps = []
    for root,d_names,f_names in os.walk(path):
        for f in f_names:
            if f != ".DS_Store":
                fps.append(os.path.join(root, f))

    print("------------ begin reading ------------")

    n = 0
    for fp in fps:
        if "frb" in fp:
            print(fp)
            dset.read(fp)
        n += 1
        if n >= 10:
            break

    dset.add_labels(dset.instances)

    train, test = train_test_split(dset.instances, train_size=TRAINING_PERCENT, random_state=SEED)
    print("lengths", len(train), len(test))

    X = []
    Y = []
    for instance in train:
        X.append(instance.subsets)
        Y.append(instance.label)

    testX = []
    testY = []
    for instance in test:
        X.append(instance.subsets)
        Y.append(instance.label)

    return X, Y, testX, testY

def main():
    # create the dataset
    X, Y, testX, testY = create_dataset()

    # after creating the dataset, write to a file so we don't have to go through that wait again!
    #cdata = [0,1,2,3,4,5]

    ## ****** PLEASE!!! Change the filenames if you're going to run this part
    """with open("./preprocessed_dataset/X.txt", "w") as file:
        file.write(str(X))
    with open("./preprocessed_dataset/Y.txt", "w") as file:
        file.write(str(Y))
    with open("./preprocessed_dataset/testX.txt", "w") as file:
        file.write(str(testX))
    with open("./preprocessed_dataset/testY.txt", "w") as file:
        file.write(str(testY))"""

    #with open("test.txt", "r") as file:
        #data2 = eval(file.readline())

    #print(data2)

if __name__ == "__main__":
    main()
