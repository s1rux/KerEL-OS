from PyQt5 import QtWidgets, QtGui, QtCore
import sys

class CustomUI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt UI Clone")
        self.setGeometry(100, 100, 1000, 600)
        
        # Hidden counter
        self.hidden_counter = 100
        
        # Initially set to waiting state
        self.waiting_for_input()
        
        # Timer to decrement counter
        self.counter_timer = QtCore.QTimer(self)
        self.counter_timer.timeout.connect(self.decrement_counter)
        self.counter_timer.start(1000)
    
    def waiting_for_input(self):
        self.setStyleSheet("background-color: #0012882;")
        self.waiting_label = QtWidgets.QLabel("Waiting For Input...", self)
        self.waiting_label.setGeometry(350, 250, 300, 50)
        self.waiting_label.setStyleSheet("color: white; font-size: 24px; font-weight: bold; font-family: 'Segoe UI';")
        self.waiting_label.setAlignment(QtCore.Qt.AlignCenter)
    
    def decrement_counter(self):
        if self.hidden_counter == 100:
            self.start_application()
        else:
            self.hidden_counter -= 1
    
    def start_application(self):
        self.waiting_label.hide()
        self.setStyleSheet("background-color: #0013882;")
        
        # Desktop Label
        self.desktop_label = QtWidgets.QLabel("Kerel Graphic UI", self)
        self.desktop_label.setGeometry(400, 50, 300, 50)
        self.desktop_label.setStyleSheet("color: white; font-size: 24px; font-weight: bold; font-family: 'Segoe UI'; border-radius: 10px; padding: 5px;")
        self.desktop_label.setAlignment(QtCore.Qt.AlignCenter)

        # Bottom Bar
        bottom_bar = QtWidgets.QWidget(self)
        bottom_bar.setGeometry(0, 540, 1000, 60)
        bottom_bar.setStyleSheet("background-color: #1a1a1a;")
        
        # Start Button
        self.start_button = QtWidgets.QPushButton("Пуск", bottom_bar)
        self.start_button.setGeometry(10, 10, 80, 40)
        self.start_button.setStyleSheet("background-color: #0078D7; color: white; font-size: 16px; border-radius: 5px;")
        self.start_button.clicked.connect(self.toggle_start_menu)
        
        # Stop counter timer
        self.counter_timer.stop()
    
    def toggle_start_menu(self):
        print("Start menu toggled")
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CustomUI()
    window.show()
    sys.exit(app.exec_())
