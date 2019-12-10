from __future__ import print_function
import numpy as np
import pandas as pd

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


def convert_instances(lower, upper, path):
    for i in range(lower, upper):
        save_data(path, "Instance" + str(i) + ".csv")


def save_data(path, file_name):
    b = np.loadtxt(path + file_name, delimiter=',')
    adj_mat = create_adjacency_matrix(b)
    np.savetxt("../datasets/data_as_adj/set_cover/set_cover_" + file_name[8:13] + ".txt", adj_mat, fmt="%.2f")


# Old test code
# adj = create_adjacency_matrix(B)
# for i in range(100):
#     np.savetxt("../datasets/data_as_adj/test_data/test_data_" + str(i) + ".txt", adj, fmt="%.2f")
