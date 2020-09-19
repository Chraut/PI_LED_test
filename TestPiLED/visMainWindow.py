'''
Created on Sep 18, 2020

@author: chraut
'''
from PyQt5.Qt import QMainWindow, QTimer
from PyQt5.QtCore import Qt

#import RPi.GPIO as GPIO

class MainWindow (QMainWindow):
    
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        
        # maximize
        self.showMaximized()
        
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
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.modeLED)
        
        # declare IO
        #GPIO.setmode(GPIO.BOARD)
        #GPIO.setup(7,GPIO.OUT)
        #GPIO.setup(11,GPIO.OUT)
        #GPIO.setup(15,GPIO.OUT)
 
    # mode 1
    def mode1Start(self):
        self.mode = 1
        self.step = 0
        self.modeLED()

    # mode 2
    def mode2Start(self):
        self.mode = 2
        self.step = 0
        self.modeLED()
        
    # stop
    def modeStop(self):
        self.mode = 0 
        self.step = 0
        self.timer.stop()
    
    def modeLED(self):
        
        ## mode 1
        if self.mode == 1:
            
            if (self.step == 0):
                print('step 0')
                #GPIO.output(7,True)
                #GPIO.output(11,False)
                #GPIO.output(15,False)
            if (self.step == 1):          
                print('step 1')
                #GPIO.output(7,False)
                #GPIO.output(11,True)
                #GPIO.output(15,False)
            if (self.step == 2):
                print('step 2')
                #GPIO.output(7,False)
                #GPIO.output(11,False)
                #GPIO.output(15,True)

            self.step += 1
            
            if (self.step >= 3):
                self.step = 0
        
        ## mode 2
        if self.mode == 2:
            
            if (self.step == 0):
                print('step 0')
                #GPIO.output(7,False)
                #GPIO.output(11,True)
                #GPIO.output(15,False)
            if (self.step == 1):          
                print('step 1')
                #GPIO.output(7,True)
                #GPIO.output(11,False)
                #GPIO.output(15,True)
            if (self.step == 2):
                print('step 2')
                #GPIO.output(7,False)
                #GPIO.output(11,False)
                #GPIO.output(15,False)

            self.step += 1
            
            if (self.step >= 3):
                self.step = 0
        
            
        self.timer.start()
            

        
        
        
        