##Copyright (C) 2018 Diego Esteves Campeao

##Contact information:  Diego Campeao - diegoecampeao@gmail.com

from PyQt4 import QtGui, QtCore # Import the PyQt4 module we'll need
import sys # We need sys so that we can pass argv to QApplication

import design # This file holds our MainWindow and all design related things
              # it also keeps events etc that we defined in Qt Designer

import RPi.GPIO as GPIO
import os

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.output(7,1)

bashCommand = 'sudo /etc/init.d/lirc restart'
os.system(bashCommand)

bashCommand = 'irsend LIST /home/pi/lircd.conf ""'
os.system(bashCommand)

class MainApp(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.LightOnPushButton.clicked.connect(self.TurnLightsOn)
        self.LightOffPushButton.clicked.connect(self.TurnLightsOff)

        self.TVOnPushButton.clicked.connect(self.TurnTVOn)
        self.TVOffPushButton.clicked.connect(self.TurnTVOff)

        self.TVCupPushButton.clicked.connect(self.TVChannelUp)
        self.TVCdnPushButton.clicked.connect(self.TVChannelDown)

        self.TVVupPushButton.clicked.connect(self.TVVolumeUp)
        self.TVVdnPushButton.clicked.connect(self.TVVolumeDown)

        self.EncoderOnPushButton.clicked.connect(self.TurnEncoderOn)
        self.EncoderOffPushButton.clicked.connect(self.TurnEncoderOff)

        self.EncoderCupPushButton.clicked.connect(self.EncoderChannelUp)
        self.EncoderCdnPushButton.clicked.connect(self.EncoderChannelDown)

        self.EncoderVupPushButton.clicked.connect(self.EncoderVolumeUp)
        self.EncoderVdnPushButton.clicked.connect(self.EncoderVolumeDown)
        
    def Sair(self):
        sys.stderr.write('\r')
        if QtGui.QMessageBox.question(None, '', "Are you sure you want to quit?",
                                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
                                QtGui.QMessageBox.No) == QtGui.QMessageBox.Yes:
            QtGui.QApplication.quit()

    def TurnLightsOn(self):
        GPIO.output(7,0)

    def TurnLightsOff(self):
        GPIO.output(7,1)

    def TurnTVOn(self):
        pass

    def TurnTVOff(self):
        pass

    def TVChannelUp(self):
        pass

    def TVChannelDown(self):
        pass

    def TVVolumeUp(self):
        pass

    def TVVolumeDown(self):
        pass

    def TurnEncoderOn(self):
        bashCommand = 'irsend SEND_ONCE Encoder KEY_POWER'
        os.system(bashCommand)

    def TurnEncoderOff(self):
        bashCommand = 'irsend SEND_ONCE Encoder KEY_POWER'
        os.system(bashCommand)

    def EncoderChannelUp(self):
        bashCommand = 'irsend SEND_ONCE Encoder KEY_CHANNELUP'
        os.system(bashCommand)
        print('Channel Up')
        
    def EncoderChannelDown(self):
        bashCommand = 'irsend SEND_ONCE Encoder KEY_CHANNELDOWN'
        os.system(bashCommand)

    def EncoderVolumeUp(self):
        bashCommand = 'irsend SEND_ONCE Encoder KEY_VOLUMEUP'
        os.system(bashCommand)

    def EncoderVolumeDown(self):
        bashCommand = 'irsend SEND_ONCE Encoder KEY_VOLUMEDOWN'
        os.system(bashCommand)

def main():
    app = QtGui.QApplication(sys.argv)
    form = MainApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
