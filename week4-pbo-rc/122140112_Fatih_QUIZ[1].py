import random

class Minesweeper:
    def __init__(self):
        self.board = [['?' for _ in range(3)] for _ in range(3)]
        # Menetapkan posisi bom secara acak
        self.bomb_row, self.bomb_col = random.randint(0, 2), random.randint(0, 2)
        self.lost = False

    def create_board(self):
        # Menampilkan keadaan papan saat ini
        for i in range(3):
            for j in range(3):
                print(f" [{self.board[i][j]}] ", end="")
                if j < 2:
                    print("|", end="")
            print()
            if i < 2:
                print("-----------")

    def check_for_bomb(self, row, col):
        # Memeriksa apakah sel yang dipilih berisi bom
        return row == self.bomb_row and col == self.bomb_col

    def play_game(self):
        print("Selamat datang di Minesweeper!")
        while not self.lost:
            self.create_board()
            row = int(input("Masukkan baris (0-2): "))
            col = int(input("Masukkan kolom (0-2): "))
            print()

            # Memeriksa apakah input pengguna berada dalam rentang yang valid
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Input tidak valid! Silakan masukkan nomor baris dan kolom antara 0 dan 2.")
                continue

            if not self.check_for_bomb(row, col):
                print("Tidak ada bom di sini! Permainan berlanjut...")
                self.board[row][col] = 0
            else:
                print("Permainan Berakhir! Anda menabrak bom.")
                self.board[row][col] = 'X'
                self.lost = True

game = Minesweeper()
game.play_game()
