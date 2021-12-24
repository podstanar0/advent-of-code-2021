def solve_part_one(segments, digits):
    # number of segments : corresponding digit
    digit = {2: 1, 4: 4, 3: 7, 7: 8}
    count = 0
    for line in digits:
        for segment in line: 
            try:
                digit[len(segment)]
                count += 1
            except KeyError:
                continue
    return count

def solve_part_two(segments, decode):
    # number of segments : corresponding index
    ldigits = {2: 1, 4: 4, 3: 7, 7: 8}
    sdigits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    result = 0
    digits = [0 for i in range(10)]
    for i, segment in enumerate(segments):
        # get values with unique segment lengths
        for j, val in enumerate(segment):
            try: 
                digits[ldigits[len(val)]] = set(val)
            except KeyError:
                continue

        # extract five and six-segment digits
        sixd = [set(val) for val in segment if len(val) == 6]
        fivd = [set(val) for val in segment if len(val) == 5]

        for j, val in enumerate(sixd):
            if not digits[1].issubset(val):
                digits[6] = val
            elif digits[4].issubset(val):
                digits[9] = val
            else:
                digits[0] = val

        for j, val in enumerate(fivd):
            if val.issubset(digits[6]):
                digits[5] = val
            elif val.issubset(digits[9]):
                digits[3] = val
            else:
                digits[2] = val

        number = ''
        for digit in decode[i]:
            digit = set(digit)
            for j, val in enumerate(digits): 
                if digit == val:
                    number += sdigits[j]
                    break
        result += int(number)
    
    return result

with open('input.txt') as f:
    segments, digits = [], []
    for line in f:
        line = line.split('|')
        segments.append(line[0].strip().split())
        digits.append(line[1].strip().split())

result = solve_part_one(segments, digits)
print('Part 1:', result)

result = solve_part_two(segments, digits)
print('Part 2:', result)
