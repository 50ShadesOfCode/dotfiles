import json
import os
import random
from datetime import date

CURRDIR = os.path.dirname(os.path.realpath(__file__))

def loadQuotes():
    with open (f'{CURRDIR}/quotes.json') as f:
        data = json.load(f)
        return data


quotes = loadQuotes().get("quotes")

curr_date = date.today()

random.seed(1)
position = curr_date.day + curr_date.month * 31 + curr_date.year * 365
random.shuffle(quotes)

randomQuote = quotes[position % len(quotes)]

arr = randomQuote.get("text").split(" ")
out_str = ""
char_count = 0
for i in range(len(arr)):
    sub_str = arr[i] + " "
    char_count += len(sub_str)
    if char_count > 40:
        out_str += "\\n" + sub_str
        char_count = len(sub_str)
    else:
        out_str += sub_str
        

print(out_str)
print("~ " + randomQuote.get("author"))
