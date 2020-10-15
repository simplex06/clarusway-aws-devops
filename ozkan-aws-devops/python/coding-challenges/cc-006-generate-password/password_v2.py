name = input("Please enter your full name: ").lower().replace(" ", "")

import random
n = str(random.randint(1000, 10000))
random_letter = random.sample(name, 3)
   
password = ''.join(random_letter) + n

print(password)
