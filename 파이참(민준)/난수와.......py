import random
a=0
b=0
c=[]
r=0
sum=int(input('?'))
e=0
while e<10:
    e=e+1
    r = random.randint(1, 10)
    c.append(r)
print(c)
for k in c:
    if k<5:
        c.remove(k)
print(c)
