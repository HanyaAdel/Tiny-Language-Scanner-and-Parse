from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from grammar import Grammar as grammarInstance


# list_1 = [[1, [0], [], ['repeat', 'identifier', ':=', 'identifier', ';', 'until', 'identifier', '$'], 's5'],
# [2, [0, 5], ['repeat'], ['identifier', ':=', 'identifier', ';', 'until', 'identifier', '$'], 's6'],
# [3, [0, 5, 6], ['repeat', 'identifier'], [':=', 'identifier', ';', 'until', 'identifier', '$'], 's9'],
# [4, [0, 5, 6, 9], ['repeat', 'identifier', ':='], ['identifier', ';', 'until', 'identifier', '$'], 's12'],
# [5, [0, 5, 6, 9, 12], ['repeat', 'identifier', ':=', 'identifier'], [';', 'until', 'identifier', '$'], 'r8'],
# [6, [0, 5, 6, 9, 11], ['repeat', 'identifier', ':=', 'factor'], [';', 'until', 'identifier', '$'], 's15'],
# [7, [0, 5, 6, 9, 11, 15], ['repeat', 'identifier', ':=', 'factor', ';'], ['until', 'identifier', '$'], 'r7'],
# [8, [0, 5, 4], ['repeat', 'assign-stmt'], ['until', 'identifier', '$'], 'r5'],
# [9, [0, 5, 2], ['repeat', 'statement'], ['until', 'identifier', '$'], 'r3'],
# [10, [0, 5, 8], ['repeat', 'stmt-seq'], ['until', 'identifier', '$'], 's10'],
# [11, [0, 5, 8, 10], ['repeat', 'stmt-seq', 'until'], ['identifier', '$'], 's14'],
# [12, [0, 5, 8, 10, 14], ['repeat', 'stmt-seq', 'until', 'identifier'], ['$'], 'r6'],
# [13, [0, 3], ['repeat-stmt'], ['$'], 'r4'],
# [14, [0, 2], ['statement'], ['$'], 'r3'],
# [15, [0, 1], ['stmt-seq'], ['$'], 'acc']]


class StackTable(QDialog):
    def __init__(self, parse_list, parent=None):
        super().__init__(parent)
        loadUi('table_widget.ui', self)

        self.tableWidget.setColumnWidth(0, 250)
        self.tableWidget.setColumnWidth(1, 350)
        self.tableWidget.setColumnWidth(2, 400)
        self.tableWidget.setColumnWidth(3, 370)

        self.tableWidget.setRowCount(len(parse_list))

        for i in range(len(parse_list)):
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(' '.join(str(element) for element in parse_list[i][1])))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(' '.join(parse_list[i][2])))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(' '.join(parse_list[i][3])))

            result = parse_list[i][4]

            if parse_list[i][4][0] == 'r':
                reduce_index = int(parse_list[i][4][1])
                result = result + ': ' + str(grammarInstance.leftOp_dict[reduce_index]) + '-> ' + str(' '.join(grammarInstance.rightOp_dict[reduce_index]))

            self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(result))