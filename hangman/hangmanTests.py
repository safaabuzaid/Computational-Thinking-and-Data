import string

secretWord = "safaa"
lettersGuessed = ['a','v','m','s']
x = True
for l in secretWord:
    x = x and (l in lettersGuessed)      

result = ""
for l in secretWord:
    if l in lettersGuessed:
        result += l
    else:
        result += "_ "

allLetters = string.ascii_lowercase
availableLetters = ""
for i in allLetters:
    if i not in lettersGuessed:
        availableLetters += i
   
        

print (availableLetters)

