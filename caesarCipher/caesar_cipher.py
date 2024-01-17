logo = '''                                                                                                                               

                                                                                     _/            _/                            
    _/_/_/    _/_/_/    _/_/      _/_/_/    _/_/_/  _/  _/_/                _/_/_/      _/_/_/    _/_/_/      _/_/    _/  _/_/   
 _/        _/    _/  _/_/_/_/  _/_/      _/    _/  _/_/                  _/        _/  _/    _/  _/    _/  _/_/_/_/  _/_/        
_/        _/    _/  _/            _/_/  _/    _/  _/                    _/        _/  _/    _/  _/    _/  _/        _/           
 _/_/_/    _/_/_/    _/_/_/  _/_/_/      _/_/_/  _/                      _/_/_/  _/  _/_/_/    _/    _/    _/_/_/  _/            
                                                                                    _/                                           
                                                                                   _/                                        '''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

isEnd = False


def encode(user_text, shift_count):
    encoded_word = ""
    for letter in user_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            new_index = index + shift_count
            if new_index > len(alphabet):
                new_index = shift_count - (len(alphabet) - index)
            encoded_word += alphabet[new_index]
        else:
            encoded_word += letter
    print(f"Here's the encoded result : {encoded_word}")


def decode(user_text, shift_count):
    decoded_word = ""
    for letter in user_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            new_index = index - shift_count
            if new_index < 0:
                new_index = len(alphabet) - (shift_count - index)
            decoded_word += alphabet[new_index]
        else:
            decoded_word += letter
    print(f"Here's the decoded result : {decoded_word}")


while not isEnd:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    if direction.lower() == "encode":
        encode(text, shift)

    elif direction.lower() == "decode":
        decode(text, shift)

    else:
        print("Invalid Input!")

    choice = input("Type 'yes' if you want to do again.Otherwise type 'no' : ")

    if choice.lower() == "no" or choice.lower() != "yes":
        isEnd = True


