file1 = open("input4.txt","r")
num_lines = sum(1 for line in open('input4.txt'))
for i in range(num_lines):
	a=file1.readline()
	print(a)
file1.close()
