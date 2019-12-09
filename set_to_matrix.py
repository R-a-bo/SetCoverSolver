from dataset import *
import networkx as nx
import numpy as np
from tqdm import tqdm

''' Approach 1: Elements in matrix
- Create a dictionary mapping the elements in the union to a list of ordered numbers 
	 - Union: [4, 5, 7, 10, 16]
	 - Map: {4: 0, 5: 1, 7: 2, 10: 3, 16: 4}
- Create a zero matrix of len(union) x len(subsets)
- Matrix[union_map[subset element]][subset number] = weight_list[subset number] '''


def element_matrix(instance):
    print("Creating element matrix...\n")
    union = instance.union
    subsets = instance.sets
    weights = instance.weights

    union_map = dict(zip(union, range(len(union))))

    rows = len(union)
    cols = len(subsets)
    matrix = np.zeros((rows, cols))

    for i in range(len(subsets)):
        # print(f"Set {i} is {subsets[i]}")
        for element in subsets[i]:
            matrix[union_map[element]][i] = weights[i]

    return np.array(matrix)


''' Approach 2: Elements as nodes
- The set of nodes will represent each element in the union
- The set of weighted edges will represent whether 2 elements $n_i$ and $n_j$ are contained in two subsets $S_i$ and $S_j$, and the weight assigned to that edge will be the aggregate weight of $S_i$ and $S_j$.'''


def element_graph(instance):
    print("Creating element graph...\n")
    union = instance.union
    subsets = instance.sets
    weights = instance.weights

    edge_list = []
    node_list = set()
    # Algorithm to turn a set into a graph
    for i in tqdm(range(len(subsets))):
        set1 = subsets[i]
        for number1 in set1:
            for j in range(i+1, len(subsets)):
                set2 = subsets[j]
                for number2 in set2:
                    if number2 in set1 and number1 in set2 and (number1, number2, weights[i] + weights[j]) not in edge_list and (number2, number1, weights[i] + weights[j]) not in edge_list:
                        # print("Number1", number1, "|| Number2", number2)
                        # print("Set1", set1, " || Set2", set2)
                        edge_list.append(
                            (number1, number2, weights[i] + weights[j]))
                    node_list.add(number2)
            node_list.add(number1)

    adj_matrix = to_graph(node_list, edge_list)

    return adj_matrix


''' Approach 3: Subsets as nodes
- The set of nodes will represent each subset $S_i$ in the family of subsets $\S$
- The set of weighted edges will represent whether 2 subsets $S_i$ and $S_j$ contain an element $s_i = s_j$ in common, and the weight assigned to that edge will be the aggregate weight of $S_i$ and $S_j$. '''


def subset_graph(instance):
    print("Creating subset graph...\n")
    union = instance.union
    subsets = instance.sets
    weights = instance.weights

    edge_list = []
    node_list = set()

    subsets = [list(element) for element in subsets]

    for i in tqdm(range(len(subsets))):
        set1 = subsets[i]
        for number1 in set1:
            for j in range(i+1, len(subsets)):
                set2 = subsets[j]
                for number2 in set2:
                    if len(set(set1 + set2)) != 0 and (i, j, weights[i] + weights[j]) not in edge_list:
                        # print("Number1", number1, "|| Number2", number2)
                        # print("Set1", set1, " || Set2", set2)
                        edge_list.append(
                            (i, j, weights[i] + weights[j]))
                node_list.add(j)
        node_list.add(i)

    adj_matrix = to_graph(node_list, edge_list)

    return adj_matrix


''' Takes in a list of nodes and edges, returns the adjacency matrix of a graph'''
def to_graph(node_list, edge_list):
    mg = nx.MultiGraph()

    # Add weighted edges from the list
    for edge in edge_list:
        mg.add_edge(edge[0], edge[1], weight=edge[2])

    # Add the nodes that haven't been added
    nodes = list(mg.nodes)
    node_list = [node for node in node_list if node not in nodes]

    mg.add_nodes_from(node_list)

    return np.array(nx.to_numpy_matrix(mg))


def test_main():

    # Generate an instance and test all representations
    data = Dataset()

    n = 20  # upper bound for range of numbers
    m = 5  # size of set
    l = 15   # size of list of subsets
    w = 10

    instance1 = data.generate_instance(n, m, l, w)
    rep1 = element_matrix(instance1)
    print("Pure matrix representation")
    print(rep1)
    print("------------------------")

    rep2 = element_graph(instance1)
    print("Elements as nodes in a graph")
    print(rep2)
    print("------------------------")

    rep3 = subset_graph(instance1)
    print("Subsets as nodes in a graph")
    print(rep3)
    print("------------------------")


if __name__ == "__main__":
    test_main()
