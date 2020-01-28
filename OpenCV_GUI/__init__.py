import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "你好，世界", "Hei maailma",\
            "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World")
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)


        self.text.setFont(QtGui.QFont("Titillium", 30))
        self.button.setFont(QtGui.QFont("Titillium", 20))

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.slider)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.magic)


    def magic(self):
        self.text.setText(random.choice(self.hello))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())