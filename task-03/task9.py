t=int(input())
m=1000000007
a=[1,2,3]
for i in range(3,1000000):
    a.append((a[i-1]%m+a[i-2]%m+a[i-3]%m)%m)
while t:
    t-=1
    n=int(input())
    x=str(a[n-1])
    x=x[::-1]
    flag=0
    for i in x:
        if i != '0':
            flag=1
        if flag:
            print(i,end="")
    print()
