def caesar(user_input, shift):
    encrypted = ""
    for ch in user_input:
        keep_alphabet = ord(ch) + shift
        lastletter = chr(keep_alphabet)
        encrypted += lastletter
    print(f"Your encrypted word is: {encrypted}")


message = input("tell me your message to encrypt: ")
caesar(message, 3)
