# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'max_input.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from ui3 import Ui_AllocInput

Max = None
class Ui_MaxInput(object):

    def setupUi(self, MaxInput, pNum, rNum):
        global Max
        self.procN = pNum
        self.resN = rNum
        Max = np.empty((int(self.procN), int(self.resN)), int)
        MaxInput.setObjectName("MaxInput")
        MaxInput.resize(357, 446)
        self.tableWidget = QtWidgets.QTableWidget(MaxInput)
        self.tableWidget.setGeometry(QtCore.QRect(20, 60, 321, 301))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(int(self.resN))
        self.tableWidget.setRowCount(int(self.procN))
        self.pushButton = QtWidgets.QPushButton(MaxInput)
        self.pushButton.setGeometry(QtCore.QRect(140, 390, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(MaxInput)
        self.label.setGeometry(QtCore.QRect(130, 20, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.MaxInput = MaxInput
        self.retranslateUi(MaxInput)
        QtCore.QMetaObject.connectSlotsByName(MaxInput)


    def retranslateUi(self, MaxInput):
        _translate = QtCore.QCoreApplication.translate
        MaxInput.setWindowTitle(_translate("MaxInput", "Max input"))
        self.pushButton.setText(_translate("MaxInput", "Enter"))
        self.label.setText(_translate("MaxInput", "Max Needed"))

    def enter_clicked(self):
        global Max
        for row in range(self.tableWidget.rowCount()):
            for column in range(self.tableWidget.columnCount()):
                Max[row, column] = int(self.tableWidget.item(row, column).text())
        self.loadNext()

    def loadNext(self):
        self.AllocInput = QtWidgets.QDialog()
        self.ui = Ui_AllocInput()
        self.ui.setupUi(self.AllocInput, self.procN, self.resN)
        self.AllocInput.show()
        self.MaxInput.hide()

        self.ui.pushButton.clicked.connect(self.ui.enter_clicked)