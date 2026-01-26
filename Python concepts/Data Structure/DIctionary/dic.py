#A mutable mapping from keys -> values , implemented using hash table


# Mapping → relationship, not sequence

# Keys → Values → lookup by meaning, not position

# Mutable → can change over time

# Hash table → extremely fast lookup

# Keys must be:

# Unique

# Hashable

# Immutable

person = {
    "name": "Alice",
    "age": 25,
    "city": "Delhi"
}


d = dict(name="Alice", age=25)
pairs = [("a", 1), ("b", 2)]
d = dict(pairs)
# accessing 

person["name"]
# safe access
person.get("salary")        # None
person.get("salary", 0)     # default

person["age"] = 26
person["salary"] = 50000
# adds if new, else modify
# to delete something 

del person["city"]
person.pop('city')

#mutable objects 
a = {"x": 1}
b = a
b["y"] = 2

print(a)  # {'x': 1, 'y': 2}

