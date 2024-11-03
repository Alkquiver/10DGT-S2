# Area and Perimeter
# Author: Jesse Mao
# Date: 2024-10-25
# Version: 3

def valid_num(question): # Testing the user's input, to see is it is a valid number that is larger than 0
    while True:
        try:
            response = float(input(question)) # User's inout
            if response > 0: # If the input is larger than 0
                return response # Continue with the code
            else: # If not
                print("Please enter a valid number above 0") # Print error message 1
        except ValueError: # If input is not a number
            print("Invalid input. Please enter a number.") # Print error message 2


while True:
    print("Perimiter and area calculator")
    width = valid_num("Please enter the width: ") # User's input is saved under width if it is a valid number
    length = valid_num("Please enter the length: ") # User's input is saved under length if it is a valid number


# Calculate the area / perimeter
    area = width * length
    perimeter = (width + length) * 2
    print(f"The perimeter is {perimeter} units, and the area is {area} units squared") # Giving the user the results
    if input("Please press enter to calculate again. Press any other key to quit.\n"): # Gives the user the choice to loop the program
        break

