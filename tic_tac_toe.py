import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe XO")
        self.board = [[' ']*3 for _ in range(3)]
        self.players = ['X', 'O']
        self.turn = 0

        self.buttons = [[None]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.master, text=' ', font=('Arial', 20), width=6, height=3,
                                                command=lambda row=i, col=j: self.make_move(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            player = self.players[self.turn % 2]
            self.board[row][col] = player
            self.buttons[row][col].config(text=player)
            if self.check_winner(player):
                messagebox.showinfo("Winner", f"Player {player} wins!")
                self.reset_board()
            elif self.is_board_full():
                messagebox.showinfo("Tie", "It's a tie!")
                self.reset_board()
            else:
                self.turn += 1

    def check_winner(self, player):
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or \
               all(self.board[j][i] == player for j in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)) or \
           all(self.board[i][2-i] == player for i in range(3)):
            return True
        return False

    def is_board_full(self):
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))

    def reset_board(self):
        self.board = [[' ']*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=' ')

def main():
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

if __name__ == "__main__":
    main()
