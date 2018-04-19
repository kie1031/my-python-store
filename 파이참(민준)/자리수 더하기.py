a=input('수입력')
sum=0
if not len(a)<5:
    for b in a :
        sum=sum+int(b)
    print(sum)
else:
    print('5자 이상')