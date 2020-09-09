# This code converts milliseconds into hours, minutes, and seconds.

while True:
        
    num = input('''###  This program converts milliseconds into hours, minutes, and seconds ###
(To exit the program, please type "exit")
Please enter the milliseconds (should be greater than zero) : ''')

    if num == 'exit':
        print("Goodbye")
        break

       
    elif num.isnumeric() :
        num = int(num)

        if num < 1:
            print("Enter a number greater than zero: ")
            continue

        elif num > 0:
            hour = num // (1000*60*60)
            minute = (num - hour * (1000*60*60)) // (1000*60)
            sec = (num - hour * (1000*60*60) - minute * (1000*60)) // (1000)
            print(f"{hour} hour/s {minute} minute/s {sec} second/s")

    else:
        print("Please enter a number")
        continue

        

