"""
To guarantee victory against the giant squid, figure out which board will win first.
What will your final score be if you choose that board?
"""

def bingo(order, boards):
    order = order.split(",")

    boards = boards.split("\n\n")
    boards = [board.split() for board in boards]

    # all possible rows and cols
    board_num = {}
    for num, board in enumerate(boards):
        board_num[num + 1] = []
        for i, n in enumerate(range(0, len(board), 5)):
            board_num[num + 1] += [board[n:n + 5]]
            board_num[num + 1] += [board[i::5]]

    for call in order:
        for num, board in board_num.items():
            for perm in board:
                try:
                    perm.remove(call)
                    boards[num].remove(call)
                except:
                    pass
                if perm == []:
                    print(f"bingo with board {num}!")
                    return sum(map(int, boards[num - 1])) * int(call)


if __name__=="__main__":

    order = "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1"

    boards = """22 13 17 11  0
        8  2 23  4 24
        21  9 14 16  7
        6 10  3 18  5
        1 12 20 15 19

        3 15  0  2 22
        9 18 13 17  5
        19  8  7 25 23
        20 11 10 24  4
        14 21 16 12  6

        14 21 17 24  4
        10 16 15  9 19
        18  8 23 26 20
        22 11 13  6  5
        2  0 12  3  7"""

    print(bingo(order, boards))
