def print_board(board):
    for row in board: # Each row
        for item in row:
            print (item, end="")
        print()

def get_location(character_name):
    pass

dim = int(input())
print ( "Player A: Select characters ( Ex: P3, P2, P5, P4, P1)")
player_A = list(map(str, input().split(",")))
print (player_A)
#P2,P1,P3,P4,P5
print(" Player B : Select characters ( Ex: P2, P1, P3, P4, P5)")
player_B = list(map(str, input().split(",")))
print (player_B)

player_a_pos={}
for index,item in enumerate(player_A):
    player_a_pos[item]=(dim*(dim-1)+1)
print(player_a_pos)

player_b_pos={}
for index,item in enumerate(player_A):
    player_b_pos[item]=index
print(player_b_pos)


# board_structure = [["P2", "P1", "P3", "P5", "P4"], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "],["P3", "P2", "P5", "P4", "P1"]]
# # print(board_structure)
# board = [[f" {board_structure[b][a]} " for a in range(dim)]for b in range(dim)]
# print_board(board)