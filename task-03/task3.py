N=int(input())
x=list(map(int, input().rstrip().split()))
y=list(map(int, input().rstrip().split()))
newlist=list()
for j,i in enumerate(x):
      z=int(y[j]/i) 
      newlist.append(z)
print(min(newlist))
