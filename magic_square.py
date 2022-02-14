m_sqr=[[8,3,4],[1,5,9],[6,7,2]]
i=0
while i<len(m_sqr):
    j=0
    row=0
    c=0
    d=0
    while j<len(m_sqr[i]):
        row=row+m_sqr[i][j]
        c=c+m_sqr[j][i]
        d=d+m_sqr[j][j]
        j=j+1
    i=i+1
if row==c==d:
    print("magic_square")
else:
    print("is not")
print(row)
print(c)
print(d) 