#hos
t=int(input())
for _ in range(t):
    n=int(input())
    a=input()
    i=0
    co=0
    while i<n:
        if a[i:i+3]=="map" or a[i:i+3]=="pie":
            co+=1
            i+=3
        else:
            i+=1
    print(co)
