alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(text, shifts):
    newText = ""
    for letter in text:
        currLetterIndex = alphabet.index(letter)
        newLetterIndex = currLetterIndex + shifts
        newLetter = alphabet[newLetterIndex]
        newText += newLetter
    print(f"The encoded text is {newText}.")    

def decrypt(text, shifts):
    newText = ""
    for letter in text:
        currLetterIndex = alphabet.index(letter)
        newLetterIndex = currLetterIndex - shifts
        newLetter = alphabet[newLetterIndex]
        newText += newLetter
    print(f"The decoded text is {newText}.")

if direction == "encode":
    encrypt(text, shift)
if direction == "decode":
    decrypt(text, shift)