# using the json library to bring the data to the dictionary app, serves as a medium 
# for data combined with python
import json 
from difflib import get_close_matches # auto-correct and auto-fill like functionality

data = json.load(open('076 data.json')) # the definitions are loaded on the json file
 
# a function that helps deal with the data
def definition(w):
    w = w.lower() # transform any input arg into lowercase
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()] 
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0: # if there's an entry of a word greater than 0 in length
        resp = input("Did you mean %s instead ? Enter Y if yes , N if no " % get_close_matches(w, data.keys())[0]) # grab the 1st one on that list of dict keys and use it in this sentence 
        if resp == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif resp == "N":
            return "Could not find the word you are looking for. Try checking your spelling."
        else:
            return "Incorrect entry. Try avoiding wrong or excess entries. Respond with what is required."    
    else:
        return "Word does not exist. Try again and pay attention to your spelling."

word = input("Enter a word: ")


# I want to show the results of the return value using the print function
# I also want to display a user friendly output to the user, instead of a list of definitions
output = definition(word)

if type(output) == list: # for when the entered word has more than one definition
        for definitions in output:
            print(definitions)
else: # to avoid the irregularity of looped through letters for single definition terms
    print(output)
