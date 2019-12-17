Rabo Birch, Daniel Firebanks, Emily Hamlin, Christian Ikeokwu

# SetCoverSolver

## Project Description

The set cover problem can be solved with a variety of approximation algorithms. However, these approximation algorithms will have a different performance depending on the instance of set cover, so there is no one-size-fits-all approximation method. Depending on the type of problem being solved, certain algorithms can lead to better accuracy or faster runtimes. We want to address this problem by building a machine learning model that is able to take any instance of set cover and choose the best algorithm for it. Inspired by the Newman et al. paper on Spectrum Repacking, this project is an optimizer that: 

  * solves a classification problem given a graph instance and an approximation algorithm as a label
  * applies the identified algorithm and outputs the minimum sized set that contains all the elements in the universe

## Code

Data code in `SetCoverSolver/Data/` and CNN code in `SetCoverSolver/CNN/code/` folders.

### Instructions

#### 0. To generate the folder structure (do this once if you haven't already)

` cd CNN `

` python create_folders.py `

#### 1. To generate/read data

- __IMPORTANT NOTE 1:__ If you will use our datasets instead of generating new ones, we have created `set_cover_classes_[range of files].txt`files for all of them, which you can find in the folder `CNN/datasets/classes/stored_set_cover`. Just change the file name to `set_cover_classes.txt` depending on the dataset you want to test it on, and move it to `CNN/datasets/classes/set_cover/`.

` cd Data `

- Run this command, where the first argument is the number of instances to generate, the second argument is the starting index of the file and the third one whether we want to use generated instances, existing, or both.
- __IMPORTANT NOTE 2:__ You should try to keep track of the starting indices you use and the number of instances you generate so there is no overlap. So if you start at index 0 and generate 100 instances (0-99), the next starting index for generation should be 100.
- __IMPORTANT NOTE 3:__ This script also creates a file called set_cover_classes.txt in the `CNN/datasets/classes/set_cover/` folder. Make sure to take it out after one run if you don't want to override it!

` python data_io.py 1000 0 0 `

- Afterwards, move data to a folder called DataSetCover_0-1000, where the range depends on the indices of the number of instances generated. This folder can be placed anywhere, as long as it is properly referenced in Step 2.
 

#### 2. To preprocess for CNN

` cd CNN/code `

- To create adjacency matrices and store them in ` ../datasets/data_as_adj/set_cover/ `

` python cnn_preoprocessing.py 0 1000 DataSetCover_0-1000/ `

Make sure to give the proper path of the DataSetCover folder, including final '/'. For example, if the folder was located in Data, write

` python cnn_preoprocessing.py 0 1000 ../../Data/DataSetCover_0-1000/`

- To create node embeddings and store them in ` ../datasets/raw_node2vec/ `

` python get_node2vec.py ../datasets/data_as_adj/ ../datasets/raw_node2vec/ ../datasets/stats/ set_cover 1 1 `

- To create histograms and store them in ` ../datasets/tensors/ `

` python get_histograms.py ../datasets/raw_node2vec/ ../datasets/tensors/ set_cover 1 1 400 5 `


#### 3. To run CNN

` python main_network.py ../datasets/ set_cover 1 1 400 5 `

----------------------------------------------------------------

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

### SetCoverSolver/CNN/code/

__TODO: Change PCA parameters!! Play around with max_channels and other stuff__



