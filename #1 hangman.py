import random
wordlist = ["HOLIDAY","ABBYSS","ABRUPTLY","ABSURD","JANUARY","FEBRUARY","MARCH","APRIL","AUGUST","SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER"]
word = random.choice(wordlist)
# trycount -- mistake counter
trycount = 0
allowed = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# tempword -- holding the guessed letter + underscores
tempword = []
# madeguess -- holding the letters that already guessed
madeguess = ""

# loop for creating a tempword that starts with all underscores
for i in range(0,len(word)):
    tempword.append("_")

# Intro
print("Hello! Welcome to Hangman game!")
print("\u001b[31mPlease enter your name: \u001b[32m")
name = input()
name = name.upper()
print(f"\u001b[34mHello {name}!")
   
hang = [" ","""\u001b[32m
_______________________
:::
:::
:::
:::
+++++:
+++++:

""","""\u001b[32m
_______________________
:::         
:::
:::
:::           \u001b[33m/ \ \u001b[32m
+++++:
+++++:""","""\u001b[32m
_______________________
:::           
:::           
:::           \u001b[33m/:\ \u001b[32m
:::           \u001b[33m/ \ \u001b[32m  
+++++:
+++++:""","""\u001b[32m
_______________________
:::           
:::            \u001b[33mO
:::           \u001b[33m/:\ \u001b[32m 
:::           \u001b[33m/ \ \u001b[32m
+++++:
+++++:
""","""\u001b[32m
_______________________
:::            :
:::            \u001b[33mO \u001b[32m
:::           \u001b[33m/:\ \u001b[32m         
:::           \u001b[33m/ \ \u001b[32m
+++++:
+++++:
"""]

# converting a list into a word
guessword = " ".join(tempword)

print("")
print(f"\u001b[37mPlease guess this word\u001b[33m {guessword}")

while trycount < 5:
    lives = 5 - trycount
    print("")
    
    if trycount == 4:
        print("Oh no last one! please don't make a mistake!") 
    else:
        print(f"\u001b[31mYou have {lives} lives ramaining {name}.") 
    
    guess = input("\u001b[37mGuess a letter:\u001b[32m ")
    guess = guess.upper()
    counter = 0

    # validating an input
    while not guess in allowed:
        print(guess,"\u001b[31mis not a valid entry")
        print("please input a valid entry.")
        guess = input("\u001b[37mGuess a letter:\u001b[32m ")
        guess = guess.upper()
    
    # checking if the input is not repeating
    while guess in madeguess:
        print("\u001b[31mYou have already guessed that letter\u001b[32m", guess)
        guess = input()
        guess = guess.upper()
    
    madeguess = madeguess + guess
    
    # putting the guess word into the list tempword
    for i in range(0,len(word)):
        if guess == word[i]:
            tempword[i] = guess
            counter = 1
    
    # checking if word is answered already
    j = 0
    for i in range(0,len(guessword)):
        if guessword[i] != " ":
            if tempword[j] == "_":
                stop = 0
                break
            else:
                stop = 1
            j = j + 1
    
    # stopping the program if the word is already answered
    if stop == 1:
        word = "".join(tempword)
        print(f"\u001b[37mThe word is\u001b[32m {word}\n\n\n\n\n")
        print("\n\u001b[35mCongratulations! You guessed the word.")
        print("\nGame Over!")
        break

    # wrong guess; counter = 0
    # correct guess; counter = 1
    # returning the error counted if the answer is correct 
    if counter == 1:
        trycount = trycount - 1
    
    # error counter
    trycount = trycount + 1
    
    # end loop display
    guessword = " ".join(tempword)
    print(f"\u001b[33m{guessword}")
    print(hang[trycount])    
    
    # if the player failed to answer within 5 tries
    if trycount == 5:     
        print("\u001b[31mGame Over!")     
        print(f"\u001b[37mThe answer is\u001b[32m {word}.")      
        print("\n\u001b[34mThank you for playing!")
    