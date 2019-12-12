#!/usr/bin/env bash

python get_node2vec.py /Users/cikeokwu/Desktop/snap-master/examples/node2vec/ /Users/cikeokwu/Desktop/Courses/ML/SetCoverSolver/cnn_processing/datasets/data_as_adj/ /Users/cikeokwu/Desktop/Courses/ML/SetCoverSolver/cnn_processing/datasets/raw_node2vec/ /Users/cikeokwu/Desktop/Courses/ML/SetCoverSolver/cnn_processing/datasets/stats/ set_cover 1 1


python get_histograms.py /Users/cikeokwu/Desktop/Courses/ML/SetCoverSolver/cnn_processing/datasets/raw_node2vec/ /Users/cikeokwu/Desktop/Courses/ML/SetCoverSolver/cnn_processing/datasets/tensors/ set_cover 1 1 400 5
