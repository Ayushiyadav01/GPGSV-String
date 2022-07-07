from PyQt5 import QtCore, QtGui, QtWidgets
import serial
from PyQt5.QtCore import QTimer
# ser = serial.Serial('COM5', 4800, timeout=0)

from fgpgsv import Ui_SecondWindow, ser

class Ui_MainWindow(object):

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SecondWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(635, 384)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LE_long = QtWidgets.QLabel(self.centralwidget)
        self.LE_long.setGeometry(QtCore.QRect(20, 40, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.LE_long.setFont(font)
        self.LE_long.setObjectName("LE_long")
        self.LE_lat = QtWidgets.QLabel(self.centralwidget)
        self.LE_lat.setGeometry(QtCore.QRect(20, 130, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.LE_lat.setFont(font)
        self.LE_lat.setObjectName("LE_lat")
        self.LE_UTC = QtWidgets.QLabel(self.centralwidget)
        self.LE_UTC.setGeometry(QtCore.QRect(20, 220, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.LE_UTC.setFont(font)
        self.LE_UTC.setObjectName("LE_UTC")
        self.pushButtonStart = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openWindow())
        self.pushButtonStart.setGeometry(QtCore.QRect(480, 280, 121, 41))
        self.pushButtonStart.setObjectName("pushButtonStart")
        self.Long_value = QtWidgets.QLabel(self.centralwidget)
        self.Long_value.setGeometry(QtCore.QRect(220, 30, 361, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Long_value.setFont(font)
        self.Long_value.setObjectName("Long_value")
        self.lat_value = QtWidgets.QLabel(self.centralwidget)
        self.lat_value.setGeometry(QtCore.QRect(220, 120, 361, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lat_value.setFont(font)
        self.lat_value.setObjectName("lat_value")
        self.UTC_value = QtWidgets.QLabel(self.centralwidget)
        self.UTC_value.setGeometry(QtCore.QRect(220, 210, 361, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.UTC_value.setFont(font)
        self.UTC_value.setObjectName("UTC_value")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 635, 26))
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
        self.qTimer.setInterval(1000) # 1000 ms = 1 s
        # connect timeout signal to signal handler
        self.qTimer.start()
        self.qTimer.timeout.connect(self.show_data)
        # self.pushButtonStart.clicked.connect(self.show_gpgsv)
        # start timer
        
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.LE_long.setText(_translate("MainWindow", "Longitude  ="))
        self.LE_lat.setText(_translate("MainWindow", "Latitude     ="))
        self.LE_UTC.setText(_translate("MainWindow", "UTC          ="))
        self.pushButtonStart.setText(_translate("MainWindow", "GPGSV"))
        self.Long_value.setText(_translate("MainWindow", "0"))
        self.lat_value.setText(_translate("MainWindow", "0"))
        self.UTC_value.setText(_translate("MainWindow", "0"))

    def show_data(self):
        # ser = serial.Serial('COM5', 4800, timeout=1)
        while True :               
            data_raw = str(ser.readline())
            data_li = list(data_raw.split(","))
            if (data_li[0]=='b\'$GPGGA'):
                utc = data_li[1]
                self.UTC_value.setText(utc)
                lat = data_li[2]+data_li[3]
                self.lat_value.setText(lat)  
                long = data_li[4]+data_li[5]
                self.Long_value.setText(long)
                break
           
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())