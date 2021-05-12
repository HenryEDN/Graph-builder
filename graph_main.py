# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
from PyQt5.QtGui import QIcon

def extractor(value):
    value = list(value)
    for i in value:
        if i == '^':
            index = value.index(i)
            value[index] = '**'
    return ''.join(value)

def check_func(func):
    x = 5
    try:
        eval(extractor(func))
    except ZeroDivisionError:
        return 'ZeroDivisionError'
    except SyntaxError:
        return 'SyntaxError'
    return False

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(543, 325)
        mainWindow.setStyleSheet("background-color: #D2CECE")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setStyleSheet("background-color: white")
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 190, 100, 30))
        self.pushButton.setStyleSheet("background-color: #D2CECE")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(11, 41, 86, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(103, 41, 133, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText('x^2')
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(11, 67, 25, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(103, 67, 133, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(103, 93, 133, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(11, 93, 29, 16))
        self.label_3.setObjectName("label_3")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(275, 30, 251, 192))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 190, 100, 30))
        self.pushButton_2.setStyleSheet("background-color: #D2CECE")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 110, 20, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(390, 230, 20, 31))
        self.label_5.setObjectName("label_5")
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 543, 21))
        self.menubar.setObjectName("menubar")
        self.menuDetail = QtWidgets.QMenu(self.menubar)
        self.menuDetail.setObjectName("menuDetail")
        mainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuDetail.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
    
        self.pushButton.clicked.connect(lambda: self.draw())
        self.pushButton_2.clicked.connect(lambda: self.clear())

    def draw(self):
        self.statusbar.showMessage('')
        self.graphicsView.clear()
        func = self.lineEdit.text()
        if func == '':
            self.statusbar.showMessage("Please, input your function")
            return None
        elif check_func(func) == 'ZeroDivisionError':
            self.statusbar.showMessage('Function Zero division error')
            return None
        elif check_func(func) == 'SyntaxError':
            self.statusbar.showMessage('Probably, you\'re entered the wrong arithmetic symbol.\nTry to use (*, /, -, +, ^) and try again.\n')
            return None
        
        result_x = []
        result_y = []
        extrenum = None
        try:    
            for x in range(int(self.lineEdit_2.text()),int(self.lineEdit_3.text())+1):
                try:
                    result_x.insert(0, x)
                    result_y.insert(0, round(eval(extractor(func)), 2))
                except ZeroDivisionError:
                    extrenum = x
                    result_y.insert(0, 0)
            self.graphicsView.plot(result_x, result_y)
        except ValueError:
            self.statusbar.showMessage("Please, input your x min or x max")
            pass
        except TypeError:
            self.statusbar.showMessage("Please, don't use float numbers")
            pass


    def clear(self):
        self.graphicsView.clear()
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Graph"))
        self.pushButton.setText(_translate("mainWindow", "Submit"))
        self.label.setText(_translate("mainWindow", "Type function y ="))
        self.label_2.setText(_translate("mainWindow", "X min"))
        self.label_3.setText(_translate("mainWindow", "X max"))
        self.pushButton_2.setText(_translate("mainWindow", "Clear"))
        self.label_4.setText(_translate("mainWindow", "    Y"))
        self.label_5.setText(_translate("mainWindow", "    X"))
        self.menuDetail.setTitle(_translate("mainWindow", "Detail"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
