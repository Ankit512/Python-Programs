file1 = open("input2.txt","r")
n=int(input("Enter number of lines: "))
print(file1.readlines()[0:n])
file1.close()
