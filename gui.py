import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import (QMainWindow, QApplication, QLineEdit, QPushButton, QTextEdit,
                               QVBoxLayout, QHBoxLayout, QLabel, QWidget, QScrollArea, QComboBox)

from howdoi import howdoi

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("How Do I")

        self.input = QLineEdit()
        self.Question = QLabel()
        self.Question.setText("Enter your question : ")
        self.input.setPlaceholderText("How do i...")

        self.text = QTextEdit()
        self.text.setText("")
        self.text.setAlignment(Qt.AlignLeft)

        self.button = QPushButton("Search")
        self.button.resize(10, 10)
        self.button.clicked.connect(self.buttonClick)

        HLayout = QHBoxLayout()
        HLayout.addWidget(self.Question)
        HLayout.addWidget(self.input)
        HLayout.addWidget(self.button)

        VLayout = QVBoxLayout()
        VLayout.addLayout(HLayout)
        VLayout.addWidget(self.text)

        Container = QWidget()
        Container.setLayout(VLayout)
        Container.setMinimumSize(650, 480)
        self.setCentralWidget(Container)

    def buttonClick(self):
        self.text.setText(howdoi.howdoi(self.input.text()))




if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()
