#User Interface

from PyQt4 import QtCore, QtGui
from time import strftime
import sys
import os
import errno
import math
import shutil
import csv
import numpy as np


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

def dist (x1,y1,x2,y2):
    return math.sqrt(math.pow(x1 - x2,2) + math.pow(y1 - y2,2))

class Ui_window(object):
    def setupUi(self, window):
        window.setObjectName(_fromUtf8("window"))
        window.resize(1138, 706)
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        window.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("uiicon.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        window.setWindowIcon(icon)
        window.setWindowOpacity(100.0)
        window.setAutoFillBackground(False)
        self.centralwidget = QtGui.QWidget(window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(504, 58, 190, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(503, 99, 190, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(710, 10, 151, 31))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.ipv = QtGui.QTextEdit(self.centralwidget)
        self.ipv.setGeometry(QtCore.QRect(710, 50, 151, 31))
        self.ipv.setObjectName(_fromUtf8("ipv"))
        self.ipv.setDisabled(True)
        self.prev = QtGui.QTextEdit(self.centralwidget)
        self.prev.setGeometry(QtCore.QRect(710, 90, 151, 31))
        self.prev.setFrameShape(QtGui.QFrame.StyledPanel)
        self.prev.setFrameShadow(QtGui.QFrame.Raised)
        self.prev.setMidLineWidth(0)
        self.prev.setObjectName(_fromUtf8("prev"))
        self.prev.setDisabled(True)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(503, 139, 190, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.prescan = QtGui.QTextEdit(self.centralwidget)
        self.prescan.setGeometry(QtCore.QRect(710, 130, 151, 31))
        self.prescan.setFrameShape(QtGui.QFrame.StyledPanel)
        self.prescan.setFrameShadow(QtGui.QFrame.Raised)
        self.prescan.setMidLineWidth(0)
        self.prescan.setDisabled(True)
        self.prescan.setObjectName(_fromUtf8("prescan"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(504, 176, 190, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.outputfolder = QtGui.QTextEdit(self.centralwidget)
        self.outputfolder.setGeometry(QtCore.QRect(710, 170, 151, 31))
        self.outputfolder.setFrameShape(QtGui.QFrame.StyledPanel)
        self.outputfolder.setFrameShadow(QtGui.QFrame.Raised)
        self.outputfolder.setMidLineWidth(0)
        self.outputfolder.setObjectName(_fromUtf8("outputfolder"))
        self.outputfolder.setDisabled(True)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 230, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(910, 110, 201, 21))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(670, 290, 141, 31))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(671, 331, 131, 31))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(672, 372, 131, 31))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.bmcur = QtGui.QTextEdit(self.centralwidget)
        self.bmcur.setGeometry(QtCore.QRect(810, 290, 81, 31))
        self.bmcur.setObjectName(_fromUtf8("bmcur"))
        self.bmcur.setDisabled(True)
        self.lncur = QtGui.QTextEdit(self.centralwidget)
        self.lncur.setGeometry(QtCore.QRect(810, 330, 81, 31))
        self.lncur.setObjectName(_fromUtf8("lncur"))
        self.lncur.setDisabled(True)
        self.Hv = QtGui.QTextEdit(self.centralwidget)
        self.Hv.setGeometry(QtCore.QRect(810, 370, 81, 31))
        self.Hv.setObjectName(_fromUtf8("Hv"))
        self.Hv.setDisabled(True)
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(673, 409, 131, 31))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(920, 332, 91, 31))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(920, 290, 91, 31))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(920, 370, 91, 31))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(920, 408, 91, 31))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.par1 = QtGui.QTextEdit(self.centralwidget)
        self.par1.setGeometry(QtCore.QRect(810, 410, 81, 31))
        self.par1.setObjectName(_fromUtf8("par1"))
        self.par1.setDisabled(True)
        self.par2 = QtGui.QTextEdit(self.centralwidget)
        self.par2.setGeometry(QtCore.QRect(1020, 290, 81, 31))
        self.par2.setObjectName(_fromUtf8("par2"))
        self.par2.setDisabled(True)
        self.par3 = QtGui.QTextEdit(self.centralwidget)
        self.par3.setGeometry(QtCore.QRect(1020, 330, 81, 31))
        self.par3.setObjectName(_fromUtf8("par3"))
        self.par3.setDisabled(True)
        self.par4 = QtGui.QTextEdit(self.centralwidget)
        self.par4.setGeometry(QtCore.QRect(1020, 370, 81, 31))
        self.par4.setObjectName(_fromUtf8("par4"))
        self.par4.setDisabled(True)
        self.par5 = QtGui.QTextEdit(self.centralwidget)
        self.par5.setGeometry(QtCore.QRect(1020, 410, 81, 31))
        self.par5.setObjectName(_fromUtf8("par5"))
        self.par5.setDisabled(True)
        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(10, 530, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_14.setFont(font)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.pp1 = QtGui.QRadioButton(self.centralwidget)
        self.pp1.setGeometry(QtCore.QRect(17, 290, 151, 22))
        self.pp1.setObjectName(_fromUtf8("pp1"))
        self.pp1.setDisabled(True)
        self.pp1.clicked.connect(self.preheatpattern1)
        self.pp2 = QtGui.QRadioButton(self.centralwidget)
        self.pp2.setGeometry(QtCore.QRect(17, 330, 151, 22))
        self.pp2.setObjectName(_fromUtf8("pp2"))
        self.pp2.setDisabled(True)
        self.pp2.clicked.connect(self.preheatpattern2)
        self.pp3 = QtGui.QRadioButton(self.centralwidget)
        self.pp3.setGeometry(QtCore.QRect(17, 370, 151, 22))
        self.pp3.setObjectName(_fromUtf8("pp3"))
        self.pp3.setDisabled(True)
        self.pp3.clicked.connect(self.preheatpattern3)
        self.pp4 = QtGui.QRadioButton(self.centralwidget)
        self.pp4.setGeometry(QtCore.QRect(17, 410, 151, 22))
        self.pp4.setObjectName(_fromUtf8("pp4"))
        self.pp4.setDisabled(True)
        self.pp4.clicked.connect(self.preheatpattern4)
        self.pp5 = QtGui.QRadioButton(self.centralwidget)
        self.pp5.setGeometry(QtCore.QRect(177, 290, 151, 22))
        self.pp5.setObjectName(_fromUtf8("pp5"))
        self.pp5.setDisabled(True)
        self.pp5.clicked.connect(self.preheatpattern5)
        self.pp6 = QtGui.QRadioButton(self.centralwidget)
        self.pp6.setGeometry(QtCore.QRect(177, 330, 151, 22))
        self.pp6.setObjectName(_fromUtf8("pp6"))
        self.pp6.setDisabled(True)
        self.pp6.clicked.connect(self.preheatpattern6)
        self.pp7 = QtGui.QRadioButton(self.centralwidget)
        self.pp7.setGeometry(QtCore.QRect(177, 370, 151, 22))
        self.pp7.setObjectName(_fromUtf8("pp7"))
        self.pp7.setDisabled(True)
        self.pp7.clicked.connect(self.preheatpattern7)
        self.pp8 = QtGui.QRadioButton(self.centralwidget)
        self.pp8.setGeometry(QtCore.QRect(177, 410, 151, 22))
        self.pp8.setObjectName(_fromUtf8("pp8"))
        self.pp8.setDisabled(True)
        self.pp8.clicked.connect(self.preheatpattern8)
        self.pp9 = QtGui.QRadioButton(self.centralwidget)
        self.pp9.setGeometry(QtCore.QRect(348, 290, 151, 22))
        self.pp9.setObjectName(_fromUtf8("pp9"))
        self.pp9.setDisabled(True)
        self.pp9.clicked.connect(self.preheatpattern9)
        self.pp10 = QtGui.QRadioButton(self.centralwidget)
        self.pp10.setGeometry(QtCore.QRect(348, 329, 161, 22))
        self.pp10.setObjectName(_fromUtf8("pp10"))
        self.pp10.setDisabled(True)
        self.pp10.clicked.connect(self.preheatpattern10)
        self.pp11 = QtGui.QRadioButton(self.centralwidget)
        self.pp11.setGeometry(QtCore.QRect(349, 370, 161, 22))
        self.pp11.setObjectName(_fromUtf8("pp11"))
        self.pp11.setDisabled(True)
        self.pp11.clicked.connect(self.preheatpattern11)
        self.skirt = QtGui.QRadioButton(self.centralwidget)
        self.skirt.setGeometry(QtCore.QRect(349, 410, 161, 22))
        self.skirt.setObjectName(_fromUtf8("skirt"))
        self.skirt.setDisabled(True)
        self.skirt.clicked.connect(self.skirtf)
        self.infill = QtGui.QRadioButton(self.centralwidget)
        self.infill.setGeometry(QtCore.QRect(507, 290, 151, 22))
        self.infill.setObjectName(_fromUtf8("infill"))
        self.infill.setDisabled(True)
        self.infill.clicked.connect(self.infillf)
        self.skin = QtGui.QRadioButton(self.centralwidget)
        self.skin.setGeometry(QtCore.QRect(508, 330, 151, 22))
        self.skin.setObjectName(_fromUtf8("skin"))
        self.skin.setDisabled(True)
        self.skin.clicked.connect(self.skinf)
        self.icont = QtGui.QRadioButton(self.centralwidget)
        self.icont.setGeometry(QtCore.QRect(509, 370, 151, 22))
        self.icont.setObjectName(_fromUtf8("icont"))
        self.icont.setDisabled(True)
        self.icont.clicked.connect(self.innercontourf)
        self.ocont = QtGui.QRadioButton(self.centralwidget)
        self.ocont.setGeometry(QtCore.QRect(510, 410, 151, 22))
        self.ocont.setObjectName(_fromUtf8("ocont"))
        self.ocont.setDisabled(True)
        self.ocont.clicked.connect(self.outercontourf)
        self.label_16 = QtGui.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(230, 80, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_15 = QtGui.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(20, 20, 201, 191))
        self.label_15.setText(_fromUtf8(""))
        self.label_15.setPixmap(QtGui.QPixmap(_fromUtf8("iisclogo2.png")))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_17 = QtGui.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(504, 214, 190, 20))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.nprep = QtGui.QTextEdit(self.centralwidget)
        self.nprep.setGeometry(QtCore.QRect(710, 210, 151, 31))
        self.nprep.setFrameShape(QtGui.QFrame.StyledPanel)
        self.nprep.setFrameShadow(QtGui.QFrame.Raised)
        self.nprep.setMidLineWidth(0)
        self.nprep.setObjectName(_fromUtf8("nprep"))
        self.nprep.setDisabled(True)
        self.fileselectbutton = QtGui.QPushButton(self.centralwidget)
        self.fileselectbutton.setGeometry(QtCore.QRect(500, 11, 200, 27))
        self.fileselectbutton.setObjectName(_fromUtf8("fileselectbutton"))
        self.fileselectbutton.clicked.connect(self.choosefile)
        self.svparambutton = QtGui.QPushButton(self.centralwidget)
        self.svparambutton.setGeometry(QtCore.QRect(20, 460, 231, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.svparambutton.setFont(font)
        self.svparambutton.setObjectName(_fromUtf8("svparambutton"))
        self.svparambutton.setDisabled(True)
        self.svparambutton.clicked.connect(self.saveparameters)
        self.convertbutton = QtGui.QPushButton(self.centralwidget)
        self.convertbutton.setGeometry(QtCore.QRect(930, 30, 161, 51))
        self.convertbutton.setDisabled(True)
        self.convertbutton.clicked.connect(self.convertfile)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.convertbutton.setFont(font)
        self.convertbutton.setObjectName(_fromUtf8("convertbutton"))
        self.genparambutton = QtGui.QPushButton(self.centralwidget)
        self.genparambutton.setGeometry(QtCore.QRect(280, 460, 271, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.genparambutton.setFont(font)
        self.genparambutton.setObjectName(_fromUtf8("genparambutton"))
        self.genparambutton.setDisabled(True)
        self.genparambutton.clicked.connect(self.generateParameterFile)
        self.simbutton = QtGui.QPushButton(self.centralwidget)
        self.simbutton.setGeometry(QtCore.QRect(20, 590, 231, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.simbutton.setFont(font)
        self.simbutton.setObjectName(_fromUtf8("simbutton"))
        self.simbutton.setDisabled(True)
        self.simbutton.clicked.connect(self.simulate)
        window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1138, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        window.setStatusBar(self.statusbar)
        self.actionReadme = QtGui.QAction(window)
        self.actionReadme.setObjectName(_fromUtf8("actionReadme"))

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window):
        window.setWindowTitle(_translate("window", "File Converter and Simulator", None))
        self.label.setText(_translate("window", "Set Input Velocity (mm/s)", None))
        self.label_2.setText(_translate("window", "Set Preheat Velocity(mm/s)", None))
        self.label_3.setText(_translate("window", "Set Preheat Scan Width(mm)", None))
        self.label_4.setText(_translate("window", "Set Output Folder", None))
        self.label_5.setText(_translate("window", "GLOBAL PARAMETER SETTINGS", None))
        self.label_6.setText(_translate("window", "Beam Current (mA)", None))
        self.label_7.setText(_translate("window", "Lens Current (mA)", None))
        self.label_8.setText(_translate("window", "High Voltage (kV)", None))
        self.label_9.setText(_translate("window", "Parameter 1", None))
        self.label_10.setText(_translate("window", "Parameter 3", None))
        self.label_11.setText(_translate("window", "Parameter 2", None))
        self.label_12.setText(_translate("window", "Parameter 4", None))
        self.label_13.setText(_translate("window", "Parameter 5", None))
        self.label_14.setText(_translate("window", "SIMULATION SETTINGS", None))
        self.pp1.setText(_translate("window", "Preheat Pattern 1", None))
        self.pp2.setText(_translate("window", "Preheat Pattern 2", None))
        self.pp3.setText(_translate("window", "Preheat Pattern 3", None))
        self.pp4.setText(_translate("window", "Preheat Pattern 4", None))
        self.pp5.setText(_translate("window", "Preheat Pattern 5", None))
        self.pp6.setText(_translate("window", "Preheat Pattern 6", None))
        self.pp7.setText(_translate("window", "Preheat Pattern 7", None))
        self.pp8.setText(_translate("window", "Preheat Pattern 8", None))
        self.pp9.setText(_translate("window", "Preheat Pattern 9", None))
        self.pp10.setText(_translate("window", "Preheat Pattern 10", None))
        self.pp11.setText(_translate("window", "Preheat Pattern 11", None))
        self.skirt.setText(_translate("window", "Skirt", None))
        self.infill.setText(_translate("window", "Infill", None))
        self.skin.setText(_translate("window", "Skin", None))
        self.icont.setText(_translate("window", "Inner Contour", None))
        self.ocont.setText(_translate("window", "Outer Contour", None))
        self.label_16.setText(_translate("window", "DESE, IISc", None))
        self.label_17.setText(_translate("window", "No. of Preheat Patterns", None))
        self.fileselectbutton.setText(_translate("window", "Select File for Conversion...", None))
        self.svparambutton.setText(_translate("window", "SAVE PARAMETERS", None))
        self.convertbutton.setText(_translate("window", "CONVERT", None))
        self.genparambutton.setText(_translate("window", "GENERATE PARAMETER FILE", None))
        self.simbutton.setText(_translate("window", "SIMULATE", None))
        self.actionReadme.setText(_translate("window", "Readme", None))

    def enable_radio_buttons(self):
        self.pp1.setDisabled(False)
        self.pp2.setDisabled(False)
        self.pp3.setDisabled(False)
        self.pp4.setDisabled(False)
        self.pp5.setDisabled(False)
        self.pp6.setDisabled(False)
        self.pp7.setDisabled(False)
        self.pp8.setDisabled(False)
        self.pp9.setDisabled(False)
        self.pp10.setDisabled(False)
        self.pp11.setDisabled(False)
        self.skirt.setDisabled(False)
        self.infill.setDisabled(False)
        self.skin.setDisabled(False)
        self.icont.setDisabled(False)
        self.ocont.setDisabled(False)

    def reset(self):
        self.bmcur.clear()
        self.lncur.clear()
        self.Hv.clear()
        self.par1.clear()
        self.par2.clear()
        self.par3.clear()
        self.par4.clear()
        self.par5.clear()
        self.bmcur.setDisabled(False)
        self.lncur.setDisabled(False)
        self.Hv.setDisabled(False)
        self.par1.setDisabled(False)
        self.par2.setDisabled(False)
        self.par3.setDisabled(False)
        self.par4.setDisabled(False)
        self.par5.setDisabled(False)
        self.svparambutton.setDisabled(False)

    def display(self,listname):
        self.bmcur.clear()
        self.lncur.clear()
        self.Hv.clear()
        self.par1.clear()
        self.par2.clear()
        self.par3.clear()
        self.par4.clear()
        self.par5.clear()
        self.bmcur.setPlainText(str(listname[0]))
        self.lncur.setPlainText(str(listname[1]))
        self.Hv.setPlainText(str(listname[2]))
        self.par1.setPlainText(str(listname[3]))
        self.par2.setPlainText(str(listname[4]))
        self.par3.setPlainText(str(listname[5]))
        self.par4.setPlainText(str(listname[6]))
        self.par5.setPlainText(str(listname[7]))

    def choosefile(self):
        filepath = QtGui.QFileDialog.getOpenFileName(None,'Open File',os.getcwd(),filter="G-code Files(*.gcode)")
        self.filename = os.path.basename(filepath)
        self.textEdit.setPlainText(self.filename)
        self.textEdit.setDisabled(True)
        self.ipv.setDisabled(False)
        self.prev.setDisabled(False)
        self.prescan.setDisabled(False)
        self.outputfolder.setDisabled(False)
        self.nprep.setDisabled(False)
        self.convertbutton.setDisabled(False)
        self.pp1list,self.pp2list,self.pp3list,self.pp4list,self.pp5list,self.pp6list,self.pp7list,self.pp8list,self.pp9list,self.pp10list,self.pp11list,self.skirtlist = ([],)*12
        self.infilllist,self.skinlist,self.iclist,self.oclist = ([],)*4
        ui.enable_radio_buttons()


    def convertfile(self):
        if(str(self.ipv.toPlainText()) == '' or str(self.prev.toPlainText()) == '' or str(self.prescan.toPlainText()) == '' or str(self.outputfolder.toPlainText()) == '' or str(self.nprep.toPlainText()) == ''):
            QtGui.QMessageBox.information(None,"Error Message","Please enter the parameters in the respective fields")
            self.fields_flag = 0
        else:
            self.fields_flag = 1

        self.list_of_pattern_array = []
        self.velocity = float(self.ipv.toPlainText())
        self.preheat_velocity = float(self.prev.toPlainText())
        self.preheat_scan_width = float(self.prescan.toPlainText())
        self.parent_folder = self.outputfolder.toPlainText()
        self.num_preheat_patterns = int(float(self.nprep.toPlainText()))
        scan_width = int(self.preheat_scan_width * 7700 / 125)
        scan_time = int(15400 * self.preheat_velocity)
        pattern_array = np.zeros(16)
        pattern_array_count = 0
        flag = 0

        file1=open(self.filename,"r")
        lines = file1.readlines()

        for i in range(self.num_preheat_patterns):
            file2 = open('slice0' + str(i) + '.txt',"w")
            valx = int(scan_width / 2 - 7700)
            file2.write("#Preheat pattern" + " " + str(i+1) + " velocity = " + str(self.preheat_velocity) + '\n')

            while (valx < 7700):
                file2.write("0," + str(valx) + "," + "-7700\n")
                file2.write(str(scan_time) + "," + str(valx) + "," + "7700\n")
                valx += scan_width

        for line in lines:
            if(line[0] == ';'):
                if(";LAYER_COUNT" in line):
                    self.totlayercount = line[len("LAYER_COUNT")+2:].strip()
                elif(";LAYER" in line):
                    if flag:
                        self.list_of_pattern_array.append(pattern_array)
                    pattern_array = np.zeros(16)
                    pattern_array_count = 0
                    self.layernum = line[len("LAYER")+2:].strip()
                    folder = "/layer" + line[7:-1]
                    for i in range(self.num_preheat_patterns):
                        pattern_array[pattern_array_count] = i
                        pattern_array_count += 1
                        file = "/slice0" + str(i) + ".txt"
                        path = os.path.join(os.getcwd(), self.parent_folder + folder + file)
                        if not os.path.exists(os.path.dirname(path)):
                            try:
                                os.makedirs(os.path.dirname(path))
                            except OSError as exc:
                                if exc.errno != errno.EEXIST:
                                    raise
                        shutil.copy("slice0" + str(i) + ".txt",path)
                    count = self.num_preheat_patterns
                    flag = 0

                elif(";TYPE" in line):
                    self.type = line[len("TYPE") + 2:].strip()
                    if (self.type == "WALL-OUTER"):
                        pattern_array[pattern_array_count] = 15
                        pattern_array_count += 1
                    elif (self.type == "WALL-INNER"):
                        pattern_array[pattern_array_count] = 14
                        pattern_array_count += 1
                    elif (self.type == "FILL"):
                        pattern_array[pattern_array_count] = 12
                        pattern_array_count += 1
                    elif (self.type == "SKIN"):
                        pattern_array[pattern_array_count] = 13
                        pattern_array_count += 1
                    elif (self.type == "SKIRT"):
                        pattern_array[pattern_array_count] = 11
                        pattern_array_count += 1

                    if count > 9:
                        file = "/slice" + str(count) + ".txt"
                    else:
                        file = "/slice0" + str(count) + ".txt"
                    count += 1
                    flag = 1
                    file2.close()
                    path = os.path.join(os.getcwd(),self.parent_folder + folder + file)
                    if not os.path.exists(os.path.dirname(path)):
                        try:
                            os.makedirs(os.path.dirname(path))
                        except OSError as exc:
                            if exc.errno != errno.EEXIST:
                                raise
                    file2 = open(path,"w")
                    file2.write("#layer number = " + self.layernum + " type = " + self.type + " velocity = " + str(self.velocity) + '\n')
                    file2.write("0," + str(x_prev) + "," + str(y_prev) + '\n')

            elif('G0' in line):
                if('X' in line):
                    start = line.find('X')
                    end = line.find(' ',start)
                    valx = float(line[start+1:end])

                    start = line.find('Y')
                    end = line.find(' ',start)
                    valy = float(line[start+1:end])
                    valx = int((valx-125)*7700/125)
                    valy = int((valy-125)*7700/125)
                    if flag:
                        file2.write("0," + str(valx) + "," + str(valy) + '\n')
                    x_prev = valx
                    y_prev = valy

            elif('G1' in line):
                if('X' in line):
                    start = line.find('X')
                    end = line.find(' ',start)
                    valx = float(line[start+1:end])

                    start = line.find('Y')
                    end = line.find(' ',start)
                    valy = float(line[start+1:end])

                    valx = int((valx-125)*7700/125)
                    valy = int((valy-125)*7700/125)
                    d = int(self.velocity * dist(x_prev,y_prev,valx,valy))
                    file2.write(str(d) + "," + str(valx) + "," + str(valy) + '\n')
                    x_prev = valx
                    y_prev = valy

        file1.close()
        file2.close()
        self.progressBar.setProperty("value",100)
        self.genparambutton.setDisabled(False)
        self.simbutton.setDisabled(False)

        file_nm2 = "/parameters.csv"

        if(str(self.outputfolder.toPlainText()) == ''):
            QtGui.QMessageBox.warning(None,"Warning","Please enter the Output/Destination in the respective field")
        else:
            path = os.path.join(os.getcwd(),self.parent_folder + file_nm2)
            if not os.path.exists(os.path.dirname(path)):
                try:
                    os.makedirs(os.path.dirname(path))
                except OSError as exc:
                    if exc.errno != errno.EEXIST:
                        raise

        file4 = open(path,"a")
        with file4 as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(self.list_of_pattern_array)

        file4.close()

    def saveparameters(self):
        global_param_true = (str(self.bmcur.toPlainText()) == '' or str(self.lncur.toPlainText()) == '' or str(self.Hv.toPlainText()) == '' or str(self.par1.toPlainText()) == '' or
        str(self.par2.toPlainText()) == '' or str(self.par3.toPlainText()) == '' or str(self.par4.toPlainText()) == '' or str(self.par5.toPlainText()) == '')

        if(global_param_true):
            QtGui.QMessageBox.warning(None,"Warning","Please enter the values for all the parameters")
        else:
            self.fields = 1

        self.beam_current = float(self.bmcur.toPlainText())
        self.lens_current = float(self.lncur.toPlainText())
        self.high_voltage = float(self.Hv.toPlainText())
        self.param1 = float(self.par1.toPlainText())
        self.param2 = float(self.par2.toPlainText())
        self.param3 = float(self.par3.toPlainText())
        self.param4 = float(self.par4.toPlainText())
        self.param5 = float(self.par5.toPlainText())

        value_list = [self.beam_current,self.lens_current,self.high_voltage,self.param1,self.param2,self.param3,self.param4,self.param5]

        if(self.select_flag == 1):
            self.pp1list = value_list
        elif(self.select_flag == 2):
            self.pp2list = value_list
        elif(self.select_flag == 3):
            self.pp3list = value_list
        elif(self.select_flag == 4):
            self.pp4list = value_list
        elif(self.select_flag == 5):
            self.pp5list = value_list
        elif(self.select_flag == 6):
            self.pp6list = value_list
        elif(self.select_flag == 7):
            self.pp7list = value_list
        elif(self.select_flag == 8):
            self.pp8list = value_list
        elif(self.select_flag == 9):
            self.pp9list = value_list
        elif(self.select_flag == 10):
            self.pp10list = value_list
        elif(self.select_flag == 11):
            self.pp11list = value_list
        elif(self.select_flag == 12):
            self.skirtlist = value_list
        elif(self.select_flag == 13):
            self.infilllist = value_list
        elif(self.select_flag == 14):
            self.skinlist = value_list
        elif(self.select_flag == 15):
            self.iclist = value_list
        elif(self.select_flag == 16):
            self.oclist = value_list
        else:
            self.normallist = value_list

        if(self.fields == 1):
            ui.reset()
            self.svparambutton.setDisabled(True)


    def preheatpattern1(self):
        ui.reset()
        self.select_flag = 1
        if(self.pp1list):
            ui.display(self.pp1list)
        else:
            ui.reset()

    def preheatpattern2(self):
        ui.reset()
        self.select_flag = 2
        if(self.pp2list):
            ui.display(self.pp2list)
        else:
            ui.reset()

    def preheatpattern3(self):
        ui.reset()
        self.select_flag = 3
        if(self.pp3list):
            ui.display(self.pp3list)
        else:
            ui.reset()

    def preheatpattern4(self):
        ui.reset()
        self.select_flag = 4
        if(self.pp4list):
            ui.display(self.pp4list)
        else:
            ui.reset()

    def preheatpattern5(self):
        ui.reset()
        self.select_flag = 5
        if(self.pp5list):
            ui.display(self.pp5list)
        else:
            ui.reset()

    def preheatpattern6(self):
        ui.reset()
        self.select_flag = 6
        if(self.pp6list):
            ui.display(self.pp6list)
        else:
            ui.reset()

    def preheatpattern7(self):
        ui.reset()
        self.select_flag = 7
        if(self.pp7list):
            ui.display(self.pp7list)
        else:
            ui.reset()

    def preheatpattern8(self):
        ui.reset()
        self.select_flag = 8
        if(self.pp8list):
            ui.display(self.pp8list)
        else:
            ui.reset()

    def preheatpattern9(self):
        ui.reset()
        self.select_flag = 9
        if(self.pp9list):
            ui.display(self.pp9list)
        else:
            ui.reset()

    def preheatpattern10(self):
        ui.reset()
        self.select_flag = 10
        if(self.pp10list):
            ui.display(self.pp10list)
        else:
            ui.reset()

    def preheatpattern11(self):
        ui.reset()
        self.select_flag = 11
        if(self.pp11list):
            ui.display(self.pp11list)
        else:
            ui.reset()

    def skirtf(self):
        ui.reset()
        self.select_flag = 12
        if(self.skirtlist):
            ui.display(self.skirtlist)
        else:
            ui.reset()

    def infillf(self):
        ui.reset()
        self.select_flag = 13
        if(self.infilllist):
            ui.display(self.infilllist)
        else:
            ui.reset()

    def skinf(self):
        ui.reset()
        self.select_flag = 14
        if(self.skinlist):
            ui.display(self.skinlist)
        else:
            ui.reset()

    def innercontourf(self):
        ui.reset()
        self.select_flag = 15
        if(self.iclist):
            ui.display(self.iclist)
        else:
            ui.reset()

    def outercontourf(self):
        ui.reset()
        self.select_flag = 16
        if(self.oclist):
            ui.display(self.oclist)
        else:
            ui.reset()

    def appendList(self,listname2):
        self.csvData.append(listname2)

    def generateParameterFile(self):
        file_nm = "/globalparam.csv"

        if(str(self.outputfolder.toPlainText()) == ''):
            QtGui.QMessageBox.warning(None,"Warning","Please enter the Output/Destination in the respective field")
        else:
            path = os.path.join(os.getcwd(),self.parent_folder + file_nm)
            if not os.path.exists(os.path.dirname(path)):
                try:
                    os.makedirs(os.path.dirname(path))
                except OSError as exc:
                    if exc.errno != errno.EEXIST:
                        raise

        self.csvData = []
        ui.appendList(self.pp1list)
        ui.appendList(self.pp2list)
        ui.appendList(self.pp3list)
        ui.appendList(self.pp4list)
        ui.appendList(self.pp5list)
        ui.appendList(self.pp6list)
        ui.appendList(self.pp7list)
        ui.appendList(self.pp8list)
        ui.appendList(self.pp9list)
        ui.appendList(self.pp10list)
        ui.appendList(self.pp11list)
        ui.appendList(self.skirtlist)
        ui.appendList(self.oclist)
        ui.appendList(self.iclist)
        ui.appendList(self.infilllist)
        ui.appendList(self.skinlist)

        file3 = open(path,"a")
        with file3 as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(self.csvData)

        file3.close()

    def simulate(self):
        print("Work In Progress")

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = QtGui.QMainWindow()
    ui = Ui_window()
    ui.setupUi(window)
    count = 1
    x_prev,y_prev = (0,0)
    folder = ""
    window.show()
    sys.exit(app.exec_())
