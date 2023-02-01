"""
Modify this docstring.

"""

# import some modules first - how many can you make use of?

import math
import statistics


# define some functions


def get_area_of_lot(length, width):
    """
    Return area of a lot given the length and width of the lot.

    Could this fail?

    """

    # Use a try / except / finally block when something
    # could go wrong
    try:
        area = 0  # fix this
        return area
    except Exception as ex:
        print(f"Error: {ex}")
        return None


# define more functions here (see instuctions)


# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # call your functions here (see instructions)
    print("your code here")


# Why? Why only print if this the module called?
# Because when you write good functions, you may want to
# import this module into another script - just like you did
# math or statistics.
# Build a library of resuable functions to support your domain.

# For example, if your domain:
# Is sports, create functions to provide a list of teams.
# Is pets, create functions to calculate adoption prices.
# Is music, create functions to return a list of your favorite artists.


# When you write reusable functions for your domain, you can
# import the module with your utility functions into other modules
# and use them there.  This is a very common practice.
# Anything you write can be imported into later projects.

#Task 3 Numeric Lists
# Population of trinidad and tobago past 2004 to 2023

#List    
TTPopulation_list=[
1534937,
1531044,
1525663,
1518147,
1519955,
1504709,
1478607,
1469330,
1460177,
1450661,
1440729,
1430377,
1420020,
1410296,
1401191,
1392803,
1384861,
1376919,
1369075,
1361172,
]

years_list = [2014,2015,2016,2017,2018,2019,2020,2021,2022,2023]
pop_list = [1450661, 1460177, 1469330, 1478607, 1504709, 1518147, 1519955, 1525663, 1531044, 1534937]

#List1
print("Descriptive sattsictics on Trinidad and Tobagos Population over the past 20 years")
mean = statistics.mean(TTPopulation_list)
print(f"The mean of Trinidad and Tobagos Population is {mean}")
median = statistics.median(TTPopulation_list)
print(f"The median of Trinidad and Tobagos Population is {median}")
mode = statistics.mode(TTPopulation_list)
print(f"The mode of Trinidad and Tobagos Population is {mode}")

stdev = statistics.stdev(TTPopulation_list)
variance = statistics.variance(TTPopulation_list) 

#List2
correlationyearspop = statistics.correlation(years_list, pop_list)

slope, intercept = statistics.linear_regression(years_list, pop_list)

new_x = max(years_list)
newx = 2024
newy = float(slope * newx + intercept)
print (new_x)

#List3

min_pop = min(TTPopulation_list)
max_pop = max(TTPopulation_list)

population_count = len(TTPopulation_list)
population_sum = sum(TTPopulation_list)

avg = sum / len

#Population over past 20 years in ascrending order

asc_population = sorted(TTPopulation_list)

#Population over past 20 years in descending order
desc_population = sorted(TTPopulation_list, reverse= True)

#List4

FamilyMmbrs_Age = [27,2,13,5,54,2]

#.Append-(add)item to list
FamilyMmbrs_Age.append(13)

#Add item to specific spot
FamilyMmbrs_Age.insert(0,99)

#.Extend-add another list to current list
FamilyMmbrs_Age.extend([20,32,16])

#Remove item from list
FamilyMmbrs_Age.remove(5)

#How many times an item appears in list
FamilyMmbrs_Age.count(2)

#Copy list to new list
Big_Happy_Family = FamilyMmbrs_Age.copy()

# remove first item from new list
first = Big_Happy_Family.pop(0)

# remove last item from new list
last = Big_Happy_Family.pop(-1)

#List5
Younger_Than_4 = [filter(lambda x: x < 4, Big_Happy_Family)]

import math
Big_Happy_Family = [2, 5, 13]
Cubed_Root_Age = list(map(lambda x: x ** (1/3), Big_Happy_Family)) 

Volume_Cube = list(map(lambda x: x**3, Big_Happy_Family))

print(Volume_Cube)

#List6


















