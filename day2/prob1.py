with open('input.txt', 'r') as f:
    fullList = f.read().splitlines()

commands = [(line.split()[0], int(line.split()[1])) for line in fullList]

hpos = depth = 0
for i, move in enumerate(commands):
    value = commands[i][1]
    if move[0] == 'forward':
        hpos += value
    elif move[0] == 'down':
        depth += value
    else: # up
        depth -= value

print('horiz. pos:', hpos, '\ndepth:', depth, '\nrezultat:', hpos * depth)
