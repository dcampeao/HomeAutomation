# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(531, 459)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Prefix/Logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.LightOnPushButton = QtGui.QPushButton(self.tab)
        self.LightOnPushButton.setGeometry(QtCore.QRect(20, 70, 93, 28))
        self.LightOnPushButton.setObjectName(_fromUtf8("LightOnPushButton"))
        self.LightOffPushButton = QtGui.QPushButton(self.tab)
        self.LightOffPushButton.setGeometry(QtCore.QRect(20, 110, 93, 28))
        self.LightOffPushButton.setObjectName(_fromUtf8("LightOffPushButton"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(40, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(200, 30, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.TVOnPushButton = QtGui.QPushButton(self.tab)
        self.TVOnPushButton.setGeometry(QtCore.QRect(170, 70, 93, 28))
        self.TVOnPushButton.setObjectName(_fromUtf8("TVOnPushButton"))
        self.TVOffPushButton = QtGui.QPushButton(self.tab)
        self.TVOffPushButton.setGeometry(QtCore.QRect(170, 110, 93, 28))
        self.TVOffPushButton.setObjectName(_fromUtf8("TVOffPushButton"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(330, 20, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.EncoderOnPushButton = QtGui.QPushButton(self.tab)
        self.EncoderOnPushButton.setGeometry(QtCore.QRect(340, 70, 93, 28))
        self.EncoderOnPushButton.setObjectName(_fromUtf8("EncoderOnPushButton"))
        self.EncoderOffPushButton = QtGui.QPushButton(self.tab)
        self.EncoderOffPushButton.setGeometry(QtCore.QRect(340, 110, 93, 28))
        self.EncoderOffPushButton.setObjectName(_fromUtf8("EncoderOffPushButton"))
        self.TVCupPushButton = QtGui.QPushButton(self.tab)
        self.TVCupPushButton.setGeometry(QtCore.QRect(170, 150, 93, 28))
        self.TVCupPushButton.setObjectName(_fromUtf8("TVCupPushButton"))
        self.TVCdnPushButton = QtGui.QPushButton(self.tab)
        self.TVCdnPushButton.setGeometry(QtCore.QRect(170, 190, 93, 28))
        self.TVCdnPushButton.setObjectName(_fromUtf8("TVCdnPushButton"))
        self.EncoderCupPushButton = QtGui.QPushButton(self.tab)
        self.EncoderCupPushButton.setGeometry(QtCore.QRect(340, 150, 93, 28))
        self.EncoderCupPushButton.setObjectName(_fromUtf8("EncoderCupPushButton"))
        self.EncoderCdnPushButton = QtGui.QPushButton(self.tab)
        self.EncoderCdnPushButton.setGeometry(QtCore.QRect(340, 190, 93, 28))
        self.EncoderCdnPushButton.setObjectName(_fromUtf8("EncoderCdnPushButton"))
        self.TVVupPushButton = QtGui.QPushButton(self.tab)
        self.TVVupPushButton.setGeometry(QtCore.QRect(170, 230, 93, 28))
        self.TVVupPushButton.setObjectName(_fromUtf8("TVVupPushButton"))
        self.TVVdnPushButton = QtGui.QPushButton(self.tab)
        self.TVVdnPushButton.setGeometry(QtCore.QRect(170, 270, 93, 28))
        self.TVVdnPushButton.setObjectName(_fromUtf8("TVVdnPushButton"))
        self.EncoderVupPushButton = QtGui.QPushButton(self.tab)
        self.EncoderVupPushButton.setGeometry(QtCore.QRect(340, 230, 93, 28))
        self.EncoderVupPushButton.setObjectName(_fromUtf8("EncoderVupPushButton"))
        self.EncoderVdnPushButton = QtGui.QPushButton(self.tab)
        self.EncoderVdnPushButton.setGeometry(QtCore.QRect(340, 270, 93, 28))
        self.EncoderVdnPushButton.setObjectName(_fromUtf8("EncoderVdnPushButton"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 531, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuArquivo = QtGui.QMenu(self.menubar)
        self.menuArquivo.setObjectName(_fromUtf8("menuArquivo"))
        self.menuAjuda = QtGui.QMenu(self.menubar)
        self.menuAjuda.setObjectName(_fromUtf8("menuAjuda"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNovo = QtGui.QAction(MainWindow)
        self.actionNovo.setObjectName(_fromUtf8("actionNovo"))
        self.actionAbrir = QtGui.QAction(MainWindow)
        self.actionAbrir.setObjectName(_fromUtf8("actionAbrir"))
        self.actionSalvar = QtGui.QAction(MainWindow)
        self.actionSalvar.setObjectName(_fromUtf8("actionSalvar"))
        self.actionSobre = QtGui.QAction(MainWindow)
        self.actionSobre.setObjectName(_fromUtf8("actionSobre"))
        self.actionSair = QtGui.QAction(MainWindow)
        self.actionSair.setObjectName(_fromUtf8("actionSair"))
        self.menuArquivo.addAction(self.actionNovo)
        self.menuArquivo.addAction(self.actionAbrir)
        self.menuArquivo.addAction(self.actionSalvar)
        self.menuArquivo.addAction(self.actionSair)
        self.menuAjuda.addAction(self.actionSobre)
        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menubar.addAction(self.menuAjuda.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "HouseAutomate", None))
        self.LightOnPushButton.setText(_translate("MainWindow", "Turn On", None))
        self.LightOffPushButton.setText(_translate("MainWindow", "Turn Off", None))
        self.label.setText(_translate("MainWindow", "COFFEE", None))
        self.label_2.setText(_translate("MainWindow", "TV", None))
        self.TVOnPushButton.setText(_translate("MainWindow", "Turn On", None))
        self.TVOffPushButton.setText(_translate("MainWindow", "Turn Off", None))
        self.label_3.setText(_translate("MainWindow", "ENCODER", None))
        self.EncoderOnPushButton.setText(_translate("MainWindow", "Turn On", None))
        self.EncoderOffPushButton.setText(_translate("MainWindow", "Turn Off", None))
        self.TVCupPushButton.setText(_translate("MainWindow", "Channel +", None))
        self.TVCdnPushButton.setText(_translate("MainWindow", "Channel -", None))
        self.EncoderCupPushButton.setText(_translate("MainWindow", "Channel +", None))
        self.EncoderCdnPushButton.setText(_translate("MainWindow", "Channel -", None))
        self.TVVupPushButton.setText(_translate("MainWindow", "Volume +", None))
        self.TVVdnPushButton.setText(_translate("MainWindow", "Volume -", None))
        self.EncoderVupPushButton.setText(_translate("MainWindow", "Volume +", None))
        self.EncoderVdnPushButton.setText(_translate("MainWindow", "Volume -", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Living Room", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Bedroom", None))
        self.menuArquivo.setTitle(_translate("MainWindow", "Files", None))
        self.menuAjuda.setTitle(_translate("MainWindow", "Help", None))
        self.actionNovo.setText(_translate("MainWindow", "New", None))
        self.actionAbrir.setText(_translate("MainWindow", "Open", None))
        self.actionSalvar.setText(_translate("MainWindow", "Save", None))
        self.actionSobre.setText(_translate("MainWindow", "About", None))
        self.actionSair.setText(_translate("MainWindow", "Quit", None))

#import resourcetest_rc
