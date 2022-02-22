n=[23,14,56,12,19,9,15,25,31,42,43]
i=0
even_count=0
odd_count=0
even_sum=0
odd_sum=0
even_avg=0
odd_avg=0
total_avg=0
total_c=0
total_sum=0
while i<len (n):
    if n[i]%2!=0:
        odd_count+=1
        odd_sum=odd_sum+n[i]
        odd_avg=odd_sum//odd_count
    if n[i]%2==0:
        even_sum=even_sum+n[i]
        even_count+=1
        even_avg=even_sum//even_count
    total_c=odd_count+even_count
    total_sum=odd_sum+even_sum
    total_avg=total_sum//total_c
    
    i=i+1
print("total odd",odd_count)
print("total sum",odd_sum)
print("total_avg",odd_avg)
print("total_even",even_count)
print("total_sum",even_sum)
print("total_avg",even_avg)
print("total avg",total_avg)
        