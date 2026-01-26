nums = [0, 1, 2, 3, 4, 5]

nums[1:4]     # [1, 2, 3]
nums[:3]      # [0, 1, 2]
nums[3:]     # [3, 4, 5]
nums[:]      #full
nums[::2]   # [0, 2, 4]
nums[::-1]   # reversed list

# [start : stop : step]
# stop is NOT included

nums = [1, 2, 3]
nums[0] = 100
print(nums)  # [100, 2, 3]
#list can be modified in place 

# integer creates a new object itself.

