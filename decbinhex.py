# random number generation
import random

# define converter functions
def dec_to_bin(rand_num):
    return format(rand_num, '08b') # always in XXXXXXXX format (8 characters)

def dec_to_hex(rand_num):
    return format(rand_num, '02X') # always in XX format (2 characters)

def bin_to_dec(bin_num):
    return int(bin_num, 2)

def bin_to_hex(bin_num):
    return format(int(bin_num, 2), '02X')

def hex_to_dec(hex_num):
    return int(hex_num, 16)

def hex_to_bin(hex_num):
    return format(int(hex_num, 16), '08b')

# decimal to binary game
def dec_to_bin_game():
    total = 0
    while True:
        rand_num = random.randint(0, 255)
        bin_num = dec_to_bin(rand_num)
        user_num = ""

        while (user_num != bin_num):
            print("Decimal number: " + str(rand_num) + "\nlength: 8")
            user_num = input("Enter number in binary: ")
            if user_num.casefold() == "exit":
                main_menu()
        print(bin_num)
        total += 1
        print("Correct! Total correct: " + str(total))

# decimal to hex game
def dec_to_hex_game():
    total = 0
    while True:
        rand_num = random.randint(0, 255)
        hex_num = dec_to_hex(rand_num)
        user_num = ""
    
        while user_num != hex_num:
            print("Decimal: " + str(rand_num))
            user_num = input("Enter in hex: ").upper()
            if user_num.casefold() == "exit":
                main_menu()
        print(hex_num)
        total += 1
        print("Correct! Total correct: " + str(total))

# binary to decimal game
def bin_to_dec_game():
    total = 0
    while True:
        rand_num = random.randint(0, 255)
        bin_num = dec_to_bin(rand_num)
        user_num = ""

        while user_num != str(rand_num):
            print("Binary: " + str(bin_num))
            user_num = input("Enter in decimal: ")
            if user_num.casefold() == "exit":
                main_menu()
        print(rand_num)
        total += 1
        print("Correct! Total correct: " + str(total))

# binary to hex game
def bin_to_hex_game():
    total = 0
    while True:
        bin_num = dec_to_bin(random.randint(0, 255))
        hex_num = bin_to_hex(bin_num)
        user_num = ""

        while user_num != hex_num:
            print("Binary: " + str(bin_num))
            user_num = input("Enter in hex: ")
            if user_num.casefold() == "exit":
                main_menu()
        print(hex_num)
        total += 1
        print("Correct! Total correct: " + str(total))

# hex to decimal game
def hex_to_dec_game():
    total = 0
    while True:
        rand_num = random.randint(0, 255)
        hex_num = dec_to_hex(rand_num)
        user_num = ""

        while user_num != str(rand_num):
            print("Hex: " + hex_num)
            user_num = input("Enter in decimal: ")
            if user_num.casefold() == "exit":
                main_menu()
        print(rand_num)
        total += 1
        print("Correct! Total correct: " + str(total))

# hex to binary game
def hex_to_bin_game():
    total = 0
    while True:
        hex_num = dec_to_hex(random.randint(0, 255))
        bin_num = hex_to_bin(hex_num)
        user_num = ""

        while user_num != bin_num:
            print("Hex: " + hex_num)
            user_num = input("Enter in binary: ")
            if user_num.casefold() == "exit":
                main_menu()
        print(bin_num)
        total += 1
        print("Correct! Total correct: " + str(total))
        
# main menu
def main_menu():
    print("1. Decimal to binary\n2. Decimal to hex\n3. Binary to decimal\n4. Binary to hex\n5. Hex to decimal\n6. Hex to binary")
    menu = input("Select a game: ")
    if menu == "1":
        dec_to_bin_game()
    elif menu == "2":
        dec_to_hex_game()
    elif menu == "3":
        bin_to_dec_game()
    elif menu == "4":
        bin_to_hex_game()
    elif menu == "5":
        hex_to_dec_game()
    elif menu == "6":
        hex_to_bin_game()
    else:
        print("Invalid number. Please try again.")
        main_menu()

# start program
print("Type exit at any time during a game to quit to main menu.")
main_menu()
