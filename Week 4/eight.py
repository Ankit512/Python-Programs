file1 = open("input8.txt","r")
a=file1.readline()
lst=a.split()
a=""
for i in range(len(lst)):
    if(len(lst[i])>len(a)):
        a=lst[i]
print("Longest Word: ",a)
file1.close()
