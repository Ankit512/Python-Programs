def fabanoci(n):
    a=0
    b=1
    c=0
    for i in range(n):
        print (c)
        c=a+b
        a=b
        b=c
    return c
