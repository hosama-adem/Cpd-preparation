#hos
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    found=False
    for i in range(n-1):
        if abs(a[i]-a[i+1])!=5 and abs(a[i]-a[i+1])!=7:
            found=True
            break
    print("NO" if found else "YES")
