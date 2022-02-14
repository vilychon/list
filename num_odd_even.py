elements=[23,14,56,12,19,9,15,25,31,42,43]
i=0
count=0
count1=0
a=[]
b=[]
even_sum=0
odd_sum=0
while i<len(elements):
    if elements[i]%2==0:
        count=count+1
        a.append (elements[i])
        even_sum=even_sum+elements[i]
    else:
        count1=count1+1
        b.append (elements[i])
        odd_sum=odd_sum+elements[i]
    i=i+1
print("Even number list=",a)
print("The Sum of even number is:",even_sum)
print("Total even number:",count)
print("Odd number list=",b)
print("The Sum of odd number is:",odd_sum)
print("Total odd number:",count1)   