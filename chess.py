
def print_board(dim, board):
    print ("CURRENT BOARD POSITION")
    print ("-------------")

    for row in range(dim): # Each row
        for col in range(dim):
            print (f" {board[row * dim + col]} ", end="")
        print()

def apply_direction( dim, player_name, old_index, move):
    print (f' dim = {dim} player_name = {player_name}  old_index = {old_index},  move = {move}')
    new_index = old_index
    if player_name == "A":
        if move =="L":
            if old_index % dim != 0:
                new_index = old_index-1
        elif move =="R":
            if old_index % dim != 4:
                new_index = old_index + 1
        elif move =="F":
            if old_index > dim :
                new_index = old_index - dim
        elif move =="B":
            if old_index <= dim * (dim -1):
                new_index = old_index + dim
    return new_index




dim = int(input())
board = ['    '] * dim * dim

print ( "Player A: Select characters ( Ex: P3, P2, P5, P4, P1)")
player_A = list(map(str, input().split(", ")))
player_A_pos = {}
for i, item in enumerate(player_A):
    board[dim * (dim -1) + i] = "A-" + item
    player_A_pos[item] = (dim * (dim -1) + i)
print (player_A_pos)


print ( "Player B: Select characters ( Ex: P2, P1, P3, P5, P4)")
player_B = list(map(str, input().split(",")))
player_B_pos = {}
for i, item in enumerate(player_A):
    board[i] = "B-"+item
    player_B_pos[item] = ( i)
print (player_B_pos)


print_board (dim, board)
while(True):
    print ("Player A’s Move: Ex: P1:F ")
    a_move = input()
    move_arr = a_move.split(":")
    character = move_arr[0]
    direction = move_arr[1]
    # Get the current index  of "A-"+ character
    old_index = board.index("A-"+ character)
    new_index = apply_direction(dim, "A", old_index, direction)
    print (old_index, " ", new_index)
    board[new_index] = board[old_index]
    board[old_index] = '    '
    print_board (dim, board)




