# ------------ CONTEXT --------------------
#           Assignment 01:
# Create a program that will print your nickname using only asterisk character (*)
# NICKNAME: LYNDON

# Function for Text Color by layer/row
def text_Decoration(row, column, list):
    if (row == 6 or row == 5):
        list [row][column] = "\u001b[36;1m❋\u001b[0m"
    if (row == 4):
        list [row][column] = "\u001b[36m❋\u001b[0m"
    if (row == 3):
        list [row][column] = "\u001b[37m❋\u001b[0m"
    if (row == 2):
        list [row][column] = "\u001b[34;1m❋\u001b[0m"
    if (row == 1):
        list [row][column] = "\33[94m❋\33[0m"
    if (row == 0):
        list [row][column] = "\u001b[94m❋\u001b[0m"

letter_L = [[" " for row in range(0, 7)] for col in range(0, 7)]
letter_Y = [[" " for row in range(0, 8)] for col in range(0, 8)]
letter_N1 = [[" " for row in range(0, 9)] for col in range(0, 9)]
letter_D = [[" " for row in range(0, 8)] for col in range(0, 8)]
letter_O = [[" " for row in range(0, 9)] for col in range(0, 9)]
letter_N = [[" " for row in range(0, 9)] for col in range(0, 9)]

# L
for row_L in range (0, 7):
    for col_L in range (0, 7):
        if (col_L == 0 or col_L == 1 or row_L == 6):
            text_Decoration(row_L, col_L, letter_L)
# Y
for row_Y in range (0, 8):
    for col_Y in range (0, 8):
        if ((col_Y == 3 or col_Y == 4) and row_Y >= 3) or (col_Y <= 3 and row_Y == col_Y) or (row_Y == 2 and col_Y == 5) or (row_Y == 1 and col_Y == 6) or (row_Y == 0 and col_Y == 7):
            text_Decoration(row_Y, col_Y, letter_Y)
# N1
for row_N1 in range (0, 8):
    for col_N1 in range (0, 8):
        if col_N1 == 0 or col_N1 == 1 or col_N1 == 6 or col_N1 == 7 or row_N1 == col_N1:
            text_Decoration(row_N1, col_N1, letter_N1)
# D
for row_D in range (0, 8):
    for col_D in range (0, 8):
        if col_D == 0 or col_D == 1 or ((row_D == 0 or row_D == 6) and (col_D <= 4)) or (row_D == 1 and col_D == 5) or (row_D == 2 and col_D == 6) or (row_D == 3 and col_D == 7) or (row_D == 4 and col_D == 7) or (row_D == 5 and col_D == 6) or (row_D == 6 and col_D == 5) or (row_D == 7 and col_D == 4):
            text_Decoration(row_D, col_D, letter_D)
# O
for row_O in range (0, 9):
    for col_O in range (0, 9):
        if ((col_O == 0 or col_O == 1 or col_O == 7 or col_O == 8) and (row_O != 0 and row_O != 6)) or ((row_O == 0 or row_O == 6) and (col_O > 1 and col_O < 7)):
            text_Decoration(row_O, col_O, letter_O)
# N
for row_N in range (0, 9):
    for col_N in range (0, 9):
        if col_N == 0 or col_N == 1 or col_N == 7 or col_N == 8 or row_N == col_N:
            text_Decoration(row_N, col_N, letter_N)

# Loop for Displaying Output
for row in range(0, 7):
    for col in range(0, 7):
        print(letter_L[row][col], end="")
    print(end="")
    for col in range(0, 8):
        print(letter_Y[row][col], end="")
    print(end="  ")
    for col in range(0, 9):
        print(letter_N1[row][col], end="")
    print(end="  ")
    for col in range(0, 8):
        print(letter_D[row][col], end="")
    print(end="  ")
    for col in range(0, 9):
        print(letter_O[row][col], end="")
    print(end="  ")
    for col in range(0, 9):
        print(letter_N[row][col], end="")
    print()

