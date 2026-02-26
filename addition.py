def get_number(num_var):
    while True:
        try:
            print(f"{num_var}")
            number = int(input())
            return number
            break
        except ValueError:
            print("Sorry, your input isn't a number, please try again")

number1 = get_number('Number1')
number2 = get_number('Number2')
result = number1 + number2
print(f"The result is {result}")


"""First Solution"""
#print(f"This is a simple program that adds 2 numbers. Please enter 2 random numbers")
#
#while True:
#    try:
#        print(f"Number 1:")
#        number1 = int(input())
#        break
#    except ValueError:
#        print(f"Sorry, your input isn't a number")    
#
#while True:
#    try:
#        print(f"Number 2:")
#        number2 = int(input())
#        break
#    except ValueError:
#        print(f"Sorry, your input isn't a number")    
#
#result = number1 + number2
#print(f"The result is {result}")
#