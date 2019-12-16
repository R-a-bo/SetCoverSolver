import os

# Our CNN requires you to have a specific folder structure, which we have created here.
# Run this script once only!

try:
	# Root folder
	os.makedirs("datasets/")

	# Subfolders
	os.makedirs("datasets/classes/")
	os.makedirs("datasets/data_as_adj/")
	os.makedirs("datasets/raw_node2vec/")
	os.makedirs("datasets/results/")
	os.makedirs("datasets/stats/")
	os.makedirs("datasets/tensors/")

	# Subsubfolders
	os.makedirs("datasets/classes/set_cover/")
	os.makedirs("datasets/data_as_adj/set_cover/")
	os.makedirs("datasets/raw_node2vec/set_cover/")
	os.makedirs("datasets/stats/set_cover/")
	os.makedirs("datasets/tensors/set_cover/")

	# Cheeky one
	os.makedirs("datasets/tensors/set_cover/node2vec_hist/")

except Exception as e:
	print(e)