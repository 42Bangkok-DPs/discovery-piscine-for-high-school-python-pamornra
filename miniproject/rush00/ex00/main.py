#!/usr/bin/env python3

board = ['0'] * 8

for i in range(len(board)):
  board[i]=[" 0"]*8

def print_board(board) :
 for i, row in enumerate(board):
     print(8-i, end=" : ")
     for j, col in enumerate(row):
       print(col, end = " ")
     print("   ")
 print(" "*3+"  a"+" "*2+"b"+" "*2+"c"+" "*2+"d"+" "*2+"e"+" "*2+"f"+" "*2+"g"+" "*2+"h")

print_board(board))
