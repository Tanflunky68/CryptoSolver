# This script is to convert numbers from an array into ASCII characters

def numbers_to_ascii(input_array):
    ascii_codes = []

    for num in input_array:
        if 0 <= num <= 127:
            ascii_code = chr(num)
            ascii_codes.append(ascii_code)
        else:
            print(f"Input number {num} is out of the valid ASCII range (0-127). Skipping...")

    return ascii_codes

if __name__ == "__main__":
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
        print("ASCII Codes:", ascii_string)
