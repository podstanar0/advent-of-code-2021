def list_to_bin(bList):
    binNum = 0
    for bit in bList:
        binNum = binNum * 2 + bit
    return binNum

def fetch_report(someList, ratingType, row):
    onesList = []
    zerosList = []
    for line in someList:
        if line[row] == 1:
            onesList.append(line)
        else: # 0
            zerosList.append(line)
    
    calcOxy = len(onesList) >= len(zerosList)
    if ratingType == 'oxygen':
        return onesList if calcOxy else zerosList
    else: # CO2
        return onesList if not calcOxy else zerosList

# ----------
with open('input.txt', 'r') as f:
    fullList = f.read().splitlines()

mainList = [[int(bit) for bit in line] for line in fullList]

i = 0
oxygen = fetch_report(mainList, 'oxygen', i)
co2 = fetch_report(mainList, 'co2', i)
while i in range(len(mainList[0])):
    i += 1
    if len(oxygen) > 1:
        oxygen = fetch_report(oxygen, 'oxygen', i)
    if len(co2) > 1:
        co2 = fetch_report(co2, 'co2', i)

oxygen = list_to_bin(oxygen[0])
co2 = list_to_bin(co2[0])

print('\noxygen generator rating:', oxygen)
print('CO2 scrubber rating:', co2)
print('\nlife support rating:', oxygen * co2)
