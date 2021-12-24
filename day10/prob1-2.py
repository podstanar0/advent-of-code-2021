def check_corrupted(line):
    opening = {']': '[', '>': '<', '}': '{', ')': '('}
    lineb = []
    for bracket in line:
        if bracket in opening.values():
            lineb.append(bracket)
        elif lineb[-1] == opening[bracket]:
            del lineb[-1]
        else:
            return True, bracket
    return False, lineb

def solve_part_one(characters):
    scores = {')': 3, ']': 57,'}': 1197, '>': 25137}
    score = 0
    for i, line in enumerate(characters):
        corrupted, bracket = check_corrupted(line)
        if corrupted:
            score += scores[bracket]
    return score

def solve_part_two(characters):
    scores = {'(': 1, '[': 2, '{': 3, '<': 4}
    scoring = []
    for i, line in enumerate(characters):
        corrupted, lineb = check_corrupted(line)
        if not corrupted:
            score = 0
            for bracket in reversed(lineb):
                score = 5*score + scores[bracket]
            scoring.append(score)
    return list(sorted(scoring))[len(scoring) // 2]


with open('input.txt') as f:
    characters = [line.strip() for line in f]

result = solve_part_one(characters)
print('Part 1:', result)
result = solve_part_two(characters)
print('Part 2:', result)
