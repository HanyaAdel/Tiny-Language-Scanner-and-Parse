from PyQt5.QtWidgets import QApplication, QPushButton, QGridLayout, QLabel, QTextEdit, QWidget

reserved_words = ('repeat', 'until')

comparators = ('=', '>', '<', '>=', '<=')

assignment = (':=')

tokens = (';', '=')

lexemes = []
types = []


def submit():
    targetRegEx = text_edit.toPlainText()

    i = 0  # initial counter that iterates over the targetRegEx string

    while i < len(targetRegEx):

        temp_string = ''

        if targetRegEx[i].isdigit():  # NUM
            temp_string += targetRegEx[i]
            i += 1
            while i < len(targetRegEx):
                if targetRegEx[i].isdigit():
                    temp_string += targetRegEx[i]

                elif targetRegEx[i].isalpha():
                    print('Wrong Token !')
                    exit()
                i += 1
            lexemes.append(temp_string)

        elif targetRegEx[i].isalpha():  # ID # TODO (_)
            temp_string += targetRegEx[i]
            i += 1
            while i < len(targetRegEx) and (targetRegEx[i].isalpha() or targetRegEx[i].isdigit()):
                temp_string += targetRegEx[i]
                i += 1
            lexemes.append(temp_string)

        elif targetRegEx[i] in tokens:  # (';', '=')
            lexemes.append(targetRegEx[i])
            i += 1

        elif targetRegEx[i] == '>' or targetRegEx[i] == '<':  # ('>', '<' '>=', '<=')
            temp_string += targetRegEx[i]
            i += 1
            if i < len(targetRegEx) and targetRegEx[i] == '=':
                temp_string += targetRegEx[i]
                i += 1
            lexemes.append(temp_string)

        elif targetRegEx[i] == ':':  # (':=')
            temp_string += targetRegEx[i]
            i += 1
            if i < len(targetRegEx) and targetRegEx[i] == '=':
                temp_string += targetRegEx[i]
                i += 1
            else:
                print('Wrong Token !')
                exit()
            lexemes.append(temp_string)

        elif targetRegEx[i] == ' ' or targetRegEx[i] == '\t' or targetRegEx[i] == '\n' or targetRegEx[i] == '\0':
            i += 1

        else:
            print('Wrong Expression !')
            exit()

    for i in lexemes:
        if i.isdigit():
            types.append('NUM')
        elif i in comparators:
            types.append('comparators')
        elif i in reserved_words:
            types.append(i)
        elif i in assignment:
            types.append('assignment')
        elif i == ';':
            types.append(';')
        else:
            types.append('ID')

    print('lexemes list:', lexemes, '\n')
    print('types list:', types, '\n')
    exit()


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
main_widget.setWindowTitle('Lexer')
main_widget.setLayout(grid)
main_widget.show()

app.exec()

# targetRegEx = 'repeatxah>=m>s<as<=e;d=5:=5'
