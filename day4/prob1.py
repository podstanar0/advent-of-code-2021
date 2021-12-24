def play(search: list, board: list) -> list:
    for row in board:
        intr = [n for n in row if n in search]
        if len(intr) == 5:
            return intr
        
    boardT = list(map(list, zip(*board)))
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

try:
    for i in range(len(nums)):
        for board in boards:
            if len(play(nums[0:i], board)) == 5:
                raise StopIteration
except StopIteration:
    pass

board = [j for sub in board for j in sub]
board = [j for j in board if j not in nums[0:i]]
print(sum(board) * nums[i-1])
