#hos
a,b,c=map(int,input().split())
p1=2*a+2*b
p2=a+c+b
p3=a+c+c+a
p4=b+c+c+b
print(min(p1,p2,p3,p4))
