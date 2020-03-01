n=int(input())
lst=[i for i in map(int,input().split())]
s=sum(lst)
l=10000000
index= None
for i,value in enumerate(lst):
    if (s-value)%7==0 and value<l:
        l=value
        index=i
        

if index is None:
    print(-1)
else:
    print(index)
