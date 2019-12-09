from operator import itemgetter

sets = [{1,2}, {1,3}, {2,3}, {2,4,6}, {3,5,6}, {4,5,6}, {4,5}, {1,2}, {}, set()]
weights = [4, 7, 8, 2, 3, 5, 1, 1, 5, 8]
subsets = [(sets[i], weights[i]) for i in range(len(sets))]

subsets.sort(key=itemgetter(1))
print(subsets)
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

print(unique_subsets)
