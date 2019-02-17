

fin=open("test.py","r")
lines=fin.readlines()
fin.close()
fout=open("testout.py","w")
print("i askisi diavazei tis grammes apo ena arxeio (test.py) kai tis grafei xwris sxolia se ena neo (testout.py) alla kai tis emfanizei san output.")
print("mporeite na anoiksete ta alla 2 arxeia gia na deite tis diafores")
for line in lines:
	if "#" in line:
		l=line.strip()
		#print(line)
		if l[0]!="#":
			templine=str(line)
			max=len(templine)
			max-=1
			i=1
			wheretocut=0

			#print (max)

			while i < max:

				if templine[i]=="#":
					#print("ektelestike to eksw fores")
					flag=0
					#print("templine has #")
					magic="#"
					tmp=[e+magic for e in line.split(magic) if e]
					#print(tmp)
					a1=0
					a2=0
					a1=tmp[0].count("'")
					a2=tmp[0].count('"')
					if a1%2==1 or a2%2==1:
						"".join(tmp)
						flag=1
						#print("joined")
						i=i+1
						wheretocut=wheretocut+1
						#print("ektelestike fores",wheretocut)
						continue
					else:

						print(line.split("#")[0])
						fout.write(line.split("#")[0])
						fout.write("\n")
						flag=0

						#print("splitted and printed 0")
						break

				i=i+1

			if flag==1:
				#print("ektelestike i flag")

				temp= [e+magic for e in line.split(magic) if e]
				temp.pop(wheretocut)

				temp1=temp[-1]
				temp1=temp1[:-1]
				temp.pop(-1)
				temp.append(temp1)

				#for i in temp:
				print(*temp)
				tempstr=str(temp)
				tempstr = tempstr.translate({ord(c): None for c in '[],'})
				tempstr=tempstr.replace("'","")
				fout.write(tempstr)
				fout.write("\n")

		#else:

			#print ("line that started with # and was skipped")
	else:
			print(line)
			fout.write(line)
			fout.write("\n")


fout.write("completed succesfully")
fout.close()
print("completed successfully")
