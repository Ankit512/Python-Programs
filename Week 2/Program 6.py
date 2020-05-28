from heapq import nlargest
d={'item1':45.50,'item2':35,'item3':41.30,'item4':55,'item5':24}
l=nlargest(3,d,key=d.get)
for v in l:
    print(v,":",d.get(v))
