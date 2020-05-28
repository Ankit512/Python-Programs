import os
statinfo = os.stat('input4.txt')
a=statinfo.st_size
print(a)