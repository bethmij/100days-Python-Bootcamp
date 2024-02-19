import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

nato_format_dict = {value.letter: value.code for (key, value) in data.iterrows()}

user_input = input('Enter a word : ').upper()

nato_nam = [nato_format_dict[letter] for letter in user_input]

print(nato_nam)


