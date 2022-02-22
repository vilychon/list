list=[1,2,3,4,5,6,7]
i=0
e=1
a=[]
while i<len(list):
    c=list[i-e+1]
    a.append(c)
    e=e+1
    i=i+1
print(a)
