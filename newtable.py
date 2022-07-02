# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test1.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import serial

ser = serial.Serial('COM5', 4800, timeout=0)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("GPGSV")
        MainWindow.resize(597, 250)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(5, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(6, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(7, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(8, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(9, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(10, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(11, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(12, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(13, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 0, 0, 200))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 0, 0, 39))
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(4, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(4, 1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(4, 2, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(5, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(5, 1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(5, 2, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(6, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(6, 1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(6, 2, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(7, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(7, 1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(7, 2, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(8, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(8, 1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(8, 2, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(9, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(9, 1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(9, 2, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(10, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(10, 1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(10, 2, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(11, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(11, 1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(11, 2, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(12, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(12, 1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(12, 2, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(13, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(13, 1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(13, 2, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(14, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(14, 1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(14, 2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(180)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(60)
        self.tableWidget.verticalHeader().setDefaultSectionSize(33)
        self.verticalLayout.addWidget(self.tableWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 597, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #self.pushButtonStart.clicked.connect(self.page2)
        self.qTimer = QTimer()
        # set interval to 1 s
        self.qTimer.setInterval(2000) # 1000 ms = 1 s
        # connect timeout signal to signal handler
        self.qTimer.start()
        self.qTimer.timeout.connect(self.data)
        #self.pushButtonStart.clicked.connect(self.call_program)
        # start timer

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        # item.setText(_translate("MainWindow", "5"))
        # item = self.tableWidget.verticalHeaderItem(5)
        # item.setText(_translate("MainWindow", "6"))
        # item = self.tableWidget.verticalHeaderItem(6)
        # item.setText(_translate("MainWindow", "7"))
        # item = self.tableWidget.verticalHeaderItem(7)
        # item.setText(_translate("MainWindow", "8"))
        # item = self.tableWidget.verticalHeaderItem(8)
        # item.setText(_translate("MainWindow", "9"))
        # item = self.tableWidget.verticalHeaderItem(9)
        # item.setText(_translate("MainWindow", "10"))
        # item = self.tableWidget.verticalHeaderItem(10)
        # item.setText(_translate("MainWindow", "11"))
        # item = self.tableWidget.verticalHeaderItem(11)
        # item.setText(_translate("MainWindow", "12"))
        # item = self.tableWidget.verticalHeaderItem(12)
        # item.setText(_translate("MainWindow", "13"))
        # item = self.tableWidget.verticalHeaderItem(13)
        # item.setText(_translate("MainWindow", "14"))
        # item = self.tableWidget.verticalHeaderItem(14)
        # item.setText(_translate("MainWindow", "15"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Satellite Number"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Elevation Angle"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Azimuth Angle"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)


    def data(self):
        global data_li
        while True :
            data_raw = str(ser.readline())
            data_li = list(data_raw.split(","))
            if (data_li[0]=='b\'$GPGSV'):
                try:
                    sat_no1 = data_li[4]
                    elev1 = data_li[5]
                    azi1 = data_li[6]
                except:
                    sat_no1 = "0"
                    elev1 = "0"
                    azi1 = "0"
                # print("data over1")

                try:
                    sat_no2 = data_li[8]
                    elev2 = data_li[9]
                    azi2 = data_li[10]
                except:
                    sat_no2 = "0"
                    elev2 = "0"
                    azi2 = "0"
                # print("Data over2")

                try:                    
                    sat_no3 = data_li[12]
                    elev3 = data_li[13]
                    azi3 = data_li[14]
                except:
                    sat_no3 = "0"
                    elev3 = "0"
                    azi3 = "0"
                # print("data over3")

                try:
                    sat_no4 = data_li[16]
                    elev4 = data_li[17]
                    azi4 = data_li[18] 
                except:
                    sat_no4 = "0"
                    elev4 = "0"
                    azi4 = "0"
                

                __sortingEnabled = self.tableWidget.isSortingEnabled()
                self.tableWidget.setSortingEnabled(False)
                
                item = self.tableWidget.item(0, 0)
                item.setText(sat_no1)

                item = self.tableWidget.item(0, 1)
                item.setText(elev1)

                item = self.tableWidget.item(0, 2)
                item.setText(azi1)

                item = self.tableWidget.item(1, 0)
                item.setText(sat_no2)

                item = self.tableWidget.item(1, 1)
                item.setText(elev2)

                item = self.tableWidget.item(1, 2)
                item.setText(azi2)

                item = self.tableWidget.item(2, 0)
                item.setText(sat_no3)

                item = self.tableWidget.item(2, 1)
                item.setText(elev3)

                item = self.tableWidget.item(2, 2)
                item.setText(azi3)

                item = self.tableWidget.item(3, 0)
                item.setText(sat_no4)

                item = self.tableWidget.item(3, 1)
                item.setText(elev4)

                item = self.tableWidget.item(3, 2)
                item.setText(azi4)

                # item = self.tableWidget.item(4, 0)
                # item.setText(sat_no1)

                # item = self.tableWidget.item(4, 1)
                # item.setText(elev1)

                # item = self.tableWidget.item(4, 2)
                # item.setText(azi1)

                # item = self.tableWidget.item(5, 0)
                # item.setText(sat_no2)

                # item = self.tableWidget.item(5, 1)
                # item.setText(elev2)

                # item = self.tableWidget.item(5, 2)
                # item.setText(azi2)

                # item = self.tableWidget.item(6, 0)
                # item.setText(sat_no3)

                # item = self.tableWidget.item(6, 1)
                # item.setText(elev3)

                # item = self.tableWidget.item(6, 2)
                # item.setText(azi3)

                # item = self.tableWidget.item(7, 0)
                # item.setText(sat_no4)

                # item = self.tableWidget.item(7, 1)
                # item.setText(elev4)

                # item = self.tableWidget.item(7, 2)
                # item.setText(azi4)

                # item = self.tableWidget.item(8, 0)
                # item.setText(sat_no1)

                # item = self.tableWidget.item(8, 1)
                # item.setText(elev1)

                # item = self.tableWidget.item(8, 2)
                # item.setText(azi1)

                # item = self.tableWidget.item(9, 0)
                # item.setText(sat_no2)

                # item = self.tableWidget.item(9, 1)
                # item.setText(elev2)

                # item = self.tableWidget.item(9, 2)
                # item.setText(azi2)

                # item = self.tableWidget.item(10, 0)
                # item.setText(sat_no3)

                # item = self.tableWidget.item(10, 1)
                # item.setText(elev3)

                # item = self.tableWidget.item(10, 2)
                # item.setText(azi3)

                # item = self.tableWidget.item(11, 0)
                # item.setText(sat_no4)

                # item = self.tableWidget.item(11, 1)
                # item.setText(elev4)

                # item = self.tableWidget.item(11, 2)
                # item.setText(azi4)
                # item = self.tableWidget.item(12, 0)
                # item.setText(sat_no1)

                # item = self.tableWidget.item(12, 1)
                # item.setText(elev1)

                # item = self.tableWidget.item(12, 2)
                # item.setText(azi1)

                # item = self.tableWidget.item(13, 0)
                # item.setText(sat_no2)

                # item = self.tableWidget.item(13, 1)
                # item.setText(elev2)

                # item = self.tableWidget.item(13, 2)
                # item.setText(azi2)

                # item = self.tableWidget.item(14, 0)
                # item.setText(sat_no3)

                # item = self.tableWidget.item(14, 1)
                # item.setText(elev3)

                # item = self.tableWidget.item(14, 2)
                # item.setText(azi3)

                self.tableWidget.setSortingEnabled(__sortingEnabled)
                break

        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
