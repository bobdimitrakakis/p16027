def sumIntervals(nums):

    fin=len(nums)
    rangelist=[]
    max=0
    zevgos=0
    while zevgos<fin:
        y=int(nums[zevgos][1])
        if y>max:
            max=y
        zevgos=zevgos+1

    #print(max)

    z=0
    while (z < max):
        rangelist.append("a")
        z=z+1
    #print (rangelist)

    x=0
    y=0
    zevgos=0
    while zevgos<fin:
        x=int(nums[zevgos][0])
        y=int(nums[zevgos][1])
        #print ("x= ",x)
        #print ("y= ",y)
        #print ("zevgos= ",zevgos)
        zevgos=zevgos+1
        tempx=str(x)
        tempy=str(y)

        #print("something")
        i=x
        for k in range(x,y):
            rangelist[i]=k
            k=k+1
            i=i+1

    returnvar = 0
    rangelength=len(rangelist)
    for k in range(rangelength):
        if rangelist[k]!="a":
            returnvar +=1
        if rangelist[k]=="a" and rangelist[k-1]!="a":
                returnvar -=1
        if k==max:
                returnvar -=1
    #print (rangelist)
    return returnvar

flag=True
nums=[]
initialize=True

while flag==True:
    if initialize==True:
        print("pata enan arithmo gia na anoikseis diastima, 'go' gia na treksei kai na vrei to diastima kai 'exit' gia termatismo.")
        print("ta inputs prepei na einai swsta. Mono arithmoi kai kathe 2os arithmos megalyteros apo ton prwto.")
        initialize=False
    arxi=input("input:")

    if arxi=="exit":
        flag=False
        continue
    if arxi=="go":
        print("to athroisma twn diastimatwn einai",sumIntervals(nums))
    else:
        int(arxi)
        telos=int(input("pata telos diastimatos: "))
        templist=[arxi,telos]
        nums.append(templist)
