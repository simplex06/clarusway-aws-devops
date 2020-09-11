# This code converts milliseconds into hours, minutes, and seconds.

while True:
        
    num = input('''###  This program converts milliseconds into hours, minutes, and seconds ###
(To exit the program, please type "exit")
Please enter the milliseconds (should be greater than zero) : ''')

    if num == 'exit':
        print("Exiting the program... Good Bye")
        break

    elif num.isalpha():
        print("Not Valid Input !!!")
        continue
       
    elif num.isnumeric() :
        num = int(num)

        if num < 1:
            print("Not Valid Input !!!")
            continue

        elif num > 0:
            hour = num // (1000*60*60)
            minute = (num - hour * (1000*60*60)) // (1000*60)
            sec = (num - hour * (1000*60*60) - minute * (1000*60)) // (1000)
            print(f'{hour} hour/s'*(hour != 0) + f' {minute} minute/s'*(minute != 0) + f' {sec} second/s' *(sec != 0) or f'just {num} millisecond/s' * (num < 1000))

        

        

