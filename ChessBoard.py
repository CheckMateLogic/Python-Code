import tkinter as tk

class ChessBoard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chess Board")
        self.canvas = tk.Canvas(self, width=400, height=400)
        self.canvas.pack()
        self.draw_board()
        self.add_pieces()
        self.add_pieces()
    def draw_board(self):
        colors = ["white", "lightgreen"]
        for row in range(8):
            for col in range(8):
                color = colors[(row + col) % 2]
                x1 = col * 50
                y1 = row * 50
                x2 = x1 + 50
                y2 = y1 + 50
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
    def add_pieces(self):
        pieces = [
            ("R", 0, 0), ("N", 0, 1), ("B", 0, 2), ("Q", 0, 3), ("K", 0, 4), ("B", 0, 5), ("N", 0, 6), ("R", 0, 7),
            ("P", 1, 0), ("P", 1, 1), ("P", 1, 2), ("P", 1, 3), ("P", 1, 4), ("P", 1, 5), ("P", 1, 6), ("P", 1, 7),
            ("p", 6, 0), ("p", 6, 1), ("p", 6, 2), ("p", 6, 3), ("p", 6, 4), ("p", 6, 5), ("p", 6, 6), ("p", 6, 7),
            ("r", 7, 0), ("n", 7, 1), ("b", 7, 2), ("q", 7, 3), ("k", 7, 4), ("b", 7, 5), ("n", 7, 6), ("r", 7, 7)
        ]
        for piece, row, col in pieces:
            x = col * 50 + 25
            y = row * 50 + 25
            self.canvas.create_text(x, y, text=piece, font=("Arial", 24))
if __name__ == "__main__":
    app = ChessBoard()
    app.mainloop()
