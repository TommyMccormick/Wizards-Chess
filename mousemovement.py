from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QMouseEvent
import sys

class MouseMovement(QWidget):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True) # Enables mouse tracking

    def mousePressEvent(self, event: QMouseEvent):
        print(f"Mouse clicked at ({event.position().x()}, {event.position().y()})")