n=int(input())
i=0
x=n//2
while 2*i+1!=n:
    print('*'*x+(2*i+1)*'D'+'*'*x)
    x-=1
    i+=1
print(n*'D')
i-=1
x=1
while 2*i+1>=1:
    print('*'*x+(2*i+1)*'D'+'*'*x)
    x+=1
    i-=1
