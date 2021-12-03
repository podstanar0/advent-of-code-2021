with open('prob1_input.txt') as f:
    fullList = f.read().splitlines()
    
counter = 0;
for i, line in enumerate(fullList[:-1]):
    nextLine = fullList[i+1]
    if int(line) < int(nextLine):
        counter += 1
        print(nextLine)
print('\nukupno povećanja:', counter)
