from PyQt6.QtWidgets import QMainWindow, QFrame, QHBoxLayout, QVBoxLayout
from .app import app

main_window = QMainWindow()
main_window.setWindowTitle("Weather app")

primary_screen = app.primaryScreen()
screen_size = primary_screen.size()
screen_width = screen_size.width()
screen_height = screen_size.height()

WIDTH_WINDOW = 1024
HEIGHT_WINDOW = 800

main_window.setGeometry(
    (screen_width // 2) - (WIDTH_WINDOW // 2),
    (screen_height // 2) - (HEIGHT_WINDOW // 2),
    WIDTH_WINDOW,
    HEIGHT_WINDOW
)

central_frame = QFrame(main_window)
central_frame.setStyleSheet("background-color: orange;")
central_frame.setFixedSize(WIDTH_WINDOW, HEIGHT_WINDOW)

main_layout = QHBoxLayout(central_frame)
main_layout.setContentsMargins(10, 10, 10, 10)
main_layout.setSpacing(10)

left_frame = QFrame(central_frame)
left_frame.setStyleSheet("background-color: grey;")
left_frame.setFixedWidth(300)
main_layout.addWidget(left_frame)

right_container = QFrame(central_frame)
right_container.setStyleSheet("background-color: transparent;")
right_layout = QVBoxLayout(right_container)
right_layout.setContentsMargins(0, 0, 0, 0)
right_layout.setSpacing(10)

top_right_frame = QFrame(right_container)
top_right_frame.setStyleSheet("background-color: black;")
top_right_frame.setFixedHeight(60)
right_layout.addWidget(top_right_frame)

middle_right_frame = QFrame(right_container)
middle_right_frame.setStyleSheet("background-color: black;")
right_layout.addWidget(middle_right_frame)

bottom_right_frame = QFrame(right_container)
bottom_right_frame.setStyleSheet("background-color: black;")
right_layout.addWidget(bottom_right_frame)

main_layout.addWidget(right_container)

main_window.setCentralWidget(central_frame)