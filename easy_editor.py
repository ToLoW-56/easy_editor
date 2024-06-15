import json
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, \
    QHBoxLayout, QVBoxLayout

app = QApplication([])
notes = []

'''Інтерфейс'''
# Параметри вікна
window = QWidget()
window.setWindowTitle('Розумні нотатки')
window.resize(900, 600) 
