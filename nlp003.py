S = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
print(S.split())
L = []
for s in S.split():
    tmp = 0
    for t in s:
        if(t.isalnum()):
            tmp += 1
    L.append(tmp)
print(L)