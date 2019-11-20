"""https://www.geeksforgeeks.org/python-linear-programming-in-pulp/"""

# import the library pulp as p
import pulp

"""
# Create a LP Minimization problem
Lp_prob = pulp.LpProblem('Problem', pulp.LpMinimize)

# Create problem Variables
x = pulp.LpVariable("x", lowBound = 0)   # Create a variable x >= 0
y = pulp.LpVariable("y", lowBound = 0)   # Create a variable y >= 0

# Objective Function
Lp_prob += 3 * x + 5 * y

# Constraints:
Lp_prob += 2 * x + 3 * y >= 12
Lp_prob += -x + y <= 3
Lp_prob += x >= 4
Lp_prob += y <= 3

# Display the problem
print(Lp_prob)

status = Lp_prob.solve()   # Solver
print(pulp.LpStatus[status])   # The solution status

# Printing the final solution
print(pulp.value(x), pulp.value(y), pulp.value(Lp_prob.objective))"""

"""
A set partitioning model of a wedding seating problem

Authors: Stuart Mitchell 2009
"""

######################## wedding problem ###############################

max_tables = 5
max_table_size = 4
guests = 'A B C D E F G I J K L M N O P Q R'.split()

def happiness(table):
    """
    Find the happiness of the table
    - by calculating the maximum distance between the letters
    """
    return abs(ord(table[0]) - ord(table[-1]))

#create list of all possible tables
possible_tables = [tuple(c) for c in pulp.allcombinations(guests,
                                        max_table_size)]

#print(possible_tables)

#create a binary variable to state that a table setting is used
x = pulp.LpVariable.dicts('table', possible_tables,
                            lowBound = 0,
                            upBound = 1,
                            cat = pulp.LpInteger)

seating_model = pulp.LpProblem("Wedding Seating Model", pulp.LpMinimize)

seating_model += sum([happiness(table) * x[table] for table in possible_tables])

#specify the maximum number of tables
seating_model += sum([x[table] for table in possible_tables]) <= max_tables, \
                            "Maximum_number_of_tables"

#A guest must seated at one and only one table
for guest in guests:
    seating_model += sum([x[table] for table in possible_tables
                                if guest in table]) == 1, "Must_seat_%s"%guest

seating_model.solve()

print("The choosen tables are out of a total of %s:"%len(possible_tables))
for table in possible_tables:
    if x[table].value() == 1.0:
        print(table)


## variables can also be integer or binary: https://www.coin-or.org/PuLP/pulp.html
# write cat='Integer' or cat='Binary'
