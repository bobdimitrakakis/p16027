
#Η ασκηση κανει ακριβως αυτο που ζηταει η εκφωνηση.
#Παίρνει κείμενο απο το randomtext.txt, και μαλιστα τσεκαρει αμα τα γραμματα c,k,r βρισκονται ΔΕΞΙΑ απο το f,
#επειδη το προγραμμα εβγαζε λαθος σε λέξεις οπως το reflect, κατι που δεν προσδιορίζεται απο την εκφώνηση.


text_file= open("randomtext2.txt",'r')
data=text_file.read()
listOfWords = data.split(" ")

#print (listOfWords)
#print (len(listOfWords))

for word in listOfWords:
    bad = 0
    good = 0
    x=0
    for letter in word:
        #print(letter)

        if ((letter == "F" or letter == "f")and x==0):
            x=1
            #print(x)

            continue
        elif ((letter == "C" or letter == "c")and x==1):
            x=2
            #print(x)

            continue
        elif ((letter == "K" or letter == "k")and x==2):
            x=3
            #print(x)
            bad=1
            continue
        elif ((letter == "R" or letter == "r")and x==3):
            bad=1
            continue
        if ((letter == "A") or (letter == "a") or (letter == "E") or (letter == "e") or (letter == "I") or (letter == "i") or (letter == "O") or (letter == "o") or (letter == "U") or (letter == "u") or (letter == "Y") or (letter == "y")):
            #print("its a vowel")
            continue
        else:
            #print("its a consonant")
            good= good+1
        #print("good=",good)
        #print("bad=",bad)
    if good>=bad:
        print (word +"="+ "good")
    else:
        print (word +"="+ "bad")
text_file.close()
