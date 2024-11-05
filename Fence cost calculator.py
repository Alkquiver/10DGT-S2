# Fence cost calculator
# Author: Jesse Mao
# Date: 2024-10-31
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
    print("Fence cost calculator")
    width = valid_num("Please enter the width of the area you want to fence: ") # User's input is saved under width if it is a valid number
    length = valid_num("Please enter the length of the area you want to fence: ") # User's input is saved under length if it is a valid number
    cost_per_m = valid_num("Please enter the cost for each metre of fencing: ") # User's input is saved under cost_per_m if it is a valid number

# Calculate the cost of the fence
    perimeter = (length + width) * 2 # Calculating the perimeter
    fence_cost = perimeter * cost_per_m # Calculating the cost of the fence
    rounded_fence_cost = round(fence_cost, 2) # Rounding the fence cost to the nearest cent
    print(f"Your area has a perimeter of {perimeter}m, and will cost ${rounded_fence_cost} to fence. ") # Giving the user the results
    if input("Please press enter to calculate again. Press any other key to quit.\n"): # Gives the user the choice to loop the program
        break