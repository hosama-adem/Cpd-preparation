# hos
a = input()
d = ""
target = "heidi"
for i in a:
    if len(d) < 5 and i == target[len(d)]:
        d += i
if d == "heidi":
    print("YES")
else:
    print("NO")
