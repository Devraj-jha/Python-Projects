#ordered collection of items.
#An ordered, immutable collection of object references

t = 1,2,3
print(t)
q1 = (1,2,3,4)
print(q1)

#empty
t = ()
point = (10, 20)
x, y = point
#left side destructres the tuple

a = 10
b = 20

a,b = b,a

a, *rest = (1, 2, 3, 4)
# \Result:

# a = 1

# rest = [2, 3, 4]