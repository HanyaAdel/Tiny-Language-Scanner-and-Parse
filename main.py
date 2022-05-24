from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QTextEdit, QWidget, QTableWidget, \
    QTableWidgetItem, QHBoxLayout, QVBoxLayout
from grammar import Grammar
from scanner import Scanner
from dfa import dfa
from graph import Graph
from stack_table import StackTable
from tree import display

sc = Scanner()
gr = Grammar()
dfa = dfa()
dfaresult = []


def submit():
    global dfaresult
    input = text_edit.toPlainText()
    result = sc.scan(input)
    status = result[0]
    tokens = result[1]
    types = result[2]
    gr.func(types, tokens)
    scanner_status_label.setText("Scanner status: " + status)

    j = 0
    while j < len(tokens):
        print('token:', tokens[j], ",type:", types[j])
        j += 1
    if status == 'Accepted':
        dfa_button.setEnabled(True)
        dfaresult = dfa.scan(types)
        syntax_status_label.setText("Syntax status: " + dfaresult[0])
    else:
        dfa_button.setEnabled(False)
        types[len(types) - 1] = "illegal token"  # modify this
    populateTable(tokens, types)


def showdfa():
    global dfaresult
    Graph(dfaresult[1])


def populateTable(tokens, types):
    row = 0
    while row < len(tokens):
        table.setRowCount(len(tokens))
        table.setItem(row, 0, QTableWidgetItem(tokens[row]))
        table.setItem(row, 1, QTableWidgetItem(types[row]))
        row += 1

    # table.insertRow(currentrowcount,0,QTableWidgetItem("Some text"))


def show_stack_table():
    dialog = StackTable(parse_list=gr.stack_table)
    dialog.exec_()

def draw_tree():
    display()


app = QApplication([])
main_widget = QWidget()

text_edit = QTextEdit()
text_edit.setTabStopWidth(15)
label = QLabel('Enter the TINY sample code below !')
scanner_status_label = QLabel("Scanner status: Waiting...")
syntax_status_label = QLabel("Syntax status: Waiting...")
submit_button = QPushButton('Submit')
dfa_button = QPushButton('Show DFA')
stack_button = QPushButton('Show Stack Table')
tree_button = QPushButton('Show Parse Tree')
submit_button.clicked.connect(submit)
dfa_button.setEnabled(False)
dfa_button.clicked.connect(showdfa)
stack_button.clicked.connect(show_stack_table)
tree_button.clicked.connect(draw_tree)

table = QTableWidget()
table.setColumnCount(2)

table.setHorizontalHeaderLabels(["Token", "Type"])
table.horizontalHeader().setStretchLastSection(True)

# grid = QGridLayout()
grid = QVBoxLayout()
grid.addWidget(label)
subgrid = QHBoxLayout()
subgrid.addWidget(text_edit)
subgrid.addWidget(table)
# grid.addWidget(text_edit)
grid.addLayout((subgrid))
grid.addWidget(scanner_status_label)
grid.addWidget(syntax_status_label)
grid.addWidget(submit_button)
grid.addWidget(dfa_button)
grid.addWidget(stack_button)
grid.addWidget(tree_button)
# grid.addWidget(tableWidget)


# main_widget.setGeometry(500, 500, 900, 700)
main_widget.setFixedSize(900, 500)

main_widget.setWindowTitle('Lexer')
main_widget.setLayout(grid)
main_widget.show()

app.exec()
