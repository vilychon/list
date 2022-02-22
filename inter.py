list=[[1,2,3],
     [4,5,6],
     [4,8,9]]
i=0 
while i<len(list):
    j=0
    sum=0
    sum1=0
    f=len(list)-1
    while j<len(list):
        sum=sum+list[j][j]
        sum1=sum1+list[j][f]
        j+=1
        f-=1
    i=i+1
print(sum)
print(sum1)     