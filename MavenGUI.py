
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MavenUI(object):
    def setupUi(self, MavenUI):
        MavenUI.setObjectName("MavenUI")
        MavenUI.resize(875, 503)
        self.centralwidget = QtWidgets.QWidget(MavenUI)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-4, -8, 881, 611))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:\\Dracarys\\Python\\Maven\\GUIMAVEN\\Black_Template.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(490, 10, 421, 281))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("D:\\Dracarys\\Python\\Maven\\GUIMAVEN\\Iron_Template_1.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(-50, 160, 321, 211))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("D:\\Dracarys\\Python\\Maven\\GUIMAVEN\\__1.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, -40, 331, 201))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("D:\\Dracarys\\Python\\Maven\\GUIMAVEN\\initial.gif"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 380, 211, 111))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("D:\\Dracarys\\Python\\Maven\\GUIMAVEN\\Health_Template.gif"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(490, 300, 351, 191))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("D:\\Dracarys\\Python\\Maven\\GUIMAVEN\\B.G_Template_1.gif"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 460, 91, 31))
        self.pushButton.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 460, 91, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        MavenUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(MavenUI)
        QtCore.QMetaObject.connectSlotsByName(MavenUI)

    def retranslateUi(self, MavenUI):
        _translate = QtCore.QCoreApplication.translate
        MavenUI.setWindowTitle(_translate("MavenUI", "MainWindow"))
        self.pushButton.setText(_translate("MavenUI", "START"))
        self.pushButton_2.setText(_translate("MavenUI", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MavenUI = QtWidgets.QMainWindow()
    ui = Ui_MavenUI()
    ui.setupUi(MavenUI)
    MavenUI.show()
    sys.exit(app.exec_())
