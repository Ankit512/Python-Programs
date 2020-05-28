file=open("D:\Python\Week 3\input.txt", "r")
f = open("D:\Python\Week 3\ output.txt", "w")
data = file.readlines()
for line in data:
    word = line.split()
    for i in range(0,len(word)):
        f.write(str(len(word[i])))
        f.write(" ")
    f.write("\n")
f.close()
f = open("D:\Python\Week 3\ output.txt", "r")
print(f.read())
