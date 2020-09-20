# The largest Number of a list with 5 elements.

lst = list()

for i in range(5):
    lst.append(int(input("Enter a number: ")))

largest_number = lst[0]

for j in lst:
    if j > largest_number:
        largest_number = j

print("The largest number: ", largest_number)
