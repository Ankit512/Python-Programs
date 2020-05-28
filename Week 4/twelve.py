file1 = open("output12.txt","a")
lst=['mai','tera','amplifier','python']
for i in range(0,len(lst)):
	file1.write(lst[i])
file1.close()