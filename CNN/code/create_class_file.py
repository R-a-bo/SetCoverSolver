import os
import pandas as pd 

def store_labels():
	file = input("Give me ya labels.csv path (including labels.csv): ")
	dset_name = input("Dataset name? ")
	out_path = input("Fine. Now give me the output file PATH: ")
	csv = pd.read_csv(file, header=None)
	if not os.path.exists(out_path + "/" + dset_name):
		os.makedirs(out_path + "/" + dset_name)
	
	with open(out_path + "/" + dset_name + "/" + dset_name + "_classes.txt", "w") as writer:
		for label in csv[1]:
			writer.write(str(label) + "\n")

def change_files():
	prefix = "./DataSetCover_2001-2691/"
	files = [prefix + "labels.csv", prefix + "costs.csv"]
	
	for file in files:
		csv = pd.read_csv(file, header=None)

		csv[0] = [f"set_cover_{i}.csv" for i in range(2001, 2692)]

		csv.to_csv(file)



def rename_files():
	prefix = "./DataSetCover_2001-2691/"
	files = os.listdir(prefix)
	files = [file for file in files if "Instance" in file]
	i = 2001

	for file in files:
		new_file = f"set_cover_{i}.csv"

		with open(prefix + file, "r") as reader:
			all_file = reader.read()

		with open(prefix + new_file, "w") as writer:
			writer.write(all_file)

		i += 1

if __name__ == "__main__":
	# rename_files()
	# change_files()
	store_labels()
