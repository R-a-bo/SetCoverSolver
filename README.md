Rabo Birch, Daniel Firebanks, Emily Hamlin, Christian Ikeokwu

# SetCoverSolver

## Project Description

## Code

All code is in the `SetCoverSolver/code/` and `SetCoverSolver/cnn_processing/code/` folders.

### SetCoverSolver/code/

#### approximations.py

`approximations.py` contains an Approximations class with an exact solution as well as four approximation methods.

  * `integer_progam()` uses integer programming to find an exact solution to the given set cover instance.
  * `deterministic_rounding()` finds an approximate solution by solving the linear programming formulation of Set Cover and including a subset in the cover if the lp variable for that subset is >= 1/f, where f is the max number of sets in which any element appears
  * `dual_rounding()` approximates by solving the dual of the Set Cover LP and including a subset in the cover if the constraint for that subset is tight
  * `primal_dual()` approximates by starting with any solution to the dual, then choosing an element and increasing the value of the dual variable corresponding to it until some constraint goes tight and repeating this until we have fully covered the universe
  * `greedy_weighted()` approximates by choosing subsets greedily by minimum ratio of weight to number of uncovered elements it contains
  * `best()` finds the overall cost of each approximation and outputs a list of costs as well as the label of the approximation alg that produced the lowest cost

#### data_io.py

Reads in (or generates) specified datasets, then outputs them to csv files to be later read into `neural_net.py`. Run using:

```python data_io.py [number of instances to generate] [starting index of file names to store] [whether we are using existing datasets or not (1 or 0)]```

We will eventually make this more command-line friendly so that we don't have to go into the code to change parameters.

#### dataset.py

`dataset.py` handles reading in and generating data and turning them into instances. It contains an Instance class that stores each set cover instance in set and graph representations, as well as other information such as label. `dataset.py` also contains a Dataset class with several methods:

  * `clean_set_cover(subsets)` takes in a list of subsets and removes any duplicate and/or empty subsets
  * `generate_instance(n, m, l, w, name)` takes in
      * n: range of numbers
      * m: size of union set
      * l: number of subsets
      * w: range of values for weights
      * name: name of the instance
    
      and outputs a randomly generated set cover.
      
  * `nonweighted_preprocess(fname)` reads in files from the frb dataset and converts them to set cover instances
  * `weighted_preprocess(fname)` reads in files from the scp (?) dataset and converts them to set cover instances
  * `read(f_name)` reads in a file and applies the correct preprocessing to it (nonweighted or weighted)

#### set_to_matrix.py

### SetCoverSolver/cnn_processing/code/

## Other

python get_node2vec.py /Users/cikeokwu/Desktop/snap-master/examples/node2vec/ /Users/cikeokwu/Desktop/Courses/ML/SetCoverSolver/cnn_processing/datasets/data_as_adj/ /Users/cikeokwu/Desktop/Courses/ML/SetCoverSolver/cnn_processing/datasets/raw_node2vec/ /Users/cikeokwu/Desktop/Courses/ML/SetCoverSolver/cnn_processing/datasets/stats/ set_cover 1 1


python get_histograms.py /Users/cikeokwu/Desktop/Courses/ML/SetCoverSolver/cnn_processing/datasets/raw_node2vec/ /Users/cikeokwu/Desktop/Courses/ML/SetCoverSolver/cnn_processing/datasets/tensors/ set_cover 1 1 400 5


python main.py /Users/cikeokwu/Desktop/Courses/ML/SetCoverSolver/cnn_processing/datasets/ set_cover 1 1 400 5

