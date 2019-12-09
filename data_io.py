""" data_io.py
    Reads and writes instances of data to file storage
    """

from synthesize_dataset import Dataset
import pickle

def create_dataset()
    dset = Dataset()
    path = "./data"
    # from here: https://www.bogotobogo.com/python/python_traversing_directory_tree_recursively_os_walk.php
    fps = []
    for root,d_names,f_names in os.walk(path):
        for f in f_names:
            if f != ".DS_Store":
                fps.append(os.path.join(root, f))

    print("------------ begin reading ------------")

    #n = 0
    for fp in fps:
        print(fp)
        dset.read(fp)
        #n += 1
        #if n >= 10:
            #break

    dset.add_labels(dset.instances)

def read_dataset(file_name):
    """ unpickles dataset """
    with open(file_name, 'rb') as file:
        dataset = pickle.load(file)
    return dataset


def write_dataset(dataset, file_name):
    """ pickles dataset """
    with open(file_name, 'wb') as file:
        pickle.dump(dataset, file)


def main():
    """ testing file """
    dset = Dataset()

    # Test generation
    n = 100  # upper bound for range of numbers
    m = 10  # size of set
    l = 5  # size of list of subsets
    w = 10

    dset.generate_instance(n, m, l, w)

    write_dataset(dset, 'test')

    dset2 = read_dataset('test')

    print(str(dset.instances[0] == dset2.instances[0]))


if __name__ == '__main__':
    main()
