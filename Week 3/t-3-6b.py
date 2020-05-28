file=open("D:\Python\Week 3\i6b.txt", "r")
f = open("D:\Python\Week 3\ o6b.txt", "w")
data = file.readlines()
total=0
n=0
for line in data:
    marks=int(line)
    total=total+marks
    n=n+1
avg=total/n
cgpa=avg/10
f.write(str(avg))
f.write("\n")
f.write(str(cgpa))
f.close()
f = open("D:\Python\Week 3\ o6b.txt", "r")
print(f.read())
