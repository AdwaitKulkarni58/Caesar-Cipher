alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from logo import logo
print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text, shift, direction):
    newText = ""
    if direction == "decode":
        shift = -1 * shift
    for letter in text:
        currLetterIndex = alphabet.index(letter)
        newLetterIndex = currLetterIndex + shift
        newLetter = alphabet[newLetterIndex]
        newText += newLetter
    print(f"The text is {newText}.")
caesar(text, shift, direction)