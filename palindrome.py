string=input("enter the string:")
l1=list(string)
l=len(l1)
i=-1
arr=[]
while i>=-1:
    arr.append(l1[i])
    i-=1
if arr==l1:
    print("palindrome")
else:
    print("not palindrome")
print(l1)
print(arr)
