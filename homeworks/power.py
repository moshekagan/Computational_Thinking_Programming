a = int(input("Base: "))
b = int(input("power: "))

if b == 0:
    print(1)

answer = a
increment = a

for i in range(0, b-1):
    for j in range(0, a-1):
        answer = answer + increment
    increment = answer

print(increment)
