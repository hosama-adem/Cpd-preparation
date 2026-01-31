#HOs
t=input()
a=t.index(".")
if t[a-1]=="9":
    print("GOTO Vasilisa.")
else:
    if int(t[a+1])>=5:
        print(int(t[:a])+1)
    else:
        print(int(t[:a]))
