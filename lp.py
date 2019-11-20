import pulp

universe = set(range(1, 11))
subsets = [set([1, 2, 3, 8, 9, 10]),
    set([1, 2, 3, 4, 5]),
    set([4, 5, 7]),
    set([5, 6, 7]),
    set([6, 7, 8, 9, 10])]

# they need to be tuples for this to work
subsets = [tuple(s) for s in subsets]
#print(subsets)

weights = [1,1,1,1,1]

x = pulp.LpVariable.dicts('s', subsets, lowBound=0, upBound=1, cat='Integer')

sc_ip = pulp.LpProblem("Set Cover Integer Programming", pulp.LpMinimize)

# sum w_i j_i
sc_ip += sum([weights[s] * x[subsets[s]] for s in range(len(subsets))])

for element in universe:
    sc_ip += sum([x[subset] for subset in subsets if element in subset]) >= 1

print(sc_ip)

sc_ip.solve()

print("The choosen subsets are:")
for subset in subsets:
    if x[subset].value() == 1.0:
        print(subset)
