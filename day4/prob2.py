def play(search: list, board: list) -> list:
    for row in board:
        intr = [n for n in row if n in search]
        if len(intr) == 5:
            return intr
        
    boardT = list(map(list, zip(*brd)))
    
    for col in boardT:
        intc = [n for n in search if n in col]
        if len(intc) == 5:
            return intc
        
    return list()


with open("input.txt", 'r') as f:
    txt = f.read()

txt = list(txt.strip().split("\n\n"))

nums = list(map(int, txt[0].split(',')))
txt = [i.split('\n') for i in txt[1:]]

boards = [[[int(k) for k in j.split(' ') if k != ''] for j in i] for i in txt]

wNums = list()
wBoards = list()

for i in range(len(nums)):
    for brd in boards:
        if len(play(nums[0:i], brd)) == 5:
            if brd not in wBoards:
                wBoards.append(brd)
                wNums.append(nums[0:i])

brd = wBoards[-1]
brd = [j for sub in brd for j in sub]
brd = [j for j in brd if j not in wNums[-1]]

print(sum(brd) * wNums[-1][-1])
