from PyQt5.QtWidgets import QApplication, QPushButton, QGridLayout, QLabel, QTextEdit, QWidget

tokens_1 = ('repeat', 'until')
tokens_2 = (':=', ';')
comparators = ('=', '>', '<', '>=', '<=')
# NUM = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
ID = ('x', 'y')


def submit():
    targetRegEx = text_edit.toPlainText()
    targetRegEx = targetRegEx.replace(';', ' ;')

    lexemes = targetRegEx.split()

    print('lexemes list:', lexemes, '\n')

    if lexemes[0] == tokens_1[0]:  # 1st word == 'repeat'
        i = 1
        while lexemes[i] != tokens_1[1]:  # == 'Until'
            if (lexemes[i] in ID) and (lexemes[i + 1] == tokens_2[0]) and (lexemes[i + 2].isdigit() or lexemes[i + 2] in ID) and (lexemes[i + 3] == tokens_2[1]):
                i += 4

            else:
                print('Wrong Expression !')
                exit()

        if(lexemes[i] == tokens_1[1]) and (lexemes[i + 1] in ID) and (lexemes[i + 2] in comparators) and (lexemes[i + 3].isdigit() or lexemes[i + 3] in ID):
            x = 5

        else:
            print('Wrong Expression !')

        print('Accepted Expression :)')

    else:
        print('Wrong Expression !')


app = QApplication([])
main_widget = QWidget()

text_edit = QTextEdit()
label = QLabel('Enter the TINY sample code below !')
submit_button = QPushButton('Submit')
submit_button.clicked.connect(submit)

grid = QGridLayout()
grid.addWidget(label)
grid.addWidget(text_edit)
grid.addWidget(submit_button)

main_widget.setGeometry(300, 300, 400, 400)
main_widget.setWindowTitle('RegEx Checker')
main_widget.setLayout(grid)
main_widget.show()

app.exec()

"""
repeat
x := 5;
y := x;
until x = 5
"""