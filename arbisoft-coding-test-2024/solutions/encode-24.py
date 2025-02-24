import sys

def decode_message(key, encoded_message):
    """
    Decodes the encoded message using the key provided and returns the decoded message
    """
    decoded_message = ""
    message_parts = encoded_message.split("0")  # Split on '0' delimiter
    uppercase_next = False  # Flag to check if next character should be uppercase

    for part in message_parts:
        # Empty part indicates the next character is uppercase
        if not part:
            uppercase_next = True
            continue  

        if uppercase_next: 
            uppercase_next = False
            is_uppercase = True
        else:
            is_uppercase = False

        # Extract key index and character index from the encoded part
        key_index = int(part[0]) - 1
        char_index = len(part) - 1

        if key_index < 0 or key_index >= len(key) or char_index < 0 or char_index >= len(key[key_index]):
            return "Error"  # Invalid encoded message

        decoded_char = key[key_index][char_index]  # Retrieve character from key

        if is_uppercase:
            decoded_char = decoded_char.upper()
            
        decoded_message += decoded_char

    return decoded_message


def encode_char(key, char):
    """
    Encodes a single character using the key provided
    """
    encoded_char = ""
    if char.isupper():
        encoded_char += "0"
    char = char.lower()
    key_index = 0
    char_index = 0
    for index, word in enumerate(key):
        if char in word:
            key_index = index + 1
            char_index = word.index(char) + 1
            break
    if key_index == 0:
        return None
    else:
        encoded_char += str(key_index) * char_index + "0"
        return encoded_char


def encode_message(key, message):
    """
    Encodes the message using the key provided and returns the encoded message
    """
    encoded_message = ""
    for char in message:
        encoded_char = encode_char(key, char)
        if encoded_char is None:
            return "Error"
        else:
            encoded_message += encoded_char
    return encoded_message


if __name__ == "__main__":
    with open(sys.argv[1], "r") as file:
        key = file.readline().strip().split(",")
        # Convert input to list of strings
        for i in range(0, len(key)):
            key[i] = key[i].strip().replace('"', "").lower()
        operation = int(file.readline().strip())
        message = file.readline().strip()
    if operation == 1:
        print(encode_message(key, message))
    elif operation == 2:
        print(decode_message(key, message))
    else:
        print("Error")
