# LIst is a collections of items. ( element in a specific order)

# ordered 
# mutable
# heteroggeneous => can cotain different types of elements

numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "apple", 3.14, True]

print(mixed[3])
print(fruits[2].title())
message = f"My favourite fruit is {fruits[0].title()}"
print(message)

#append => add element to the end of the list. 

motorcycles = ['honda', 'yamaha',' suzuki ']


#insert  => INSERT element at the specific position.. 
#name.insert(0, 'ducati')

motorcycles.insert(2,'ducatii')

print(motorcycles)

# del = > delete particular item from the list. 
del motorcycles[0]
# pop()  => REMOVE LAST ELEMENT can be used to remvoe the element.



print(len(motorcycles))