class mapp(dict):
    def init(self):
        self = dict()
    def add(self, key, value):
        self[key] = value

n,m=map(int,input().split())
data=mapp()
a=list(map(int,input().split()))
for i in range(n):
    pos=a[i]
    try:
        data[pos]
    except:
        data.add(pos,[])
    data[pos].append(i+1)
    data[pos].sort()
a=list(map(int,input().split()))
for i in range(m):
    pos=a[i]
    try:
        print(data[pos][-1],end=' ')
        data[pos].pop()
    except:
        print(-1,end=' ')
