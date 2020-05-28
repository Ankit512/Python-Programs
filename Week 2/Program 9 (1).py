d = {
"Hello" : 56,
"at" : 23,
"test"  : 43,
"this" : 43
}
for i in d:
    print(i,":",d.get(i))
d['well']=50
print(d)
del d['well']
print(d)    
