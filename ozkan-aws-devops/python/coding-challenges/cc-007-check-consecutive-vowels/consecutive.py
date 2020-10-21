# Python Challange / cc-007-check-consecutive-vowels
string = list(input("Please enter a string: ").lower())
vowels = ["a", "e", "i", "o", "u"]
lst = []

for i in range(1, len(string)):
    if string[i] in vowels:
        if string[i-1] in vowels:
            lst.append([string[i-1], string[i]])
 
if len(lst)!= 0:
    print("Positive")
else:
    print("Negative")