
#binom coeff
gridSize = 20
paths = 1

for i in range(gridSize):
    paths *= int((2 * gridSize) - i)
    paths /= int(i + 1)

print(paths)