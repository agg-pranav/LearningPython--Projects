arr = list()
# No of integersin list
n = int(input('No of integers to be added in the array: '))

# Inputting n values of list
for i in range(n):
    arr.append(int(input()))

# Two value sum (target)
target = int(input("Enter the Sum value(target) : "))

# Finding Indices whose sum equals Target
for i in range(n-1):
    for j in range(i+1, n):
        if i + j == target:
            print(arr.index(i), ' ', arr.index(j), '\n')
        else:
            print("No indices found\n")
