""" synthesize_dataset.py
	reads in and generates data, turns them into instances, calls approximations class to produce labels
	"""

import sys
import random
from approximations import Approximations
from operator import itemgetter
from tqdm import tqdm

class Instance(object):
	def __init__(self, union, subsets, name=None, weighted=False):

		# Main features
		self.name = name
		self.union = list(union)
		self.subsets = subsets

		# Separate access to subsets and weights, indices are the same in both lists
		self.sets = [tup[0] for tup in subsets]
		self.weights = [tup[1] for tup in subsets]

		# Indicates whether the instance is weighted or not
		self.is_weighted = weighted

		# Will set up later
		self.element_matrix = None
		self.element_graph = None
		self.subset_graph = None

class Dataset:
	def __init__(self):
		#self.set_covers = []
		self.instances = []
		self.mlinstances = []

	def clean_set_cover(self, subsets):
		"""remove duplicate sets and empty sets"""
		subsets.sort(key=itemgetter(1))
		#print(subsets)
		unique_subsets = []
		for subset in subsets:
		    if len(subset[0]) != 0:
		        in_unique = False
		        for item in unique_subsets:
		            #print(subset[0], item[0])
		            if subset[0] == item[0]:
		                in_unique = True
		                break
		        if in_unique == False:
		            unique_subsets.append(subset)

		return unique_subsets

	def generate_instance(self, n, m, l, w):
		''' Input:
			n: range of numbers
			m: size of union set
			l: number of subsets
			w: range of values for weights

			Output: a union set, and a list of subsets '''

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

		# Add weights to each subset
		weights = [random.randrange(w) for s in subsets]

		# Put them together and add them to the
		weighted_subsets = list(zip(subsets, weights))
		weighted_subsets = self.clean_set_cover(weighted_subsets)

		instance = Instance(U, weighted_subsets)
		self.instances.append(instance)

		return instance

	def nonweighted_preprocess(self, fname):
		""" Preprocess files with name frb in them - they are instances of unweighted set cover.
			We add a weight of 1 to each subset for consistency. """

		# Read data and split lines
		#fname = "data/frb/frb30-15-msc/frb30-15-1.msc"
		frb = open(fname, 'r')
		frb_txt = frb.read()
		frb_lines = frb_txt.split('\n')

		# Get all elements, metadata and subset elements separately
		frb_all = [el for el in frb_lines if len(el) != 0]
		frb_meta = frb_lines[0].split()
		frb_els = [el.split()[1:] for el in frb_lines[1:]]

		# Metadata
		union_range = int(frb_meta[2])
		num_subsets = int(frb_meta[3])

		# Elements
		union = set(range(1, union_range + 1))
		subsets = [{int(num) for num in subset} for subset in frb_els]

		# Add a weight of 1 to each
		unweighted_subsets = list(zip(subsets, [1]*len(subsets)))

		return union, unweighted_subsets

	def weighted_preprocess(self, fname):
		""" Preprocess files with name scp in them - they are instances of weighted set cover """

		# Read data and split lines
		# fname = "data/scp/scp43.txt"
		scp = open(fname, 'r')
		scp = scp.read()
		lines = scp.split('\n')

		# Separate each of the lines and create a list of numbers
		parsed_lines = [el.strip().split() for el in lines]
		parsed_lines = [int(el) for subset in parsed_lines for el in subset]

		# For the matrix form, get the number of rows and columns
		num_rows = int(parsed_lines[0])
		num_cols = int(parsed_lines[1])

		# Separate different blocks of information
		scp_meta = lines[0]
		weights = parsed_lines[2:2 + num_cols]
		elements = parsed_lines[2 + num_cols:]

		# Get weights for each column, where element i is the weight for column i
		weight_map = dict(zip(range(1, num_cols + 1), weights))

		# Build the row cover map with structure {row i: [columns that cover row i]}
		row_cover = {}

		# Store ALL the rows being covered = Union set
		union = set(range(1, num_rows + 1))

		# The first element of the parsed numbers
		col_count = elements[0]

		# Start at the second element of parsed numbers to add columns
		col_idx = 1

		# Build the row_cover dictionary
		for row_idx in range(1, num_rows + 1):
			# Add column indices that cover row i
			row_cover[row_idx] = elements[col_idx:col_idx + col_count - 1]

			# Move the column index to the next number representing number of columns
			col_idx += col_count

			# Only keep going until we don't have any columns left!
			if col_idx < len(elements):

				# Get the number of columns that we are about to read
				col_count = elements[col_idx]

				# Make sure to start a number after the number of columns
				col_idx += 1

		# Now build col_cover as the inverse of row_cover: {column i: rows that are covered by column i}
		col_cover = {}
		for i in range(1, num_cols + 1):
			col_cover[i] = []
			for row in union:
				if i in row_cover[row]:
					col_cover[i].append(row)

		# Make a list of tuplets that contains subsets and their weights!
		weighted_subsets = []

		for col_idx, row_indices in col_cover.items():
			weighted_subsets.append((set(row_indices), weight_map[col_idx]))

		# DONE :)!
		# print(weighted_subsets)
		return [union, weighted_subsets]

	def read(self, f_name):
		""" Takes in a file name and applies the correct preprocessing """

		# Make sure we have the correct file format
		if "frb" not in f_name and "scp" not in f_name:
			print("Wrong filename/unable to preprocess file")
			sys.exit(1)

		# Make name for instance
		t_name = f_name.split("/")
		inst_name = t_name[-1].replace(".txt", "").replace(".msc", "")

		# Read and add to the instances
		if "frb" in f_name:
			union, subsets = self.nonweighted_preprocess(f_name)
			#instance = Instance(union, subsets, name=inst_name)
		else: #if "scp" in f_name:
			union, subsets = self.weighted_preprocess(f_name)
			#instance = Instance(union, subsets, name=inst_name, weighted=True)

		# remove duplicates and empty sets
		subsets = self.clean_set_cover(subsets)

		if "frb" in f_name:
			instance = Instance(union, subsets, name=inst_name)
		else:
			instance = Instance(union, subsets, name=inst_name, weighted=True)

		# Create a new instance object and append it to the list of instances
		self.instances.append(instance)

		return instance

	def add_labels(self, set_covers):
		"""take each instance in set_covers and run it on our approximations. Set the label to the approx
			technique that leads to the smallest set cover."""
		for sc in tqdm(set_covers):
			input = Approximations(set(sc.union), sc.subsets)
			if input.valid():
				costs, label = input.best()
				sc.label = label
				sc.costs = costs
				#print(label)
			else:
				print("not valid")

def main():

	dset = Dataset()

	# Test generation
	n = 100 # upper bound for range of numbers
	m = 10  # size of set
	l = 5   # size of list of subsets
	w = 10

	generated_instance = dset.generate_instance(n, m, l, w)
	print()
	print("=================================")
	print("Generated union:")
	#print(generated_instance.union[:10])
	print(generated_instance.union[:10])
	print("Generated subsets:")
	print(generated_instance.subsets[:10])


	# Test reading files
	weighted_fname = "data/scp/scpd1.txt"
	unweighted_fname = "data/frb/frb30-15-msc/frb30-15-1.msc"

	weighted_instance = dset.read(weighted_fname)
	unweighted_instance = dset.read(unweighted_fname)

	print()
	print("=================================")
	print("Weighted name:")
	print(weighted_instance.name)
	print("Weighted union:")
	print(weighted_instance.union[:10])
	print("Weighted subsets:")
	print(weighted_instance.subsets[:10])

	print()
	print("=================================")
	print("Un-weighted name:")
	print(unweighted_instance.name)
	print("Un-weighted union:")
	print(unweighted_instance.union[:10])
	print("Un-weighted subsets")
	print(unweighted_instance.subsets[:10])
	print("=================================")

	dset.add_labels(dset.instances)
	#print(dset.mlinstances[:5])
	

if __name__ == "__main__":
	main()
