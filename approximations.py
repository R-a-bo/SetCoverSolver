"""TODO: document"""

# Book notes:

# approx method 1: linear relaxation w/ deterministic rounding
#   --> solve the linear relaxation. Include subset S_j if x_j >= 1/f,
#       where f is the maximum number of sets in which any element appears.
#   --> it's an f-approximation
#   --> therefore, it's a 2-approx for vertex cover

# approx method 2: rounding a dual solution

# approx method 3: greedy approx. A ln(n) approximation


def greedy_unweighted_set_cover(universe, subsets):
    """ Here is an implementation of a greedy approximation for unweighted SC
        SOURCE: http://www.martinbroadhurst.com/greedy-set-cover-in-python.html"""

    elements = set(e for s in subsets for e in s)
    # Check the subsets cover the universe
    if elements != universe:
        return None
    covered = set()
    cover = []
    # Greedily add the subsets with the most uncovered points
    while covered != elements:
        subset = max(subsets, key=lambda s: len(s - covered))
        cover.append(subset)
        covered |= subset

    return cover

def greedy_weighted_set_cover(universe, subsets, weights):
    """My edits of greedy unweighted to make it weighted"""

    maximum = max(weights)+1
    elements = set(e for s in subsets for e in s)

    """ # in for loop form so my smol brain can understand:
    elements = set()
    for s in subsets:
        for e in s:
            elements.add(e)"""

    # Check the subsets cover the universe
    if elements != universe:
        return None

    covered = set()
    cover = []
    # Greedily add the subsets with the most uncovered points
    while covered != elements:
        min_value = maximum      # so that we always know this value will be bigger than every min_value
        min_subset = subsets[0]
        for i in range(len(subsets)):
            if len(subsets[i] - covered) > 0:       # avoiding division by zero errors
                value = weights[i]/len(subsets[i] - covered)
                if value < min_value:
                    min_value = value
                    min_subset = subsets[i]

        cover.append(min_subset)
        #print("subset:",min_subset)
        covered |= min_subset  # this apparently means covered = covered | subset
        #print("covered:", covered)

    return cover


def main():
    universe = set(range(1, 11))
    subsets = [set([1, 2, 3, 8, 9, 10]),
        set([1, 2, 3, 4, 5]),
        set([4, 5, 7]),
        set([5, 6, 7]),
        set([6, 7, 8, 9, 10])]

    weights = [1,1,1,1,1]   # with this, the weighted and unweighted algs get the same value, as they should

    cover = greedy_unweighted_set_cover(universe, subsets)
    new_cover = greedy_weighted_set_cover(universe, subsets, weights)
    print(cover)
    print(new_cover)

if __name__ == '__main__':
    main()
