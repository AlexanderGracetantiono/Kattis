ipt = str(input()).split()
a = []
day = 1
checked=0
for n in range(int(ipt[1])):
    cek="false"
    tex = str(input())
    for m in a:
        if (tex == m):
            cek = "true"
    if (cek == "false"):
        a.append(tex)
        checked += 1
    if (checked != int(ipt[0])):
        day += 1
if (day >= int(ipt[1])+1):
    print("paradox avoided")
else:
    print(day)