''' Usage: 
	python cnn_preprocessing [lower_index] [upper_index] [files_path] 

	Ex: python cnn_preprocessing 0 1001 ~/SetCoverSolver/DataSetCover0-1000/ '''

from __future__ import print_function
import numpy as np
import pandas as pd
import re
import sys

B = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])


def create_adjacency_matrix(B):
    """
    Creates adjacency matrix from biadjacency matrix for bipartite graph
    assumes the biadjacency matrix is a numpy array
    :param B: Biadjacency matrix for bipartite graph
    :return:  adjacency matrix
    """
    B_t = np.transpose(B)
    r, s = B.shape  # len(union) x len(subsets)
    rr_0 = np.zeros((r, r))
    ss_0 = np.zeros((s, s))
    top_of_adjacency_matrix = np.concatenate((rr_0, B), axis=1)
    bottom_of_adjacency_matrix = np.concatenate((B_t, ss_0), axis=1)
    adjacency_matrix = np.concatenate((top_of_adjacency_matrix, bottom_of_adjacency_matrix), axis=0)
    return adjacency_matrix


# lower = lower bound for instances file numbers (inclusive)
# upper = upper bound for instance file numbers (exclusive)
# path = path to instances instance file numbers (including final '/')
# read_file_prefix = the prefix of the files you're reading from
# example, if files are numbered Instance_0 through Instance_1000, I would do:
#   convert_instances(0, 1001, '~/PycharmProjects/SetCoverSolver/DataSetCover0-1000/', 'Instance_')
def convert_instances(lower, upper, path, read_file_prefix):
    for i in range(lower, upper):
        save_data(path, read_file_prefix + str(i) + ".csv", read_file_prefix)


# you shouldn't call this - instead call convert_instances()
# path = same as above
# save_file_name = name for prefix of save file
# read_file_prefix = same as above
def save_data(path, save_file_name, read_file_prefix):
    b = np.loadtxt(path + save_file_name, delimiter=',')
    adj_mat = create_adjacency_matrix(b)
    idx = re.search(read_file_prefix + '(.*)\\.csv', save_file_name).group(1)
    np.savetxt("../datasets/data_as_adj/set_cover/set_cover_" + str(idx) + ".txt", adj_mat, fmt="%.2f")


def main():
    lower = int(sys.argv[1])
    upper = int(sys.argv[2])
    path = sys.argv[3]
    convert_instances(lower, upper, path, "set_cover_")


if __name__ == '__main__':
    main()
