text_file= open("randomtext5.txt",'r')
data=text_file.read()
listOfWords = data.split(" ")
finaltext=[]
finaltextstr=""
for word in listOfWords:
    if len(word)>3:
        endlist=[]
        temp1=""
        temp=word[0]
        templist=list(word)
        templist[0]=""
        word="".join(templist)
        word=word+temp+"ay"
        for letter in word:
            if letter==":":
                temp=word.index(":")
                templist=list(word)
                templist[temp]=""
                word="".join(templist)
                temp1=":"
                word=word+temp1
            if letter==",":
                temp=word.index(",")
                templist=list(word)
                templist[temp]=""
                word="".join(templist)
                temp1=","
                word=word+temp1
            if letter==".":
                temp=word.index(".")
                templist=list(word)
                #endlist.append(templist[temp])
                templist[temp]=""
                word="".join(templist)
                temp1="."
                word=word+temp1
            if letter=="?":
                temp=word.index("?")
                templist=list(word)
                templist[temp]=""
                word="".join(templist)
                temp1="?"
                word=word+temp1
            if letter=="!":
                temp=word.index("!")
                templist=list(word)
                templist[temp]=""
                word="".join(templist)
                temp1="!"
                word=word+temp1



        #templist.append(endlist)
        #word="".join(templist)

        #print(word)
    finaltext.append(word)

for i in finaltext:
    finaltextstr=finaltextstr+i+" "

print(finaltextstr)
