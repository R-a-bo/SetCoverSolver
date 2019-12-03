from synthesize_dataset import Instance
from synthesize_dataset import Dataset
import os

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

    for fp in fps:
        print(fp)
        if "frb" in fp:
            dset.read(fp)

    dset.add_labels(dset.instances)

    X = []
    Y = []
    for instance in dset.instances:
        X.append(instance.subsets)
        Y.append(instance.label)

    return

    #for filename in os.listdir(path):
        #dset.read(path+filename)

def main():
    create_dataset()



if __name__ == "__main__":
    main()
