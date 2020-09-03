'''
This program finds the largest number by user input.
The user inputs a number until a negative number is entered.
'''

num_int = int(input("Input a number: "))    # Do not change this line
max_int = num_int + 1

for i in range(0, max_int):

    num_int = int(input("Input a number: "))

    if num_int >= 0:
        continue


    if num_int < 0:
        print("The maximum is", max_int)    # Do not change this line
