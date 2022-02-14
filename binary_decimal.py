b=[1,0,0,1,1,0,1,1]
i=-1
power=0
sum=0
while i>=(-(len(b))):
    n=b[i]*2**power
    sum=sum+n
    power+=1
    i-=1
print(sum)