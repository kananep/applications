import json
from difflib import get_close_matches

data = json.load(open('c:/Users/toy/Desktop/appdevelopment/dictionary/dictwords.json'))

def dictionary(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif get_close_matches(word, data.keys()):
        YesNo = input("Did you mean %s instead? Enter Y if Yes or N if No. \nY or N : " % get_close_matches(word, data.keys())[0])
        if YesNo == 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif YesNo =='N':
            return 'Word not Found . Please Double Check it'
        else:
            return 'We Didnt Understand Your Query'
    else:
        return 'Word not Found'
word = input('Enter Word:')

output = dictionary(word)

if type(output) == list:
   for i in output:
       print(i)

else:
    print(output)       