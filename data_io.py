""" data_io.py
    Reads and writes instances of data to file storage
    """

from synthesize_dataset import Dataset
import pickle


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
