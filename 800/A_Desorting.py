#hos
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if sorted(a)!=a:
        print(0)
    else:
        diff=[]
        for i in range(n-1):
            ds=abs(a[i]-a[i+1])
            diff.append(ds)
        if min(diff)==0:
            print(1)
        else:
            print((min(diff)//2)+1)
