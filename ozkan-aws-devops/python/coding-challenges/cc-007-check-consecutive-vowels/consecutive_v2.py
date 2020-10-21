str = list(input("Please enter a string: ").lower())

vow = ["a", "e", "i", "o", "u"]

lst = [[str[i-1], str[i]] for i in range(1, len(str)) if str[i] in vow if str[i-1] in vow]

print(f"{'Positive'}" * (len(lst)!= 0) + f"{'Negative'}" * (len(lst) == 0))