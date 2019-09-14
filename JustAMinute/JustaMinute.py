n = int(input())
sum_min = 0
sum_sec = 0
for a in range(n):
    ipt = str(input()).split()
    sum_min += int(ipt[0])
    sum_sec += int(ipt[1])
total = (sum_sec / 60) / sum_min
if (total <= 1.0):
    print("measurement error")
else:
    print(total)
