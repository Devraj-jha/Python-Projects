# for loop 



for i in range(1,4):
    print(i )

 # Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#while loop 
count = 0
while count < 5:
    print("Count:", count)
    count += 1  # important to avoid infinite loop
# contiune = skips , break = exit the loop there  

for i in range(1, 6):
    if i == 3:
        continue  # skip 3
    print(i)

for i in range(1, 6):
    if i == 5:
        break  # exit loop at 4
    print(i)
