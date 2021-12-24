def solve_part_one(numbers):
    dx = 1E6
    for i in range(max(numbers)):
        dxi = sum([abs(num - i) for num in numbers])
        if dxi < dx: dx = dxi
    return dx

def solve_part_two(numbers):
    dx = 1E16
    for i in range(max(numbers)):
        dxi = sum([abs(num - i) * (1 + abs(num - i)) for num in numbers])
        if dxi < dx: dx = dxi
    return dx/2

numbers = [int(num) for num in open('input.txt').readline().split(',')]

result = solve_part_one(numbers)
print('Part 1:', result)
result = solve_part_two(numbers)
print('Part 2:', result)
