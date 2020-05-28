file=open("D:\Python\Week 3\i6a.txt", "r")
f = open("D:\Python\Week 3\ o6a.txt", "w")
data = file.readlines()

for line in data:
    word = line.split()
    for i in range(0,len(word)):
        for j in word[i]:
            if(j>='a') and (j<='z'):
               f.write(j.upper())
            elif(j>='A') and (j<='Z'):
               f.write(j.lower())
        f.write(" ")
    f.write("\n")
f.close()
f = open("D:\Python\Week 3\ o6a.txt", "r")
print(f.read())
