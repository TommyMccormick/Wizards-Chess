#import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel
import chess

# GUI
app = QApplication([]) # Initialize the application (takes command-line arguments)

window = QWidget()  # Create the main window (an empty window for now)
window.setWindowTitle("PyQt6 Chess Game")  # Set the window title
window.resize(400, 400)  # Set the window size (you can adjust this)

layout = QGridLayout()  # Create a grid layout to arrange widgets
window.setLayout(layout)  # Set the layout to the window

window.show()  # Show the window
app.exec()  # Start the event loop (keeps the window open)

# Colors for light and dark squares
white = "#ffffff"
black = "#000000"
# silver = "#bcbcbc"

# Create QLabel for each square and set the background color
for row in range(8):
    for col in range(8):
        label = QLabel()
        # Apply color alternation logic based on row and column
        if (row + col) % 2 == 0:
            label.setStyleSheet(f"background-color: {white}")
        else: # (row + col) % 2 != 0
            label.setStyleSheet(f"background-color: {black}")
        
        # Add the label to the grid layout at position (row, col)
        layout.addWidget(label, row, col)

# LOGIC
chess.Board()
