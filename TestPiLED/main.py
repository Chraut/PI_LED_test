'''
Created on Sep 17, 2020

@author: chraut
'''

import sys

from qtMainWindow import Ui_MainWindow
from visMainWindow import MainWindow
from PyQt5 import QtWidgets

class MainProg(object):
    
    def __init__(self):    

        # super
        self.app = QtWidgets.QApplication(sys.argv)
        
        # main window
        self.mainWindow = MainWindow()
        self.uiMainWindow = Ui_MainWindow()
        self.uiMainWindow.setupUi(self.mainWindow)
        self.mainWindow.initUI(self, self.uiMainWindow)
        
        self.mainWindow.show()
        
        sys.exit(self.app.exec_())

mainP = MainProg()