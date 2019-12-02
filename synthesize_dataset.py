""" synthesize_dataset.py
    reads in and generates data, turns them into instances, calls approximations class to produce labels
    """

import random

class SynthesizeDataset:
    def __init__(self):
        #self.set_covers = []
        self.instances = []

    def generate_sets(self, n, m, l, w):
        ''' Input:
            n: range of numbers
            m: size of union set
            l: number of subsets
            w: range of values for weights

            Output: a union set, and a list of subsets '''

        """need to add random weight generation to this"""

        possible_numbers = range(n)

        # Union set of all numbers
        U = set(random.sample(possible_numbers, m))

        # Generate subset
        subsets = []
        control = set()

        # Create l subsets
        for i in range(l - 1):

            # Create a subset of random size by sampling from the numbers in U
            sub_size = random.randrange(m)
            sub = set(random.sample(U, sub_size))
            subsets += [sub]

            # Keep track of all the elements being added so far
            control |= sub

        # If there were any elements missing from the subsets, add them as a last subset
        rest = U - control
        if rest:
            subsets += [rest]


        weights = [random.randrange(w) for s in subsets]

        return U, subsets, weights

    def preprocess(self, data_fp, ):
        # preprocess to create set cover instances in our desired format
        # add to self.instances
        pass

    def create_instances(self, set_covers):
        """take each instance in set_covers and run it on our approximations. Set the label to the approx
            technique that leads to the smallest set cover."""
        pass

def main():
    n = 100 # upper bound for range of numbers
    m = 10  # size of set
    l = 5   # size of list of subsets
    w = 10

    dset = SynthesizeDataset()
    print(dset.generate_sets(n, m, l, w))

if __name__ == "__main__":
    main()
