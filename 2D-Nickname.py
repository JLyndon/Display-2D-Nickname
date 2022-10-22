# ------------ CONTEXT --------------------
#           Assignment 01:
# Create a program that will print your nickname using only asterisk character (*)
# NICKNAME: LYNDON

letter_L = [[" " for row in range(0, 6)] for col in range(0, 6)]
letter_N = [[" " for row in range(0, 6)] for col in range(0, 6)]

for row_L in range (0, 6):
    for col_L in range (0, 6):
        if (col_L == 0 or row_L == 5):
            letter_L [row_L][col_L] = "*"

for row_N in range (0, 6):
    for col_N in range (0, 6):
        if col_N == 0 or col_N == 5 or row_N == col_N:
            letter_N [row_N][col_N] = "*"

for row in range(6):
    for col in range(6):
        print(letter_L[row][col], end="")
    print(end="  ")
    for col in range(0, 6):
        print(letter_N[row][col], end="")
    print()

