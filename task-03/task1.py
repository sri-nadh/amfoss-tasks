outputlist=[]
def term():
    k=int(input())
    sentence=input().split()
    if k <= len(sentence):
        word=sentence[k]
        sum=0
        for i in word:
            sum=sum+ord(i)
        outputlist.append(sum)
    else:
        outputlist.append(-1)
t=int(input())
for i in range(t):
    term()
for i in outputlist:
    print(i)
