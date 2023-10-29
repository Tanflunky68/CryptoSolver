import base64


ascii_art = '''
_________                          __           _________        .__                         
\_   ___ \_______  ___.__.______ _/  |_  ____  /   _____/  ____  |  | ___  __  ____ _______  
/    \  \/\_  __ \<   |  |\____ \\   __\/  _ \ \_____  \  /  _ \ |  | \  \/ /_/ __ \\_  __ \ 
\     \____|  | \/ \___  ||  |_> >|  | (  <_> )/        \(  <_> )|  |__\   / \  ___/ |  | \/ 
 \______  /|__|    / ____||   __/ |__|  \____//_______  / \____/ |____/ \_/   \___  >|__|    
        \/         \/     |__|                        \/                          \/         
                                                                                             
'''

#Cryptographic functions
def numbers_to_ascii():
    ascii_codes = []
    result_string = ""
    input_str = input("Enter the array in the format [99, 114, 121, 112, ...]: ")
    
    # Extract numbers from the input string using eval
    try:
        input_array = eval(input_str)
    except (SyntaxError, NameError):
        print("Invalid input format. Please use the format [99, 114, 121, 112, ...]")
        exit()

    for num in input_array:
        if 0 <= num <= 127:
            ascii_code = chr(num)
            ascii_codes.append(ascii_code)
        else:
            print(f"Input number {num} is out of the valid ASCII range (0-127). Skipping...")
    print("")

    for value in ascii_codes:
        result_string += str(value)

    if input_array:
        print_result_pretty(result_string)



def hex_to_base64():
    hex_value = input("Enter a hex value: ")
    base64_string = ""
    decoded_bytes = ""
    
    try:
        # Convert the hexadecimal string to bytes and then decode it as a string
        decoded_bytes = bytes.fromhex(hex_value)
        base64_string = base64.b64encode(decoded_bytes).decode('utf-8')

        print(base64_string)
        print_result_pretty(base64_string) 
    except ValueError:
        return "Invalid hexadecimal input"
    




#Commun functions used after every cryptographic process
def write_result_file(result):
    # Define the file path and name
    file_path = "CryptoSolver_results.txt"

    # Open the file in write mode ('w')
    with open(file_path, 'w') as file:
        file.write(result)

def print_result_pretty(result):
        print("")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("ASCII Codes:", result)
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("")
        print("")
        write_result_file(result)

        print("Chose an option")
        print("1. Go back to the main menu")
        print("2. Exit the program") 
        choice = input("Enter your choice: ")      
        if choice == "1":
            main_menu("0")



# Define the main menu function
def main_menu(choice):

    if choice is "Y":
        print(choice)
    else:
        while True:
            if choice is "Y":
                break
            else:    
                print(ascii_art)
                print("Main Menu:")
                print("1. Takes an array of numbers and converts them to a string")
                print("2. Hexadecimal to Base64")
                print("Enter Y to exit")

                choice = input("Enter your choice: ")

                if choice == "1":
                    numbers_to_ascii()
                    break
                elif choice == "2":
                    hex_to_base64()
                    break
                elif choice == "3":
                    break
                elif choice == "4":
                    break
                elif choice == "Y":
                    print("Exiting the program. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please select a valid option.")



if __name__ == "__main__":
    main_menu("0")
