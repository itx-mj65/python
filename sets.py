a={2,762,7628,78}
b=set() # empty set write with word set 
# set return repeated values only 1 one time
print(a)
print(type(a))

# add value in set
a.add(1)
print(a)
# remove value from set
a.remove(1)
print(a)

# remove value from set using discard method

a.discard(2)
print(a)

# clear the set

a.clear()
print(a)

# union of two sets

set1={1,2,3,4}
set2={3,4,5,6}
set3=set1.union(set2)
print(set3)

# intersection of two sets

set4={1,2,3,4,5,6}
set5={3,4,5,6,7,8}
set6=set4.intersection(set5)
print(set6)

# difference of two sets
# Returns the elements that are in the first set but not in the second set (or other sets, if provided).

set7={1,2,3,4,5,6}
set8={3,4,5,6,7,8}
set9=set7.difference(set8)
print(set9)

# symmetric difference of two sets
# Returns the elements that are in either of the sets but not in their intersection (i.e., elements unique to each set).
set10={1,2,3,4,5,6}

set11={3,4,5,6,7,8}

set12=set10.symmetric_difference(set11)

print(set12)

# copy method 
# Returns a copy of the set.
# set13={1,2,3,4,5,6}

# set14=set13.copy()
# print(set14)

# isdisjoint()
# Returns True if the set has a null intersection with another set, i.e., if they have the same
# elements, and False otherwise.

# set15={1,2,3,4}
# set16={5,6,7,8}

# print(set15.isdisjoint(set16))

# pop
# Removes and returns an arbitrary element from the set.
# If the set is empty, it raises a KeyError.
# set17={1,2,3,4,5,6}
# set18=set17.pop()
# print(set18)

#intersection
# Returns a new set with elements common to the set and the other set(s) or other iterabl
# e(s).
# set19={1,2,3,4,5,6}
# set20={3,4,5,6,7,8}
# set21=set19.intersection(set20)
# print(set21)

# issubset
# Returns True if all elements of the set are present in the other set, and False otherwise.
# set22={1,2,3,4,5,6}
# set23={1,2,3,4,5,6,7,8}
# print(set22.issubset(set23))
