num = int(input("input a number: "))
list = [num]
for x in range(4):
    num = num + 1
    list.append(num)

print(list)
list[2] = 400
print(list)
print(list[2:8])
print(list[0])
print(list[-1])
print(list[2])