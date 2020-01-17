num=input("Enter a number..")
numint=int(num)
#print(numint)
tint=0
summ=10
while summ//10!=0:
    summ=0
    numint=3*numint+1
    #print("3*+1 = ", numint)
    intstr=str(numint)
    numarray=list(intstr)
    #print(numarray)
    length=len(numarray)
    for x in range(length):
        tstr=""
        tstr="".join(numarray[x])
        #print("tstr=",tstr)
        tint=int(tstr)
        summ=summ+tint
        #print("summin is=" ,summ)
    numint=summ
print("sum=",summ)
