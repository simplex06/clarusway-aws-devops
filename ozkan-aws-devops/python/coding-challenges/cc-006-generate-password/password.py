name = input("Please enter your full name: ").lower().replace(" ", "")

p_lst = []

import random
n = str(random.randint(1000, 10000))

for i in range(3):
    random_letter = random.choice(name)
    p_lst.append(random_letter)

password = ''.join(p_lst) + n

print(password)
