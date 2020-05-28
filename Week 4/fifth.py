file1 = open("input4.txt","r")
num_lines = sum(1 for line in open('input4.txt'))
lst=file1.readlines()[0:num_lines]
print(lst)
file1.close()