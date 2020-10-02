# https://www.facebook.com/harsith.gayle.1/posts/2784315391846205
# Subscribed by Code House

import random  #importing random module
wordlist=[] #creating a list to store data
special_char =["!","@","$","#","^","-","*","&"]
with open("words.txt", 'r') as file: #opening text file
    opens = file.readlines()  #read the lines in file
    
    for lines in opens: 
        line = lines.split() #splitting the lines
        
        for word in line:
            if len(word) >5: #selecting the words in the file
                wordlist.append(word.capitalize())   #adding the words to the list

first = random.choice(wordlist)   #this helps to pick a word randomly
second = str(random.randrange(10,99))   #this helps to pick a random number
third = random.choice(special_char)   #this helps to pick a random character
print(first+second+third)   #displaying the password
