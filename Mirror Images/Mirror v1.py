from collections import deque
cases = int(input())
for n in range(cases):
    tables=deque()
    rc = str(input()).split()
    r = int(rc[0])
    c = int(rc[1])
    for colom in range(c):
        testrow=""
        row = str(input())
        for ch in reversed(row):
            testrow+=ch
        tables.appendleft(testrow)
    print("Test", n + 1)
    for colom in range(c):
        print(tables[colom])

        

    
