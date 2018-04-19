import random
a=0
b=[]
c=0
r=0
while c<10:
    r=random.randint(1,10)
    c=c+1
    b.append(r)
print(b)
for k in b:
    if k%2==1:
        b.remove(k)
print(b)
print(sum(b))

