from PyQt5.QtWidgets import QApplication, QPushButton, QGridLayout, QLabel, QTextEdit, QWidget
from scanner import Scanner
from dfa import dfa
from graph import Graph
sc = Scanner()
dfa = dfa()
dfaresult = []
def submit():
    global  dfaresult
    input = text_edit.toPlainText()
    result = sc.scan(input)
    status = result[0]
    tokens = result[1]
    types = result[2]
    scanner_status_label.setText("Scanner status: "+status)

    j = 0
    while (j < len(tokens)):
        print('token:', tokens[j], ",type:", types[j])
        j += 1
    if(status=='Accepted'):
        dfa_button.setEnabled(True)
        dfaresult = dfa.scan(types)
        syntax_status_label.setText("Syntax status: " + dfaresult[0])
    else:
        dfa_button.setEnabled(False)

def showdfa():
    global dfaresult
    Graph(dfaresult[1])



app = QApplication([])
main_widget = QWidget()

text_edit = QTextEdit()
label = QLabel('Enter the TINY sample code below !')
scanner_status_label = QLabel("Scanner status: Waiting...")
syntax_status_label = QLabel("Syntax status: Waiting...")
submit_button = QPushButton('Submit')
dfa_button = QPushButton('Show DFA')
submit_button.clicked.connect(submit)
dfa_button.setEnabled(False)
dfa_button.clicked.connect(showdfa)

grid = QGridLayout()
grid.addWidget(label)
grid.addWidget(text_edit)
grid.addWidget(scanner_status_label)
grid.addWidget(syntax_status_label)
grid.addWidget(submit_button)
grid.addWidget(dfa_button)

main_widget.setGeometry(300, 300, 400, 400)
main_widget.setWindowTitle('Lexer')
main_widget.setLayout(grid)
main_widget.show()

app.exec()