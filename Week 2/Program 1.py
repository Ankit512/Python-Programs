1. 
def computeReverseNumber(n):
  s = 0
  while True:
    k = str(n)
    if k == k[::-1]:
      break
    else:
      m = int(k[::-1])
      n += m
      s += 1
  return n
print (computeReverseNumber(123))

# 2. 
# matrix=[]
# n = int(input("Enter a number: "))
# for i in range(n):
#     row=[]
#     for j in range(n):
#         row.append(0)
#     matrix.append(row)
# print (matrix)

# 4. 
# str = input()
# v=0
# c=0
# for s in str:
#     if(s=='a' or s=='e' or s=='i' or s=='o' or s=='u'):
#         v=v+1
#     else:
#         c=c+1
# print("Vowels Occurance Percentage=",v/len(str)*100)
# print("Constant Occurance Percentage=",c/len(str)*100)      

# 5.
# a=0
# for i in range(5):
#     for j in range(i+1):
#         a=a+1
#         print(a,end='')
#         print(' ',end='')
#     print()
        
# 6. 
# from heapq import nlargest
# d={'item1':45.50,'item2':35,'item3':41.30,'item4':55,'item5':24}
# l=nlargest(3,d,key=d.get)
# for v in l:
#     print(v,":",d.get(v))

# 7. 
# l=[(10,20,40),(40,50,60),(70,80,90)]
# print([t[:-1] + (100,) for t in l])

# 8. 
# l=[(10,20,40),(40,50,60),(70,80,90)]
# for i in l:
#     print([i[:-1] + (100,)], end='')

# 9. 
# for i in range(5):
#     for j in range(i+1):
#         print('*',end='')
#         print(' ',end='')
#     print()
# for i in range(4):
#     for l in range(4-i):
#             print('*',end='')
#             print(' ',end='')
#     print('')

# 10. 
# d = {
# "Hello" : 56,
# "at" : 23,
# "test"  : 43,
# "this" : 43
# }
# for i in d:
#     print(i,":",d.get(i))
# d['well']=50
# print(d)
# del d['well']
# print(d)    

# 11. 
# n=int(input())
# i=1
# while(n>0):
#     if(i%5==0):
#         n=n-1
#         print(i)
#     i=i+1

# 12. 
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# c = float(input("Enter third number: "))

# if (a > b) and (a > c):
#     largest = a
# elif (b > a) and (b > c):
#    largest = b
# else:
#    largest = c

# print("The largest number is",largest)

# 13. 
# strng=input("Enter string:")
# from string import ascii_lowercase as asc_lower
# def check(s):
#     return set(asc_lower) - set(s.lower()) == set([])
# if(check(strng)==True):
#       print("The string is a pangram")
# else:
#       print("The string isn't a pangram")

# 14. 
# def char_frequency(str1):
#     dict = {}
#     for n in str1:
#         keys = dict.keys()
#         if n in keys:
#             dict[n] += 1
#         else:
#             dict[n] = 1
#     return dict
# print(char_frequency('GOOGLE.COM'))

# 15. 
# x=input()
# rev=x[: :-1]
# print(rev)	  
