# Unique elements
k=list(map(int,input().split()))
b=[]
l=[]
for i in k:
    if k.count(i) <2:
        b.append(i)
    else:
        l.append(i)
for i in b:
	print(i,end=" ")
