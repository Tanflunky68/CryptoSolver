def hex_to_string(hex_value):
    try:
        # Remove any leading "0x" if present
        hex_value = hex_value.lstrip("0x")
        
        # Convert the hexadecimal string to bytes and then decode it as a string
        decoded_string = bytes.fromhex(hex_value).decode('utf-8')
        return decoded_string
    except ValueError:
        return "Invalid hexadecimal input"

if __name__ == "__main__":
    hex_value = input("Enter a hex value: ")
    result = hex_to_string(hex_value)
    print("Decoded String:", result)
