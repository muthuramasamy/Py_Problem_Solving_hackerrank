a,b=map(int,input().split())
for i in range(a,b+1):
    if a>=0 and b==10 :
        print('{:02}'.format(i))
    elif a>=0 and  b<=9:
        print(i)
    elif a>=0 and b>=100:
        print('{:03}'.format(i))
    elif a>=0 and b>=100 or b<1000:
        print(i)
