#hos
t=int(input())
for _ in range(t):
    n=input()
    a=input()
    if len(set(a))==1:
        print(0)
    else:
        x=0
        for i in range(len(a)-1) :
            v=n.index(a[i])+1
            b=n.index(a[i+1])+1
            s=abs(v-b)
            x+=s
        print(x)
