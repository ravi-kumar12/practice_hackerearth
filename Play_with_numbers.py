n,q=input().split(" ")
n=int(n)
q=int(q)
l=list(map(int,input().split()))
while q!=0:
    s,e=input().split(" ")
    s=int(s)
    e=int(e)
    add=0
    av=0
    for i in range(s-1,e):
        add+=l[i]
    av=add//(e-s+1)
    print(av)
    q-=1
