def list_to_bin(bList):
    binNum = 0
    for bit in bList:
        binNum = binNum * 2 + bit
    return binNum

# ----------
with open('input.txt', 'r') as f:
    fullList = f.read().splitlines()

mainList = [[int(bit) for bit in line] for line in fullList]

result = []
ones = zeros = 0
for i in range(len(mainList[0])):
    for line in mainList:
        if line[i] == 1:
            ones += 1
        else: # 0
            zeros += 1
    result.append(1 if ones > zeros else 0)
    ones = zeros = 0

gamma = list_to_bin(result)
epsilon = int(''.join(['1' if i == '0' else '0' for i in bin(gamma)[2:]]), 2)

print('\ngamma rate:', gamma)
print('epsilon rate:', epsilon)
print('\npotrošnja:', gamma * epsilon)
