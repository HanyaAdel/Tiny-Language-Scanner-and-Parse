# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
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


class StackTable(QtWidgets.QDialog):
    def __init__(self, parse_list, parent=None):
        super().__init__(parent)
        self.setObjectName("Dialog")
        self.resize(1450, 800)
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 1411, 771))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setColumnWidth(0, 250)
        self.tableWidget.setColumnWidth(1, 350)
        self.tableWidget.setColumnWidth(2, 400)
        self.tableWidget.setColumnWidth(3, 370)
        self.tableWidget.setRowCount(len(parse_list))
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)

        self.retranslateUi(self, parse_list=parse_list)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog, parse_list):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "States"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Stack"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Input"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Action"))

        for i in range(len(parse_list)):
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(' '.join(str(element) for element in parse_list[i][1])))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(' '.join(parse_list[i][2])))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(' '.join(parse_list[i][3])))

            result = parse_list[i][4]

            if parse_list[i][4][0] == 'r':
                reduce_index = int(parse_list[i][4][1])
                result = result + ': ' + str(grammarInstance.leftOp_dict[reduce_index]) + '-> ' + str(' '.join(grammarInstance.rightOp_dict[reduce_index]))

            self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(result))
