SIZE = 10

grads = [None] * SIZE

for i in range(0, len(grads)):
    grads[i] = float(input(str(i+1) + ". insert a grade: "))

    while grads[i] < 0 or 100 < grads[i]:
        grads[i] = float(input(str(i + 1) + ". Invalid grade! insert again: "))

print(str(grads))

for i in range(0, len(grads)):
    grads[i] = grads[i] * 1.1

    if grads[i] > 100:
        grads[i] = 100

print(str(grads))