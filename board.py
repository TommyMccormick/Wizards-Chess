import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel
from PyQt6.QtGui import QPixmap, QMouseEvent
import chess

class ChessBoard(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Chess Game with PyQt6")  # Set the window title
        self.setGeometry(100, 100, 600, 600)  # Set the window size

        layout = QGridLayout()  # Create a grid layout to arrange widgets
        self.setLayout(layout)  # Set the layout to the window

        # Colors for light and dark squares
        white = "#ffffff"
        black = "#7e7e7e" # Black with my black pawns doesnt show them on black squares

        # Map pieces to images
        piece_dict = {
            "K": "images/white_king.png",
            "Q": "images/white_queen.png",
            "R": "images/white_rook.png",
            "B": "images/white_bishop.png",
            "N": "images/white_knight.png",
            "P": "images/white_pawn.png",
            "k": "images/black_king.png",
            "q": "images/black_queen.png",
            "r": "images/black_rook.png",
            "b": "images/black_bishop.png",
            "n": "images/black_knight.png",
            "p": "images/black_pawn.png",
        }

        # Setting up the initial positions for a game
        starting_positions = [
            ["R", "N", "B", "Q", "K", "B", "N", "R"],  # 1st row (White pieces)
            ["P", "P", "P", "P", "P", "P", "P", "P"],  # 2nd row (White pawns)
            ["", "", "", "", "", "", "", ""],  # 3rd row
            ["", "", "", "", "", "", "", ""],  # 4th row
            ["", "", "", "", "", "", "", ""],  # 5th row
            ["", "", "", "", "", "", "", ""],  # 6th row
            ["p", "p", "p", "p", "p", "p", "p", "p"],  # 7th row (Black pawns)
            ["r", "n", "b", "q", "k", "b", "n", "r"],  # 8th row (Black pieces)
        ]

        # Create QLabel for each square and set the background color
        for row in range(8):
            for col in range(8):
                square = QLabel()
                square.setFixedSize(70, 70)

                # Color alternation logic based on row and column
                if (row + col) % 2 == 0:
                    square.setStyleSheet(f"background-color: {white}")
                else: # (row + col) % 2 != 0
                    square.setStyleSheet(f"background-color: {black}")

                # Place pieces on the board in the correct spaces
                piece = starting_positions[row][col]
                if piece:  # If there's a piece in this position
                    piece_path = piece_dict.get(piece, "")
                    print(f"Placing {piece} at ({row}, {col})")
                    if os.path.exists(piece_path): # Ensure image exists
                        # QPixmap is for handling images efficiently
                        pixmap = QPixmap(piece_path).scaled(40, 40)  # Resize to fit square
                        square.setPixmap(pixmap)
                        print(f"✔ Image applied for {piece} at ({row}, {col})")
                    else:
                        print(f"❌ Missing image for {piece} at ({row}, {col})")
                layout.addWidget(square, row, col)

        self.setLayout(layout)  # Ensure layout is set
        self.update()           # Force UI update
        self.repaint()          # Refresh display
        # self.update()
        # self.repaint()

# LOGIC
# chess.Board()



#f __name__ == "__main__":
app = QApplication(sys.argv)
window = ChessBoard()
window.show()
sys.exit(app.exec())