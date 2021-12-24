def solve(numbers, nDays):
    fish = [0 for i in range(9)]

    for num in numbers:
        fish[num] += 1

    for n in range(nDays):
        spawn = fish[0]
        fish[:] = fish[1:] + [spawn]
        fish[6] += spawn

    return sum(fish)

numbers = [int(num) for num in open('input.txt').readline().split(',')]

result = solve(numbers, 80)
print('Part 1:', result)
result = solve(numbers, 256)
print('Part 2:', result)
