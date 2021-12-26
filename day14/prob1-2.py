def adjust_count(d, key, count):
    try:
        d[key] += count
    except KeyError:
        d[key] = count

def solve_part_one(seq, rules, n):
    rkeys = rules.keys()

    for i in range(n):
        seq = ''.join([l1 + rules[l1 + l2] if l1 + l2 in rkeys else l1 
                           for l1, l2 in zip(seq[:-1], seq[1:])]) + seq[-1]

    counts = {letter: 0 for letter in seq}
    for letter in seq:
        counts[letter] += 1
    return max(counts.values()) - min(counts.values())

def solve_part_two(seq, rules, n):
    last_letter = seq[-1]

    # store initial counts
    pairs = {}
    for l1, l2 in zip(seq[:-1], seq[1:]):
        adjust_count(pairs, l1 + l2, 1)

    for i in range(n):
        pairs_temp = {}
        for pair, count in pairs.items():
            if count == 0: continue
            pairs[pair] -= count
            add = rules[pair]
            adjust_count(pairs_temp, pair[0] + add, count)
            adjust_count(pairs_temp, add + pair[1], count)

        for pair, count in pairs_temp.items():
            adjust_count(pairs, pair, count)

    # count letters
    counts = {}
    for j, (pair, count) in enumerate(pairs.items()):
        if count != 0:
            adjust_count(counts, pair[0], count)

    # make sure last letter is counted
    counts[last_letter] += 1
    return max(counts.values()) - min(counts.values())


with open('input.txt') as f:
    seq = f.readline().strip()
    next(f)
    rules = [line.strip().split(' -> ') for line in f]
    rules = {rule: val for rule, val in rules}

# this is slow, but works
result = solve_part_one(seq, rules, 10)
print('Part 1:', result)
# this is much faster
result = solve_part_two(seq, rules, 40)
print('Part 2:', result)
