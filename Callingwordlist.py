# calling words from the individual word lists #
# import list
import random
import linecache
    
def CallWordlist(difficulty):
    if difficulty == 1:
        # the difficulty is be chosen in the main game
        wordfile = "wordlist.txt"
        numberoflines = 1
        wordlistother(wordfile,numberoflines)
    elif difficulty == 2:
        wordfile = "wordlist2.txt"
        numberoflines = random.randint(1,2)
        # numberoflines determines the number of phrases to be entered by the user
        wordlistother(wordfile,numberoflines)
    elif difficulty == 3:
        numberoflines = random.randint(1,2)
        filetochoose = random.randint(1,2)
        # filetochoose determins which file is used to select a phrase from
        if filetochoose == 1:
            wordfile = "wordlist2.txt"
            wordlistother(wordfile,numberoflines)
        if filetochoose == 2:
            wordfile = "wordlist3.txt"
            wordlistother(wordfile,numberoflines)

def wordlistother(wordfile,numberoflines):
    count = 0
    with open(wordfile) as infp:
        for line in infp:
            if line.strip():
                count += 1
    # counts the number of lines in the wordlist
    linetoread = random.randint(1,count)
    Tword = ""
    Tword2 = ""
    Tword = linecache.getline(wordfile,linetoread)
    #gets a single line from the wordlist
    Tword = Tword.strip()
    #removes an additional line entered when line from wordlist is called
    if numberoflines == 2:
        #creates another line for the user to enter if the randomiser chooses so
        linetoread2 = random.randint(1,count)
        while linetoread2 == linetoread:
            linetoread2 = random.randint(1,count)
            #checks that the two phrases given arent the same
        Tword2 = linecache.getline(wordfile,linetoread2)
        Tword2 = Tword2.strip()
        printwords(Tword,Tword2)
    elif numberoflines == 1:
        printwords(Tword,Tword2)

def printwords(word,word2):
    globals()['word'] = word
    globals()['word2'] = word2
    #turns the variables into global variables
