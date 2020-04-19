S = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
print(S.split())
for s in S.split():
    if(s.isalnum):
        print(len(s))