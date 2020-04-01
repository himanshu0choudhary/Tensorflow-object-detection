import sys,os
from PyQt5 import QtCore, QtGui, QtWidgets
from os.path import expanduser

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5 import uic, QtGui, QtCore


class Ui_MainWindow(object):
    def __init__(self,dir="../nature"):
        self.dir=dir
        self.pic=1
        self.lis=self.GetImg()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.OpneFolder = QtWidgets.QPushButton(self.centralwidget)
        self.OpneFolder.setGeometry(QtCore.QRect(10, 20, 100, 35))
        self.OpneFolder.setObjectName("OpneFolder")
        self.OpneFolder.clicked.connect(self.OpenF)

        self.NextImage = QtWidgets.QPushButton(self.centralwidget)
        self.NextImage.setGeometry(QtCore.QRect(10, 100, 100, 35))
        self.NextImage.setObjectName("NextImage")
        self.NextImage.clicked.connect(self.NextI)
        
        self.PreImage = QtWidgets.QPushButton(self.centralwidget)
        self.PreImage.setGeometry(QtCore.QRect(10, 180, 100, 50))
        self.PreImage.setObjectName("PreImage")
        self.PreImage.clicked.connect(self.PreI)
        
        self.SaveAnnonation = QtWidgets.QPushButton(self.centralwidget)
        self.SaveAnnonation.setGeometry(QtCore.QRect(10, 260, 100, 50))
        self.SaveAnnonation.setObjectName("SaveAnnonation")
        self.SaveAnnonation.clicked.connect(self.SaveAnn)
        
        self.SelectModel = QtWidgets.QPushButton(self.centralwidget)
        self.SelectModel.setGeometry(QtCore.QRect(600, 20, 100, 50))
        self.SelectModel.setObjectName("SelectModel")

        self.FRCNN = QtWidgets.QRadioButton(self.centralwidget)
        self.FRCNN.setGeometry(QtCore.QRect(600, 75, 80, 20))
        self.FRCNN.setObjectName("FRCNN")

        self.Mobilenet = QtWidgets.QRadioButton(self.centralwidget)
        self.Mobilenet.setGeometry(QtCore.QRect(600, 100, 100, 20))
        self.Mobilenet.setObjectName("Mobilenet")

        self.SSD = QtWidgets.QRadioButton(self.centralwidget)
        self.SSD.setGeometry(QtCore.QRect(600, 125, 62, 20))
        self.SSD.setObjectName("SSD")

        self.DetThresold = QtWidgets.QPushButton(self.centralwidget)
        self.DetThresold.setGeometry(QtCore.QRect(600, 160, 75, 40))
        self.DetThresold.setCheckable(False)
        self.DetThresold.setObjectName("DetThresold")

        self.Detect = QtWidgets.QPushButton(self.centralwidget)
        self.Detect.setGeometry(QtCore.QRect(600, 360, 75, 50))
        self.Detect.setObjectName("Detect")
        self.Detect.clicked.connect(self.DetectI)

        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(680, 160, 65, 40))
        self.doubleSpinBox.setMinimum(0)
        self.doubleSpinBox.setMaximum(1)
        self.doubleSpinBox.setSingleStep(0.05)
        self.doubleSpinBox.setObjectName("Input")
        
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(600, 210, 100, 140))
        self.groupBox.setObjectName("groupBox")
        
        self.Person = QtWidgets.QCheckBox(self.groupBox)
        self.Person.setGeometry(QtCore.QRect(10, 25, 80, 16))
        self.Person.setObjectName("Person")
        
        self.Cat = QtWidgets.QCheckBox(self.groupBox)
        self.Cat.setGeometry(QtCore.QRect(10, 45, 80, 16))
        self.Cat.setObjectName("Cat")
        
        self.Dog = QtWidgets.QCheckBox(self.groupBox)
        self.Dog.setGeometry(QtCore.QRect(10, 65, 80, 16))
        self.Dog.setObjectName("Dog")
        
        self.Bottle = QtWidgets.QCheckBox(self.groupBox)
        self.Bottle.setGeometry(QtCore.QRect(10, 85, 80, 16))
        self.Bottle.setObjectName("Bottle")
        
        self.Chair = QtWidgets.QCheckBox(self.groupBox)
        self.Chair.setGeometry(QtCore.QRect(10, 110, 80, 16))
        self.Chair.setObjectName("Chair")

        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(125, 20, 450, 400))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("../nature/"+self.lis[0]))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.OpneFolder.setText(_translate("MainWindow", "Open Folder"))
        self.NextImage.setText(_translate("MainWindow", "Next Image"))
        self.PreImage.setText(_translate("MainWindow", "Previous\n"
"Image"))
        self.SaveAnnonation.setText(_translate("MainWindow", "Save\n"
"Annotation"))
        self.SelectModel.setText(_translate("MainWindow", "Select\n"
"Model"))
        self.FRCNN.setText(_translate("MainWindow", "FRCNN"))
        self.Mobilenet.setText(_translate("MainWindow", "Mobilenet"))
        self.SSD.setText(_translate("MainWindow", "SSD"))
        self.DetThresold.setText(_translate("MainWindow", "Detection\n"
"Thresold"))
        self.Detect.setText(_translate("MainWindow", "Detect"))
        self.groupBox.setTitle(_translate("MainWindow", "Label Filter"))
        self.Person.setText(_translate("MainWindow", "Person"))
        self.Cat.setText(_translate("MainWindow", "Cat"))
        self.Dog.setText(_translate("MainWindow", "Dog"))
        self.Bottle.setText(_translate("MainWindow", "Bottel"))
        self.Chair.setText(_translate("MainWindow", "Chair"))


    def OpenF(self):
        print("Opening New Directory...")
        self.dir = QFileDialog.getExistingDirectory(None, 'Select a folder:', expanduser("~"))
        self.lis=self.GetImg()
        self.pic=1
        assert(len(self.lis)>0)
        #print(self.lis[self.pic])
        self.photo.setPixmap(QtGui.QPixmap(self.dir+'/'+self.lis[0]))
        #print(self.dir)


    def GetImg(self):
        assert(self.dir!=None)
        lis=os.listdir(self.dir)
        #print(lis)
        return lis

    def NextI(self):
        print("Next Image")
        assert(len(self.lis)>=0)
        self.photo.setPixmap(QtGui.QPixmap(self.dir+'/'+self.lis[self.pic]))
        print(self.dir+self.lis[self.pic])
        if self.pic<len(self.lis)-1:
            self.pic+=1
            

    def PreI(self):
        print("Prev Image")
        assert(len(self.lis)>=0)
        self.photo.setPixmap(QtGui.QPixmap(self.dir+'/'+self.lis[self.pic]))
        print(self.dir+self.lis[self.pic])
        if self.pic>=1:
            self.pic-=1

    def SaveAnn(self):
        print("Ann Saved")

    def DetectI(self):
            print("Detecting...")

    



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow("../nature")
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())