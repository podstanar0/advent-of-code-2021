def get_neighbours(i, j):
    return ([i + k if i + k >= 0 and i + k < 10 else None
             for k in range(-1, 2) 
             for m in range(-1, 2)],
            [j + m if j + m >= 0 and j + m < 10 else None
             for k in range(-1, 2) 
             for m in range(-1, 2)])

def update_neighbour(energy, i, j):
    indi, indj  = get_neighbours(i, j)
    for k, m in zip(indi, indj):
        if k is not None and m is not None and energy[k][m] != 0:
            energy[k][m] = (energy[k][m] + 1) % 10
            if energy[k][m] == 0:
                energy = update_neighbour(energy, k, m)
    return energy

def step(energy):
    # increase all values by one
    energy = [[(val + 1) % 10 for val in line] for line in energy]

    # update neighbours of those which are zero
    inds = [(i, j) for i in range(10) 
            for j in range(10) if energy[i][j] == 0]
    for i, j in inds:
        energy = update_neighbour(energy, i, j)
        
    return energy, sum([1 for line in energy for val in line if val == 0])

def solve_part_one(energy):
    count = 0
    for i in range(100):
        energy, counti = step(energy)
        count += counti
    return count

def solve_part_two(energy):
    n = 0
    while sum(map(sum, energy)) != 0:
        energy, count = step(energy)
        n += 1
    return n


with open('input.txt') as f:
    energy = [list(map(int, line.strip())) for line in f]

result = solve_part_one(energy)
print('Part 1:', result)
result = solve_part_two(energy)
print('Part 2:', result)
