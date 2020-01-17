from datetime import datetime, timedelta, date

datee=input()
strdate="".join(datee)
#print(strdate)
strday=strdate[0]+strdate[1]
strmonth=strdate[3]+strdate[4]
stryear=strdate[6]+strdate[7]+strdate[8]+strdate[9]
dayy=int(strday)
month=int(strmonth)
year=int(stryear)

usertime=datetime(year,month,dayy)
currenttime=datetime.now()
print('Time difference:', str(currenttime - usertime))

numm=(date(year,month+1,1) - date(year,month,1)).days
print('Days of the month:',numm)

#print(currenttime)
