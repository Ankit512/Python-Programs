file=open("D:\Python\Week 3\i6c.txt", "r")
f = open("D:\Python\Week 3\ o6c.txt", "w")
data = file.readlines()
n=int(data[1])
for line in data:
     for i in line[0:len(line):n]:
             f.write(i)
             f.write(" ")


f.write("\n")
f.close()
f = open("D:\Python\Week 3\ o6c.txt", "r")
print(f.read())
