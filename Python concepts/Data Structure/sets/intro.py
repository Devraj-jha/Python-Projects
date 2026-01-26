# set => unordered mutable collections of unique, hashable ojects

#Unordered → no index, no position

# Mutable → can add/remove elements

# Unique → duplicates are impossible

# Hashable → elements must be immutable

s = {1,2,3}
s = {}       # dictionary
s = set()    #  empty set


## automatically removes the duplicates

s = set([1, 2, 2, 3])
print(s)  # {1, 2, 3}

print(hash("hello"))
print(hash("hello"))

#if somethign can change it can not be a set element

# like list or dicnoary

