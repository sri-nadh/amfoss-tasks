t=int(input())
while t:
    t-=1
    sum=0
    c=0
    flag=1
    n,m,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    b.sort(reverse=True)
    for i in range(m):
        sum+=b[i]
        c+=1
        if sum>=n:
            if c<=k:
                print('YES')
                flag=0
            else:
                break
        if(flag==0):
            break
    if(flag):
        print('NO')
