import os

# Our CNN requires you to have a specific folder structure, which we have created here.
# Run this script once only!

try:
    # Root folder
    if not os.path.exists("datasets/"):
        os.makedirs("datasets/")

    # Subfolders
    subfolders = ["datasets/classes/", "datasets/data_as_adj/", "datasets/raw_node2vec/", "datasets/results/",
                  "datasets/stats/", "datasets/tensors/"]
    for subfolder in subfolders:
        if not os.path.exists(subfolder):
            os.makedirs(subfolder)

    # Subsubfolders
    subsubfolders = ["datasets/classes/set_cover/", "datasets/data_as_adj/set_cover/",
                     "datasets/raw_node2vec/set_cover/",
                     "datasets/stats/set_cover/", "datasets/tensors/set_cover/",
                     "datasets/tensors/set_cover/node2vec_hist/"]

    for subsubfolder in subsubfolders:
        if not os.path.exists(subsubfolder):
            os.makedirs(subsubfolder)


except Exception as e:
    print(e)
