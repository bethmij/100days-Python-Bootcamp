import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
isEnd = False


def caesar(u_direction, u_text, u_shift):
    new_word = ""
    for letter in u_text:
        if letter in alphabet:
            index = alphabet.index(letter)

            if u_direction.lower() == "encode":
                new_index = index + u_shift
                if new_index > len(alphabet):
                    new_index = u_shift - (len(alphabet) - index)
                new_word += alphabet[new_index]

            elif u_direction.lower() == "decode":
                new_index = index - u_shift
                if new_index < 0:
                    new_index = len(alphabet) - (u_shift - index)
                new_word += alphabet[new_index]

            else:
                print("Invalid Input!")
        else:
            new_word += letter
    print(f"Here's the {direction} result : {new_word}")


while not isEnd:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    shift = shift % 26
    caesar(direction, text, shift)

    choice = input("Type 'yes' if you want to do again.Otherwise type 'no' : ")

    if choice.lower() == "no" or choice.lower() != "yes":
        isEnd = True
