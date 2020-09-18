'''
Created on Sep 18, 2020

@author: chraut
'''
from PyQt5.Qt import QMainWindow, QTimer

import RPi.GPIO as GPIO

class MainWindow (QMainWindow):
    
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        
    def initUI(self,mainProg,ui):
        
        # save prog and ui
        self.mainProg = mainProg
        self.ui = ui
        
        # connect buttons
        self.ui.butMode1.clicked.connect(lambda: self.mode1Start())
        self.ui.butMode2.clicked.connect(lambda: self.mode2Start())
        self.ui.butStopp.clicked.connect(lambda: self.modeStop())
        
        # set timer
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.modeLED)
        
        # declare IO
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(7,GPIO.OUT)
        GPIO.setup(11,GPIO.OUT)
        
    # mode 1
    def mode1Start(self):
        self.mode = 1
        self.timer.start()

    # mode 2
    def mode2Start(self):
        self.mode = 2
        self.timer.start()
        
    # stop
    def modeStop(self):
        self.mode = 0 
        self.timer.stop()
    
    def modeLED(self):

        if self.mode == 1:
            GPIO.output(7,True)
            
        if self.mode == 2:
            GPIO.output(7,False)

        
        
        
        