import pandas


# data = pandas.read_csv('nato_phonetic_alphabet.csv')
#
# nato_format_dict = {value.letter: value.code for (key, value) in data.iterrows()}
#
# user_input = input('Enter a word : ').upper()
#
# nato_nam = [nato_format_dict[letter] for letter in user_input]
#
# data = [23,432,34,'fgfg',324,True]
#
# print(data)

def add(*args):
    return sum(args)


total = add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(total)
