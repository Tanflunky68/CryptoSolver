ascii_art = '''
_________                          __           _________        .__                         
\_   ___ \_______  ___.__.______ _/  |_  ____  /   _____/  ____  |  | ___  __  ____ _______  
/    \  \/\_  __ \<   |  |\____ \\   __\/  _ \ \_____  \  /  _ \ |  | \  \/ /_/ __ \\_  __ \ 
\     \____|  | \/ \___  ||  |_> >|  | (  <_> )/        \(  <_> )|  |__\   / \  ___/ |  | \/ 
 \______  /|__|    / ____||   __/ |__|  \____//_______  / \____/ |____/ \_/   \___  >|__|    
        \/         \/     |__|                        \/                          \/         
                                                                                             
'''



#Cryptographic functions
def numbers_to_ascii(input_array):
    ascii_codes = []

    for num in input_array:
        if 0 <= num <= 127:
            ascii_code = chr(num)
            ascii_codes.append(ascii_code)
        else:
            print(f"Input number {num} is out of the valid ASCII range (0-127). Skipping...")

    return ascii_codes


# Define functions for each menu option
def option1():
    print("")
    input_str = input("Enter the array in the format [99, 114, 121, 112, ...]: ")
    
    # Extract numbers from the input string using eval
    try:
        input_array = eval(input_str)
    except (SyntaxError, NameError):
        print("Invalid input format. Please use the format [99, 114, 121, 112, ...]")
        exit()

    ascii_result = numbers_to_ascii(input_array)

    if ascii_result:
        ascii_string = "".join(ascii_result)
        print("")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("ASCII Codes:", ascii_string)
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("")
        print("")

        print("Chose an option")
        print("1. Go back to the main menu")
        print("2. Exit the program") 
        choice = input("Enter your choice: ")      
        if choice == "1":
            main_menu("0")
        elif choice == "2":
            main_menu("Y")


def option2():
    print("You selected Option 2")

def option3():
    print("You selected Option 3")

def option4():
    print("You selected Option 4")

# Define the main menu function
def main_menu(choice):
    if choice is "Y":
        return
    else:
        while True:
            if choice is "Y":
                break

            print(ascii_art)
            print("Main Menu:")
            print("1. Takes an array of numbers and converts them to a string")
            print("2. Hexadecimal to string")
            print("3. Base64 to string")
            print("4. Option 4")
            print("Enter Y to exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                option1()
            elif choice == "2":
                option2()
            elif choice == "3":
                option3()
            elif choice == "4":
                option4()
            elif choice == "Y":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main_menu("0")
