from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout,
    QWidget, QLabel, QFrame
)
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtCore import Qt
import subprocess

class LexerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Analizador Léxico Bryan Marc 1190040')
        self.setGeometry(100, 100, 900, 600)
        self.setStyleSheet("background-color: #2E2E2E; color: #FFFFFF;")

     
        self.inputLabel = QLabel('Entrada:', self)
        self.inputLabel.setStyleSheet("font-size: 16px; font-weight: bold;")

        self.textEdit = QTextEdit(self)
        self.textEdit.setStyleSheet("background-color: #1E1E1E; color: #FFFFFF; font-size: 14px;")

        self.runButton = QPushButton('Run', self)
        self.runButton.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 5px;
                font-size: 16px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.runButton.clicked.connect(self.runLexer)

        self.outputLabel = QLabel('Salida:', self)
        self.outputLabel.setStyleSheet("font-size: 16px; font-weight: bold;")

        self.resultEdit = QTextEdit(self)
        self.resultEdit.setReadOnly(True)
        self.resultEdit.setStyleSheet("background-color: #1E1E1E; color: #FFFFFF; font-size: 14px;")

     
        inputLayout = QVBoxLayout()
        inputLayout.addWidget(self.inputLabel)
        inputLayout.addWidget(self.textEdit)
        inputLayout.addWidget(self.runButton)

        outputLayout = QVBoxLayout()
        outputLayout.addWidget(self.outputLabel)
        outputLayout.addWidget(self.resultEdit)

        mainLayout = QHBoxLayout()
        mainLayout.addLayout(inputLayout, 1)
        mainLayout.addLayout(outputLayout, 1)

        container = QWidget()
        container.setLayout(mainLayout)
        self.setCentralWidget(container)

    def runLexer(self):
        input_text = self.textEdit.toPlainText()
        with open('lexer/input.txt', 'w') as f:
            f.write(input_text)

 
        result = subprocess.run(['bash', '-c', './lexer/lexer < lexer/input.txt'], capture_output=True, text=True)
        self.resultEdit.setPlainText(result.stdout)

if __name__ == '__main__':
    app = QApplication([])
    lexerApp = LexerApp()
    lexerApp.show()
    app.exec_()
