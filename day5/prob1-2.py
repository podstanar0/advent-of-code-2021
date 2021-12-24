def solve(p2):
    with open('input.txt', 'r') as f: 
        data = [list(map(int, line.strip().replace('->', ',').split(','))) for line in f]

    nx = max(max([(c[0], c[2]) for c in data])) + 1
    ny = max(max([(c[1], c[3]) for c in data])) + 1

    field = [[0 for i in range(nx)] for j in range(ny)]

    for x1, y1, x2, y2 in data:
        xmin, dx = min(x1, x2), abs(x2 - x1)
        ymin, dy = min(y1, y2), abs(y2 - y1)
        if x1 == x2:
            for i in range(dy + 1):
                field[i + ymin][x1] += 1
        elif y1 == y2:
            for i in range(dx + 1):
                field[y1][i + xmin] += 1
        elif p2:
            cx = 1 if x2 > x1 else -1
            cy = 1 if y2 > y1 else -1
            for i in range(dx + 1):
                field[cy*i + y1][cx*i + x1] += 1

    return sum([1 for line in field for num in line if num > 1])

result = solve(0)
print('Part 1:', result)
result = solve(1)
print('Part 2:', result)
