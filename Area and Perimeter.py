# Area and Perimeter
# Author: Jesse Mao
# Date: 2024-10-25
# Version: 1

def valid_num(question):
    while True:
        try:
            response = float(input(question))
            if response > 0:
                return response
            else:
                print("Please enter a valid number above 0")
        except ValueError:
            print("Invalid input. Please enter a number.")


while True:
    print("Perimiter and area calculator")
    width = valid_num("Please enter the width: ")
    length = valid_num("Please eneter the length: ")


# Calculate the area / perimeter
    area = width * length
    perimeter = (width + length) * 2
    print(f"The perimeter is {perimeter} units, and the area is {area} units squared")
    if input("Please press enter to calculate again. Press any other key to quit.\n"):
        break

