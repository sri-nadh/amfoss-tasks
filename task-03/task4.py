t=int(input())
while t:
    t-=1
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort(reverse=True)
    a[0]-=k;
    prod=1;
    for i in range(n):
        prod*=a[i];
    print(prod)
