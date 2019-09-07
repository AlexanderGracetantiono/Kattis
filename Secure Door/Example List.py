list_people_inside = [""] * (0)
many_Cases = int(input())
for i in range(many_Cases):
    list_people_inside.append(str(input()))
print(list_people_inside)

list_people_inside.remove(str(input()))
print(list_people_inside)
