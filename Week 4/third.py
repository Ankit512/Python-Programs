file1 = open("input3.txt","a")
file1.write("hahaha")
file1.close()
file1=open("input3.txt","r")

print(file1.read())

file1.close()
