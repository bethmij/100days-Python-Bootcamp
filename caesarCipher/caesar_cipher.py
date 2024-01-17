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
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))
isEnd = False

while not isEnd:
    if direction.lower() == "encode":
        encoded_word = ""

        for letter in text:
            index = alphabet.index(letter)
            encoded_word += alphabet[index + shift]

        print(f"Here's the encoded result : {encoded_word}")

    elif direction.lower() == "decode":
        decoded_word = ""

        for letter in text:
            index = alphabet.index(letter)
            decoded_word += alphabet[index - shift]

        print(f"Here's the decoded result : {decoded_word}")

    else:
        print("Invalid Input!")

    choice = input("Type 'yes' if you want to do again.Otherwise type 'no'")

    if choice.lower() == "no" or choice.lower() != "yes":
        isEnd = True
