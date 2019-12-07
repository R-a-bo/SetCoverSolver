""" approximations.py
    --> implements a variety of approximation algorithms for set cover"""

import pulp      # you will need to pip install pulp :)

"""NOTE!!! This does not correctly handle duplicate sets right now. As long as we have no duplicate sets, it's fine.
    we just need to make sure this is the case for our sets."""

# curious about this other greedy method: https://arxiv.org/pdf/1506.04220.pdf

class Approximations:
    def __init__(self, universe, subset_tuples):
        self.universe = universe
        self.subset_tuples = subset_tuples
        #self.subsets = subsets
        #self.weights = weights

    def valid(self):
        #elements = set(e for s in self.subset_tuples for e in s)
        elements = set()
        for subset in self.subset_tuples:
            for element in subset[0]:
                elements.add(element)
        #print(list(elements)[:10], list(self.universe)[:10])
        # Check the subsets cover the universe
        return elements == self.universe

    def cost(self, cover):
        cover_cost = 0
        for subset_tuple in cover:
            cover_cost += subset_tuple[1] #self.weights[self.subsets.index(subset)]
        return cover_cost

    def integer_program(self):
        """ Integer programming implementation.
            This is the EXACT SOLUTION!!
            Help from: https://pythonhosted.org/PuLP/CaseStudies/a_set_partitioning_problem.html"""

        # subsets need to be tuples for this to work
        subsets = [tuple(s[0]) for s in self.subset_tuples]
        #print(subsets)
        #print(subsets)

        # create decision variables
        x = pulp.LpVariable.dicts('s', subsets, lowBound=0, upBound=1, cat='Integer')

        # create the integer program
        integer_program = pulp.LpProblem("Set Cover Integer Programming", pulp.LpMinimize)

        # add the objective function
        integer_program += sum([self.subset_tuples[s][1] * x[subsets[s]] for s in range(len(subsets))])

        # add the constraints
        for element in self.universe:
            integer_program += sum([x[subset] for subset in subsets if element in subset]) >= 1

        #print(integer_program)

        integer_program.solve()

        # create the cover based on results of IP
        #cover = [set(subset) for subset in self.subset_tuples if x[self.subset_tuples[0]].value() == 1.0]
        cover = [self.subset_tuples[i] for i in range(len(self.subset_tuples))
                if x[tuple(self.subset_tuples[i][0])].value() == 1.0]

        return cover, self.cost(cover)

    def deterministic_rounding(self):
        """ Linear programming with deterministic rounding. """

        subsets = [tuple(s[0]) for s in self.subset_tuples]

        # create (continouous) decision variables
        x = pulp.LpVariable.dicts('s', subsets, lowBound=0, cat='Continuous')

        # create the linear program
        linear_program = pulp.LpProblem("Set Cover Deterministic Rounding", pulp.LpMinimize)

        # add the objective function
        linear_program += sum([self.subset_tuples[s][1] * x[subsets[s]] for s in range(len(subsets))])

        # add the constraints
        for element in self.universe:
            linear_program += sum([x[subset] for subset in subsets if element in subset]) >= 1

        linear_program.solve()

        # create the cover using deterministic rounding
        cover = []
        f_i_vals = []
        for element in self.universe:
            f_i = 0
            for subset in self.subset_tuples:
                if element in subset[0]:
                    f_i += 1
            f_i_vals.append(f_i)
        f = max(f_i_vals)

        #for subset in x:
            #print(x[subset].value())

        #cover = [set(subset) for subset in subsets if x[subset].value() >= 1/f]
        cover = [self.subset_tuples[i] for i in range(len(self.subset_tuples))
                if x[tuple(self.subset_tuples[i][0])].value() >= 1/f]

        return cover, self.cost(cover)

    def dual_rounding(self):
        # create an LP for the dual
        #subsets = [tuple(s[0]) for s in self.subset_tuples]
        universe = list(self.universe)

        # create (continouous) decision variables
        y = pulp.LpVariable.dicts('s', universe, lowBound=0, cat='Continuous')

        # create the dual lp
        dual_program = pulp.LpProblem("Set Cover Dual Rounding", pulp.LpMaximize)

        # add the objective function
        dual_program += sum([y[element] for element in universe])

        # add the constraints
        for subset in self.subset_tuples:
            dual_program += sum(y[element] for element in subset[0]) <= subset[1]

        dual_program.solve()

        #for element in y:
            #print(y[element].value())

        #cover = [self.subset_tuples[i] for i in range(len(self.subset_tuples))
                #if x[tuple(self.subset_tuples[i][0])].value() >= 1/f]

        cover = []
        for subset in self.subset_tuples:
            # i wonder if I could get this directly from the dual program I created?
            print(sum(y[element] for element in subset[0]).value(), subset[1])
            #print(subset[1])
            if sum(y[element] for element in subset[0]).value() == subset[1]:
                cover.append(subset)

        return cover, self.cost(cover)


    def greedy_unweighted(self):
        """this is going to error now, don't use. just here for reference."""

        """ Here is an implementation of a greedy approximation for unweighted SC
            SOURCE: http://www.martinbroadhurst.com/greedy-set-cover-in-python.html"""

        covered = set()
        cover = []
        # Greedily add the subsets with the most uncovered points
        while covered != self.universe:
            subset = max(self.subsets, key=lambda s: len(s - covered))
            cover.append(subset)
            covered |= subset

        return cover, self.cost(cover)

    def greedy_weighted(self):
        """My edits of greedy unweighted to make it weighted"""

        #maximum = max(self.weights)+1
        #print([self.subset_tuples[i][1] for i in range(len(self.subset_tuples))])
        maximum = max([self.subset_tuples[i][1] for i in range(len(self.subset_tuples))]) + 1

        covered = set()
        cover = []
        # Greedily add the subsets with the most uncovered points
        while covered != self.universe:
            min_value = maximum      # so that we always know this value will be bigger than every min_value
            min_subset = self.subset_tuples[0][0]
            for i in range(len(self.subset_tuples)):
                if len(self.subset_tuples[i][0] - covered) > 0:       # avoiding division by zero errors
                    value = self.subset_tuples[i][1]/len(self.subset_tuples[i][0] - covered)
                    if value < min_value:
                        min_value = value
                        min_subset = self.subset_tuples[i]

            cover.append(min_subset)
            #print("subset:",min_subset)
            covered |= min_subset[0]  # this apparently means covered = covered | subset
            #print("covered:", covered)

        return cover, self.cost(cover)

    def best(self):
        """runs each approximation algorithm and returns the one that does best"""

        costs = [self.greedy_weighted()[1],
                self.deterministic_rounding()[1],
                self.dual_rounding()[1]]   # add more as they are implemented

        #labels = ["greedy", "deterministic rounding", "dual rounding"]
        labels = [0, 1, 2]     # scikit-learn doesn't like strings

        index_min = min(range(len(costs)), key=costs.__getitem__)
        print("costs:", costs)

        # if multiple sets are equal, we currently return the first in the list.
        # Would it be better to return randomly instead?

        return labels[index_min]

def main():
    """universe = set(range(1, 11))
    subsets = [set([1, 2, 3, 8, 9, 10]),
        set([1, 2, 3, 4, 5]),
        set([4, 5, 7]),
        set([5, 6, 7]),
        set([6, 7, 8, 9, 10])]
    weights = [1,1,1,1,1]"""

    # one of daniel's random graphs:
    """universe = {4, 70, 8, 41, 12, 77, 44, 21, 53, 87}
    subsets = [{70, 41, 12, 77, 44, 21, 87}, {70, 8, 44, 77, 53, 87}, {41, 12}, {4, 70, 8, 41, 12, 44, 53, 87}]
    weights = [1,1,1,1]"""

    # example where IP and LP are different. Results of LP are as expected.
    # (source: http://math.mit.edu/~goemans/18434S06/setcover-tamara.pdf)
    universe = {1, 2, 3, 4, 5, 6}
    subsets = [{1,2}, {1,3}, {2,3}, {2,4,6}, {3,5,6}, {4,5,6}, {4,5}]
    #weights = [1,1,1,1,1,1,1]          # for this, dual does very badly!
    #weights = [1, 7, 8, 2, 3, 5, 1]
    weights = [1, 7, 8, 9, 1, 4, 3]     # for this arbitrary set of weights, they all return the same SC
    subset_tuples = [(subsets[i], weights[i]) for i in range(len(subsets))]
    print(subset_tuples)

    #greedy_unweighted_cover = greedy_unweighted(universe, subsets)
    solns = Approximations(universe, subset_tuples)
    if solns.valid():
        greedy_weighted_cover = solns.greedy_weighted()
        integer_program_cover = solns.integer_program()
        deterministic_rounding_cover = solns.deterministic_rounding()
        dual_rounding_cover = solns.dual_rounding()

        print("integer program (exact soln):", integer_program_cover)
        print("greedy algorithm:            ", greedy_weighted_cover)
        print("deterministic LP rounding:   ", deterministic_rounding_cover)
        print("dual rounding:               ", dual_rounding_cover)

        print(solns.best())


        #should be:
        #integer program (exact soln): ([{1, 3}, {2, 3}, {4, 5, 6}], 3)
        #greedy algorithm:             ([{2, 4, 6}, {1, 3}, {3, 5, 6}], 3)
        #deterministic LP rounding:    ([{1, 2}, {1, 3}, {2, 3}, {4, 5, 6}], 4)
    else:
        print("sets can't cover the universe!")

    #print("greedy_unweighted_cover:", greedy_unweighted_cover)


if __name__ == '__main__':
    main()
