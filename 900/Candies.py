# hos
a, c = map(int, input().split())

if a % c == 0:
    d = a // c
    j = str(d)
    print((j + " ") * c)

else:
    d = a // c
    j = str(d)
    k = a - (d * c)
    if k > 0:
        print((j + " ") * (c - k) + (str(d + 1) + " ") * k)
