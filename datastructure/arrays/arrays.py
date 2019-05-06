numbers = [10,20,30,400,50,60]

#Print at index:
print("Print at index:")
print(numbers[0])
print(numbers[4])

# Print all elements:
print("Print all elements:")
print(numbers)
print(numbers[:])

print("Print from index 0 to 2:")
print(numbers[0:2])

print("Print last but 2:")
print(numbers[:-2])

print('Print from index 1:')
print(numbers[1:]) 


#Iterate all elements
print("Iterate all elements:")
for num in numbers:
    print(num)

# Other way of printing
print("Iterate all elements:")
for i in range(len(numbers)):
    print(numbers[i])

#Assign a value:
print("Assign a value:")
numbers[1] = 200
print(numbers[1])

print("Assign a value of different typr in same array:")
numbers[2] = 'Adam'
print(numbers[2])

numbers[2] = 30

#Print largest number

largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

print("Largest number:")
print(largest)




