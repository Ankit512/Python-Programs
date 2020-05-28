file1 = open("input4.txt","r")
arr=[]
num_lines = sum(1 for line in open('input4.txt'))
arr=file1.readlines()[0:num_lines]
print(arr)
file1.close()
