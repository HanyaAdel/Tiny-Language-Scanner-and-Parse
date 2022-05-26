from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *



parseTable = [
                ["State", "Actions (terminal)", "Go to (non-terminals)"],
                ["", "repeat", "until", "identifier", "number",     "$",    ":=",   ";", "stmt-seq", "statement", "repeat-stmt", "assign-stmt", "factor"],
                ["0",    "s5",      "",       "s6",        "",         "",      "",    "",    '1',         '2',            '3',          '4',          ""],
                ["1",    "s5",      "",       "s6",        "",         "acc",   "",    "",    "",          '7',            '3',          '4',          ""],
                ["2",     "r3",    "r3",      "r3",        "",         "r3",    "",    "",    "",          "",             "",             "",         ""],
                ["3",     "r4",    "r4",      "r4",        "",         "r4",    "",    "",    "",          "",             "",             "",         ""],
                ["4",     "r5",    "r5",      "r5",        "",         "r5",    "",    "",    "",          "",             "",             "",         ""],
                ["5",     "s5",     "",       "s6",        "",          "",     "",    "",    '8',        '2',             '3',           '4',          ""],
                ["6",      "",      "",         "",        "",          "",     "",   "s9",   "",          "",             "",             "",         ""],
                ["7",     "r2",    "r2",      "r2",        "",         "r2",    "",    "",    "",          "",             "",             "",         ""],
                ['8',     "s5",   "s10",      "s6",        "",          "",     "",    "",    "",         '7',             '3',           '4',          ""],
                ['9',      "",      "",       "s12",     "s13",         "",     "",    "",    "",          "",             "",             "",        '11'],
                ['10',     "",      "",       "s14",       "",          "",     "",    "",    "",          "",             "",             "",         ""],
                ['11',     "",      "",         "",        "",          "",     "",   "s15",  "",          "",             "",             "",         ""],
                ['12',     "",      "",         "",        "",          "",     "",   "r8",   "",          "",             "",             "",         ""],
                ['13',     "",      "",         "",        "",          "",     "",   "r9",   "",          "",             "",             "",         ""],
                ['14',    "r6",     "r6",      "r6",       "",         "r6",    "",    "",    "",          "",             "",             "",         ""],
                ['15',    "r7",     "r7",      "r7",       "",         "r7",    "",    "",    "",          "",             "",             "",         ""],

]

class ParseTable(QDialog):


    

    def __init__(self, parent=None):
        super().__init__(parent)

        
        reductions =  QLabel()
        reductions.setText("r1: stmt-seq’ -> stmt-seq \n" + 
        "r2: stmt-seq -> stmt-seq statement \n" +
        "r3: stmt-seq -> statement \n" +
        "r4: statement -> repeat-stmt \n" +
        "r5: statement -> assign-stmt \n" +
        "r6: repeat-stmt -> repeat stmt-seq until identifier \n" +
        "r7: assign-stmt -> identifier := factor ; \n" +
        "r8: factor -> identifier \n" +
        "r9: factor -> number\n" )

        reductions.setFont(QFont('Arial', 15))
        

        
        table = QTableWidget()
        table.setColumnCount(13)

        i = 0
        while i < 13:
            table.setColumnWidth(i, 50)
            i+=1
        
        
        table.horizontalHeader().hide()
        table.verticalHeader().hide()


        grid = QVBoxLayout()

        subgrid = QHBoxLayout()
        subgrid.addWidget(table)
        subgrid.addWidget(reductions)

        grid.addLayout(subgrid)

        
        self.setFixedSize(1200, 650)
        self.setLayout(grid)
        self.setWindowTitle("Parse Table")

        print(len(parseTable))
        table.setRowCount(len(parseTable))
        table.setSpan(0, 1, 1, 7)
        table.setSpan(0, 8, 1, 5)

        for i in range(len(parseTable)):
            table.setRowHeight(i, 35)
            if i == 0:
                item1 = QTableWidgetItem(parseTable[i][0])
                item1.setTextAlignment(QtCore.Qt.AlignHCenter)

                item2 = QTableWidgetItem(parseTable[i][1])
                item2.setTextAlignment(QtCore.Qt.AlignHCenter)

                item3 = QTableWidgetItem(parseTable[i][2])
                item3.setTextAlignment(QtCore.Qt.AlignHCenter)

                table.setItem(i, 0, item1)
                table.setItem(i, 1, item2)
                table.setItem(i, 8, item3)  

            else:
                for j in range (len(parseTable[i])):

                    item1 = QTableWidgetItem(parseTable[i][j])
                    item1.setTextAlignment(QtCore.Qt.AlignHCenter)
                    table.setItem(i, j, item1)




        

