#main widget

from PySide2.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, QVBoxLayout, QMessageBox


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main widget")
        self.setMinimumSize(640, 480)

        button = QPushButton("Press me!", self)
        button.clicked.connect(self.onButtonClicked)
        button.move(30, 30)


        self.edit = QLineEdit(self)
        #self.label = QLabel("tekst", self)

        layout = QVBoxLayout(self)
        layout.addWidget(self.edit)
        #layout.addWidget(self.label)
        layout.addWidget(button)


        #self.label.move(100, 0)
        #self.lebel.setFixedWidth(300)




    def onButtonClicked(self):
        editText = self.edit.text()
       # self.label.setText(editText)
        QMessageBox.information(self, "Info","editText")