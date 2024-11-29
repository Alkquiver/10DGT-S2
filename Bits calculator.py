# Bits calculator
# Author: Jesse Mao
# Date: 2024-11-18
# Version: 1

def valid_num(question):
    while True:
        try:
            response = float(input(question))
            if response >= 0:
                return response
            else: 
                print("Please enter a valid number above 0.")
        except ValueError:
            print("Invalid input. Please enter a number")

def valid_pixel(question):
    while True:
        try:
            response = int(input(question))
            if response > 0:
                return response
            else: 
                print("Please enter a valid whole number above 0.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

print("Bits calculator")
selection = None
while True:
    User_input = input("Please select whether you would like to convert text, image or number to bits.\n").lower()
    if User_input == "text" or User_input == "t":
        print("You chose to convert text into bits.")
        selection = 1
    if User_input == "image" or User_input == "i":
        print("You chose to convert an image into bits.")
        selection = 2
    if User_input == "number" or User_input == "num" or User_input == "n":
        print("You chose to convert a number into bits.")
        selection = 3
    if selection is None:
        print("Invalid input. Please enter 'text' for text, 'image' for image and 'number' for number.")
        continue

    if selection is not None:
        if selection == 3:
            user_num = int(float(valid_num("Please enter your number:\n")))
            binary_representation = bin(user_num)[2:]
            bits = (len(binary_representation))
            print(f"The number {user_num} in binary form is {binary_representation}. {bits} bits are required to represent {user_num}")

        elif  selection == 1:
            user_text = input("Please enter your text\n")
            bits = (len(user_text)) *8
            print(f"The text: {user_text} requires {bits} bits.")

        elif selection == 2:
            pixel_height = int(valid_pixel("Please enter the height of your image in pixels\n"))
            pixel_width = int(valid_pixel("Please enter the width of your image in pixels.\n"))
            bits = (pixel_height * pixel_width) * 24
            kilobytes = bits/8000
            print(f"Your image is represented with {bits} bits/ {kilobytes} kilobytes")    

    if input("Please press enter to calculate again. Press any other key to quit.\n"): # Gives the user the choice to loop the program
        break