str = input()
v=0
c=0
for s in str:
    if(s=='a' or s=='e' or s=='i' or s=='o' or s=='u'):
        v=v+1
    else:
        c=c+1
print("Vowels Occurance Percentage=",v/len(str)*100)
print("Constant Occurance Percentage=",c/len(str)*100)        
