def append(l):
    l.append(1)


def assign(l):
    l = [0, 1]


print("Test 1: ")
l = [0]
append(l)
print(l)

print("Test 2: ")
l = [0]
assign(l)
print(l)



