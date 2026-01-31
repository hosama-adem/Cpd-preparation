#hos
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    if s.count("1")>1 or s.count("0")>1:
        print("NO")
    else:
        print("YES")
