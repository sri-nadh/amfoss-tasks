def check(a,n,m):
    s=set()
    for i in range(n):
        temp=m-a[i]
        if temp in s:
            print('True')
            return
        s.add(a[i])
    print('False')
n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort(reverse=True)
check(a,n,m)
