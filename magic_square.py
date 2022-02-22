m_sqr=[
    [8,3,4],
    [1,5,9],
    [6,7,2]
    ]
i=0
while i<len(m_sqr):
    j=0
    a=0
    b=0
    c=0
    d=0
    e=0
    f=0
    g=0
    h=0
    l=len(m_sqr)-1
    while j<len(m_sqr[i]):
        a=a+m_sqr[i][j]
        b=b+m_sqr[i][j]
        c=c+m_sqr[i][j]
        d=d+m_sqr[j][j]
        e=e+m_sqr[j][j]
        f=f+m_sqr[j][j]
        g=g+m_sqr[i][j]
        h=h+m_sqr[j][l]     
        j=j+1
        l-=1
    i+=1
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print()
if a==b==c:
    print("magic_square")
else:
    print("not a magic square")

                         
