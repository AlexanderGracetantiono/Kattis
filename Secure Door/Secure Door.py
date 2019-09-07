many_Cases = int(input())
statement = [""] * (0)
list_People_Inside = [""] * (0)
for i in range(many_Cases):
    text_Input = str(input()).split()
    anomaly = ""
    if (str(text_Input[0]) == "entry"):
        for people_Inside in list_People_Inside:
            if (str(text_Input[1]) == people_Inside):
                anomaly = "(ANOMALY)"
                break
        if(anomaly == ""):
            list_People_Inside.append(str(text_Input[1]))
        statement.append(str(text_Input[1]) + " entered "+anomaly)
    else:
        anomaly = "(ANOMALY)"
        for people_Inside in list_People_Inside:
            if (str(text_Input[1]) == people_Inside):
                anomaly = ""
        if (anomaly == ""):
            list_People_Inside.remove(str(text_Input[1]))
        statement.append(str(text_Input[1]) + " exited " + anomaly)

for a in statement:
    print(a)
