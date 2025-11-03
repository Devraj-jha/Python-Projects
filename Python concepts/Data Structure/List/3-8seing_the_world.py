# “Seeing the World: Think of at least five places in the world you’d like to visit.

# Store the locations in a list. Make sure the list is not in alphabetical order.
# Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
# Use sorted() to print your list in alphabetical order without modifying the actual list.
# Show that your list is still in its original order by printing it.



places = ['kashi', 'mathura', 'vridavan', 'himalaya', 'swiss']
print(places)
print(sorted(places))
print(places)
#“Use sorted() to print your list in reverse-alphabetical order without changing the order”

print(sorted(places,reverse=True))
# “Use reverse() to change the order of your list. Print the list to show that its order has changed.
# Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.”


places.reverse()
print(places)
places.reverse()
print(places)
