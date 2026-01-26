# list is ordered mutable collection of references

# ordered => has specific order
# mutable => can change afterwards
# can hold multiple items
# gives refrecnces to objects
nums = [1, 2, 3]
names = ["Alice", "Bob"]
mixed = [1, "hello", 3.5, True]

#can have multiple data types together

## differnet method to use list

chars = list('ehllo') # h,e , l , l , 0
nums = list(range(5))        # [0, 1, 2, 3, 4]
nums = list(range(1, 10, 2)) # [1, 3, 5, 7, 9]

#indexing 
nums = [10, 20, 30, 40]

nums[0]  # 10
nums[1]  # 20
nums[-1] # 40
nums[-2] # 30
