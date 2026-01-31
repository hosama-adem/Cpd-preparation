#hos
t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    if a==1 and b==1:
        print(1)
    else:
        print(max(a,b)-min(a,b))
    
