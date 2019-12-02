""" synthesize_dataset.py
	reads in and generates data, turns them into instances, calls approximations class to produce labels
	"""

import random

class Instance(object):
	def __init__(self, union, subsets):
		self.union = list(union)
		self.subsets = subsets 
		self.sets = [tup[0] for tup in subsets]
		self.weights = [tup[1] for tup in subsets]

class Dataset:
	def __init__(self):
		#self.set_covers = []
		self.instances = []

	def generate_instance(self, n, m, l, w):
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

		# Add weights to each subset
		weights = [random.randrange(w) for s in subsets]

		# Put them together and add them to the 
		weighted_subsets = list(zip(subsets, weights))

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
		union = set(range(0, union_range + 1))
		subsets = [{int(num) for num in subset} for subset in frb_els]

		# Add a weight of 1 to each
		unweighted_subsets = list(zip(subsets, [1]*len(subsets)))

		return union, unweighted_subsets

	def weighted_preprocess(self, fname):
		""" Preprocess files with name scp in them - they are instances of weighted set cover """

		# Read data and split lines
		# fname = "data/scp/scp43.txt"
		scp = open(fname, 'r')
		scp_txt = scp.read()
		scp_lines = scp_txt.split('\n')

		# Separate different blocks of information
		scp_meta = scp_lines[0]
		scp_weights = scp_lines[1:85]
		scp_els = scp_lines[85:]

		# For the matrix form, get the number of rows and columns
		num_rows = int(scp_meta.split()[0])
		num_cols = int(scp_meta.split()[1])

		# Get weights for each column, where element i is the weight for column i
		weights = [el.strip().split() for el in scp_weights]
		weights = [int(el) for w_list in weights for el in w_list]
		weight_map = dict(zip(range(1, num_cols + 1), weights))

		# Get the column indices as a list of numbers 
		parsed_els = [el.strip().split() for el in scp_els]
		parsed_els = [int(el) for subset in parsed_els for el in subset]

		# Build the row cover map with structure {row i: [columns that cover row i]}
		row_cover = {}

		# Store ALL the rows being covered = Union set
		union = set(range(1, num_rows + 1))

		# The first element of the parsed numbers 
		col_count = parsed_els[0]

		# Start at the second element of parsed numbers to add columns
		col_idx = 1

		# Build the row_cover dictionary
		for row_idx in range(1, num_rows + 1):
			# Add column indices that cover row i
			row_cover[row_idx] = parsed_els[col_idx:col_idx + col_count - 1]
			
			# Move the column index to the next number representing number of columns
			col_idx += col_count 

			# Only keep going until we don't have any columns left!
			if col_idx < len(parsed_els):
				
				# Get the number of columns that we are about to read
				col_count = parsed_els[col_idx]
				
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

		# Read and add to the instances
		if "frb" in f_name:
			union, subsets = self.nonweighted_preprocess(f_name)
		elif "scp" in f_name:
			union, subsets = self.weighted_preprocess(f_name)
		
		# Create a new instance object and append it to the list of instances
		instance = Instance(union, subsets)
		self.instances.append(instance)
		
		return instance

	def create_instances(self, set_covers):
		"""take each instance in set_covers and run it on our approximations. Set the label to the approx
			technique that leads to the smallest set cover."""
		pass

def main():
	n = 100 # upper bound for range of numbers
	m = 10  # size of set
	l = 5   # size of list of subsets
	w = 10

	dset = Dataset()

	# Test generation
	generated_instance = dset.generate_instance(n, m, l, w)
	print()
	print("=================================")
	print("Generated union:")
	print(generated_instance.union[:10])
	print("Generated subsets:")
	print(generated_instance.subsets[:10])


	# Test reading files
	weighted_fname = "data/scp/scp43.txt"
	unweighted_fname = "data/frb/frb30-15-msc/frb30-15-1.msc"

	weighted_instance = dset.read(weighted_fname)
	unweighted_instance = dset.read(unweighted_fname)


	print()
	print("=================================")
	print("Weighted union:")
	print(weighted_instance.union[:10])
	print("Weighted subsets:")
	print(weighted_instance.subsets[:10])

	print()
	print("=================================")
	print("Un-weighted union:")
	print(unweighted_instance.union[:10])
	print("Un-weighted subsets")
	print(unweighted_instance.subsets[:10])
	print("=================================")



if __name__ == "__main__":
	main()
