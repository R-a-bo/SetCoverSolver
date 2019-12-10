import os

directory = "/Users/cikeokwu/Desktop/Courses/ML/SetCoverSolver/cnn_processing/datasets/data_as_adj/set_cover"
for file_name in os.listdir(directory):
    beg = file_name[:-8]
    endend = file_name[-4:]
    end = file_name[-8:-4]
    # print(beg)
    # print(end)
    # print(endend)
    new_num = (int(end) % 3000) - 1
    new_filename = beg + str(new_num) + endend
    print file_name
    print new_filename
    os.rename( directory + "/" + file_name, directory + "/" + new_filename)
