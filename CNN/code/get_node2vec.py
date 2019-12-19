import argparse

import os
import re
import networkx as nx
import numpy as np
from subprocess import call
from sklearn.decomposition import PCA

import tempfile
import shutil
from multiprocessing import Pool, cpu_count
from functools import partial
import time as t
import datetime

# =============================================================================


parser = argparse.ArgumentParser()

# positional arguments (required)
parser.add_argument('path_read', type=str, help='path to adjacency matrices')
parser.add_argument('path_write', type=str, help='path to folder where node2vec embeddings should be saved')
parser.add_argument('path_stats', type=str, help='path to folder where statistics should be saved')
parser.add_argument('dataset', type=str,
                    help='name of the dataset. Must correspond to a valid value that matches an adjacency matrix folder')
parser.add_argument('p', type=str, help='p parameter of node2vec')
parser.add_argument('q', type=str, help='q parameter of node2vec')

# optional arguments
parser.add_argument('--dims', type=int, default=1024,  
                        help='Number of dimensions. Default is 1024.') # ORIGINAL = 128
parser.add_argument('--max_n_channels', type=int, default=5,
                    help='maximum number of channels that we will be able to pass to the network')

args = parser.parse_args()

# convert command line arguments
# path_node2vec = args.path_node2vec
path_read = args.path_read
path_write = args.path_write
path_stats = args.path_stats
dataset = args.dataset
dims = args.dims
p = args.p
q = args.q
max_n_channels = args.max_n_channels

# =============================================================================

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [atoi(c) for c in re.split('(\d+)', text)]

def get_embeddings_node2vec(g, d, p, q, dimensions):
    my_pca = PCA(n_components=d)

    my_edgelist = list(nx.generate_edgelist(g, data=["weight"]))

    # create temp dir to write and read from
    tmpdir = tempfile.mkdtemp()

    # create subdirs for node2vec
    os.makedirs(tmpdir + '/graph/')
    os.makedirs(tmpdir + '/emb/')

    # write edge list
    with open(tmpdir + '/graph/input.edgelist', 'w') as my_file:
        my_file.write('\n'.join('%s' % x for x in my_edgelist))

    # execute node2vec
    #print( tmpdir + '/emb/output.emb'
    call(['python' + ' main_node2vec.py  --input ' + tmpdir + '/graph/input.edgelist' + ' --output ' + tmpdir + '/emb/output.emb' + ' --p ' + p + ' --q ' + q + ' --dimensions ' + str(dimensions) + ' --weighted'], shell=True)
    #call([path_node2vec + 'node2vec  -i:' + tmpdir + '/graph/input.edgelist' + ' -o:' + tmpdir + '/emb/output.emb' + ' -p:' + p + ' -q:' + q + ' -w'], shell=True)

    # read back results
    emb = np.loadtxt(tmpdir + '/emb/output.emb', skiprows=1)

    # sort by increasing node index and keep only coordinates
    emb = emb[emb[:, 0].argsort(), 1:]

    # remove temp dir
    shutil.rmtree(tmpdir)

    # perform PCA on the embeddings to align and reduce dim
    pca_output = my_pca.fit_transform(emb)

    return pca_output

def to_parallelize(file_name, p, q, dataset, path_read, path_write, dimensions):
    excluded = ''
    excluded_exc = ''

    idx = file_name.split('.txt')[0].split('_')[-1:][0]

    adj_mat = np.loadtxt(path_read + dataset + '/' + file_name)

    g = nx.from_numpy_matrix(adj_mat)

    if len(g) < (max_n_channels * 2):  # exclude graphs with less nodes than the required min number of dims
        excluded = file_name
    try:
        emb = get_embeddings_node2vec(g, d=max(20, max_n_channels * 2), p=p, q=q, dimensions=dimensions)  # Original d = max(20, max_n_channels*2)
        np.save(path_write + dataset + '/' + dataset + '_node2vec_raw_p=' + p + '_q=' + q + '_' + idx, emb,
                allow_pickle=False)
    except Exception as e:
        print(e)
        excluded_exc = file_name

    return [len(g), g.number_of_edges(), excluded, excluded_exc]


# =============================================================================

def main():
    my_date_time = '_'.join(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S").split())

    file_names = os.listdir(path_read + dataset + '/')
    if ".DS_Store" in file_names:
        file_names.remove(".DS_Store")

    file_names.sort(key=natural_keys)
    print( '===== Number of graphs: =====', len(file_names))
    print( '*** Head ***')
    print( file_names[:5])
    print( '*** Tail ***')
    print( file_names[-5:])

    # Create folder if it doesn't exist
    if not os.path.exists(path_write + dataset + "/"):
        os.makedirs(path_write + dataset + "/")
    if not os.path.exists(path_stats + dataset + "/"):
        os.makedirs(path_stats + dataset + "/")

    # map 'to_parallelize' over all files
    to_parallelize_partial = partial(to_parallelize, p=p, q=q, dataset=dataset, path_read=path_read,
                                     path_write=path_write, dimensions=dims)

    n_jobs = cpu_count()

    print('Using', n_jobs, 'cores')
    start = t.time()

    pool = Pool(processes=n_jobs)
    lol = pool.map(to_parallelize_partial, file_names)
    pool.close()

    stats_array = np.array(lol)

    np.savetxt(path_stats + '/' + dataset + '_' + my_date_time + '.txt', stats_array, fmt='%s')

    end = t.time()
    hours, rem = divmod(end - start, 3600)
    minutes, seconds = divmod(rem, 60)

    print("Done in: {:0>2}:{:0>2}:{:05.2f}".format(int(hours), int(minutes), seconds))


if __name__ == "__main__":
    main()
