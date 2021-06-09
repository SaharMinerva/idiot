import pyinputplus as pyip
import re
while True:
    prompt = 'Want to know how to keep an idiot busy for hours?\n'
    response = pyip.inputYesNo(prompt, allowRegexes=[r'(!|.)*'])
    if response == 'no' or response == 'no' + '!' or response == 'no' + '.':
        print('fine!')
        break

