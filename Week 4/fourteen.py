file3=open("output14.txt","a")
with open('input14(a).txt') as file1, open('input14(b).txt') as file2:
    for line1, line2 in zip(file1, file2):
        file3.write(line1+line2)
file3.close()
        