ascii_art = '''
_________                          __           _________        .__                         
\_   ___ \_______  ___.__.______ _/  |_  ____  /   _____/  ____  |  | ___  __  ____ _______  
/    \  \/\_  __ \<   |  |\____ \\   __\/  _ \ \_____  \  /  _ \ |  | \  \/ /_/ __ \\_  __ \ 
\     \____|  | \/ \___  ||  |_> >|  | (  <_> )/        \(  <_> )|  |__\   / \  ___/ |  | \/ 
 \______  /|__|    / ____||   __/ |__|  \____//_______  / \____/ |____/ \_/   \___  >|__|    
        \/         \/     |__|                        \/                          \/         
                                                                                             
'''

print(ascii_art)




# Define functions for each menu option
def option1():
    print("You selected Option 1")
	input_str = input("Enter the array in the format [99, 114, 121, 112, ...]: ")




def option2():
    print("You selected Option 2")

def option3():
    print("You selected Option 3")

def option4():
    print("You selected Option 4")

# Define the main menu function
def main_menu():
    while True:
        print("Main Menu:")
        print("1. Takes an array of numbers and converts them to a string")
        print("2. Hexadecimal to string")
        print("3. Base64 to string")
        print("4. Option 4")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            option1()
        elif choice == "2":
            option2()
        elif choice == "3":
            option3()
        elif choice == "4":
            option4()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main_menu()
