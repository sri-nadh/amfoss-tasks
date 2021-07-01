t=int(input())
while t:
    t-=1
    n,m=map(int,input().split())
    n=str(n)
    if len(n)<m:
        print(-1)
        continue
    mi=1000000000000000
    pos=0
    sum=0
    pre=[]
    for i in range(m):
        sum+=ord(n[i])-48
    pre.append(sum)  
    for i in range(m,len(n)):
        sum=ord(n[i])-48+sum-(ord(n[pos])-48)
        pos+=1
        if(i!=0):
            mi=min(mi,abs(pre[-1]-sum))
        pre.append(sum)
    if(mi!=1000000000000000):
        print(mi)
    else:
        print(-1)
