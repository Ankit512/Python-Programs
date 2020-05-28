file1 = open("input4.txt","r")
a=int(input("Enter any number: "))
#num_lines = sum(1 for line in open('input4.txt'))
lst=file1.readlines()[a]
print(lst)
file1.close()