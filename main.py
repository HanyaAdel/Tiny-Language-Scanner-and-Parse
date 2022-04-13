from PyQt5.QtWidgets import QApplication, QPushButton, QGridLayout, QLabel, QTextEdit, QWidget
from scanner2 import  Scanner
sc = Scanner()

def submit():
    input = text_edit.toPlainText()
    result = sc.scan(input)
    status = result[0]
    tokens = result[1]
    types = result[2]
    status_label.setText("Status: "+status)

    j = 0
    while (j < len(tokens)):
        print('token:', tokens[j], ",type:", types[j])
        j += 1


app = QApplication([])
main_widget = QWidget()

text_edit = QTextEdit()
label = QLabel('Enter the TINY sample code below !')
status_label = QLabel("Status: Waiting...")
submit_button = QPushButton('Submit')
submit_button.clicked.connect(submit)

grid = QGridLayout()
grid.addWidget(label)
grid.addWidget(text_edit)
grid.addWidget(status_label)
grid.addWidget(submit_button)

main_widget.setGeometry(300, 300, 400, 400)
main_widget.setWindowTitle('Lexer')
main_widget.setLayout(grid)
main_widget.show()

app.exec()