# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1117, 783)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setStyleSheet("font: 75 14pt \"Arial\";\n"
"")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.original_img = QtWidgets.QLabel(self.groupBox)
        self.original_img.setMinimumSize(QtCore.QSize(456, 353))
        self.original_img.setMaximumSize(QtCore.QSize(456, 353))
        self.original_img.setText("")
        self.original_img.setPixmap(QtGui.QPixmap("../asset/schindler.png"))
        self.original_img.setScaledContents(True)
        self.original_img.setObjectName("original_img")
        self.gridLayout_3.addWidget(self.original_img, 1, 0, 1, 4)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 2, 0, 1, 4)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 4, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_3.setStyleSheet("font: 75 14pt \"Arial\";")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.gridLayout_2.addWidget(self.groupBox_3, 5, 4, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_4.setStyleSheet("font: 75 14pt \"Arial\";")
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_4)
        self.textBrowser.setStyleSheet("font: 10pt \"Arial\";")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.gridLayout_2.addWidget(self.groupBox_4, 0, 4, 5, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.original_figure = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.original_figure.setFont(font)
        self.original_figure.setStyleSheet("background-color: rgb(226, 226, 226);")
        self.original_figure.setObjectName("original_figure")
        self.gridLayout_5.addWidget(self.original_figure, 1, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_5)
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: rgb(226, 226, 226);")
        self.label_12.setObjectName("label_12")
        self.gridLayout_5.addWidget(self.label_12, 3, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_5)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(226, 226, 226);")
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_5)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_5)
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: rgb(0, 211, 102);")
        self.label_10.setObjectName("label_10")
        self.gridLayout_5.addWidget(self.label_10, 3, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox_5)
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: rgb(226, 226, 226);")
        self.label_13.setObjectName("label_13")
        self.gridLayout_5.addWidget(self.label_13, 4, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_5)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 2, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_5.addWidget(self.checkBox, 5, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_5)
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: rgb(226, 75, 0);")
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 4, 0, 2, 1)
        self.gridLayout_2.addWidget(self.groupBox_5, 4, 0, 2, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_2.setMaximumSize(QtCore.QSize(11111111, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 2, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 3, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem1, 7, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setMaximumSize(QtCore.QSize(300, 200))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../asset/schindler.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 5)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setMinimumSize(QtCore.QSize(0, 0))
        self.label_9.setMaximumSize(QtCore.QSize(300, 200))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("../asset/schindler.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 5, 0, 1, 5)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 2, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_19 = QtWidgets.QLabel(self.groupBox_6)
        self.label_19.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.gridLayout_6.addWidget(self.label_19, 0, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox_6)
        self.label_14.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.label_14.setObjectName("label_14")
        self.gridLayout_6.addWidget(self.label_14, 0, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox_6)
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.label_15.setObjectName("label_15")
        self.gridLayout_6.addWidget(self.label_15, 6, 1, 1, 1)
        self.horizontalSlider = QtWidgets.QSlider(self.groupBox_6)
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(50)
        self.horizontalSlider.setProperty("value", 25)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout_6.addWidget(self.horizontalSlider, 0, 3, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_6.addWidget(self.pushButton, 6, 3, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_6.addWidget(self.lineEdit, 6, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_6.addWidget(self.pushButton_3, 7, 1, 1, 3)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_6.addWidget(self.pushButton_5, 8, 1, 1, 3)
        self.gridLayout_4.addWidget(self.groupBox_6, 9, 0, 1, 5)
        self.reco = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.reco.setFont(font)
        self.reco.setStyleSheet("background-color: rgb(226, 226, 226);")
        self.reco.setAlignment(QtCore.Qt.AlignCenter)
        self.reco.setObjectName("reco")
        self.gridLayout_4.addWidget(self.reco, 6, 0, 1, 5)
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 2, 6, 1)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1117, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionConfigure = QtWidgets.QAction(MainWindow)
        self.actionConfigure.setObjectName("actionConfigure")
        self.actionSave_Image = QtWidgets.QAction(MainWindow)
        self.actionSave_Image.setObjectName("actionSave_Image")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit_2 = QtWidgets.QAction(MainWindow)
        self.actionExit_2.setObjectName("actionExit_2")
        self.actionAbout_this = QtWidgets.QAction(MainWindow)
        self.actionAbout_this.setObjectName("actionAbout_this")
        self.actionUser_Guide = QtWidgets.QAction(MainWindow)
        self.actionUser_Guide.setObjectName("actionUser_Guide")
        self.actionCapture_New_Image = QtWidgets.QAction(MainWindow)
        self.actionCapture_New_Image.setObjectName("actionCapture_New_Image")
        self.actionre_Training_NN = QtWidgets.QAction(MainWindow)
        self.actionre_Training_NN.setObjectName("actionre_Training_NN")
        self.actionExpand = QtWidgets.QAction(MainWindow)
        self.actionExpand.setObjectName("actionExpand")
        self.actionNormal_View = QtWidgets.QAction(MainWindow)
        self.actionNormal_View.setObjectName("actionNormal_View")
        self.actionMininal_View = QtWidgets.QAction(MainWindow)
        self.actionMininal_View.setObjectName("actionMininal_View")
        self.actionOpen_Log = QtWidgets.QAction(MainWindow)
        self.actionOpen_Log.setObjectName("actionOpen_Log")
        self.actionNN_List = QtWidgets.QAction(MainWindow)
        self.actionNN_List.setObjectName("actionNN_List")
        self.actionSave_Log = QtWidgets.QAction(MainWindow)
        self.actionSave_Log.setObjectName("actionSave_Log")
        self.actionConnect_TaTu = QtWidgets.QAction(MainWindow)
        self.actionConnect_TaTu.setObjectName("actionConnect_TaTu")
        self.actioncollect_images = QtWidgets.QAction(MainWindow)
        self.actioncollect_images.setObjectName("actioncollect_images")
        self.actionMerge_images = QtWidgets.QAction(MainWindow)
        self.actionMerge_images.setObjectName("actionMerge_images")
        self.menuFile.addAction(self.actionConfigure)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_Log)
        self.menuFile.addAction(self.actionOpen_Log)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_Image)
        self.menuFile.addAction(self.actionExit)
        self.menuSetting.addAction(self.actionConnect_TaTu)
        self.menuSetting.addSeparator()
        self.menuSetting.addAction(self.actioncollect_images)
        self.menuSetting.addSeparator()
        self.menuSetting.addAction(self.actionMerge_images)
        self.menuSetting.addSeparator()
        self.menuSetting.addAction(self.actionre_Training_NN)
        self.menuHelp.addAction(self.actionAbout_this)
        self.menuHelp.addAction(self.actionUser_Guide)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Camera"))
        self.label_4.setText(_translate("MainWindow", "TaTu Offline"))
        self.pushButton_2.setText(_translate("MainWindow", "Run"))
        self.pushButton_4.setText(_translate("MainWindow", "Stop"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Log Record"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Test Summary"))
        self.original_figure.setText(_translate("MainWindow", "N.A."))
        self.label_12.setText(_translate("MainWindow", "0"))
        self.label_7.setText(_translate("MainWindow", "N.A."))
        self.label_6.setText(_translate("MainWindow", "Camera Show:"))
        self.label_10.setText(_translate("MainWindow", "Test case Passed:"))
        self.label_13.setText(_translate("MainWindow", "0"))
        self.label_8.setText(_translate("MainWindow", "Recognized As:"))
        self.checkBox.setText(_translate("MainWindow", "Save Image of  Failed Test Case"))
        self.label_11.setText(_translate("MainWindow", "Test case Failed:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Image"))
        self.label_3.setText(_translate("MainWindow", "Location"))
        self.label.setText(_translate("MainWindow", "Cipped Image"))
        self.groupBox_6.setTitle(_translate("MainWindow", " Configure"))
        self.label_19.setText(_translate("MainWindow", "25"))
        self.label_14.setText(_translate("MainWindow", "Sample Rate:"))
        self.label_15.setText(_translate("MainWindow", "Label:"))
        self.pushButton.setText(_translate("MainWindow", "Save Image"))
        self.pushButton_3.setText(_translate("MainWindow", "Merge Image"))
        self.pushButton_5.setText(_translate("MainWindow", "Re-training NN"))
        self.reco.setText(_translate("MainWindow", "N.A."))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSetting.setTitle(_translate("MainWindow", "Functions"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionConfigure.setText(_translate("MainWindow", "Configure"))
        self.actionSave_Image.setText(_translate("MainWindow", "Save Window image"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit_2.setText(_translate("MainWindow", "Exit"))
        self.actionAbout_this.setText(_translate("MainWindow", "About this"))
        self.actionUser_Guide.setText(_translate("MainWindow", "User Guide"))
        self.actionCapture_New_Image.setText(_translate("MainWindow", "re-Training image"))
        self.actionre_Training_NN.setText(_translate("MainWindow", "re-Training NN"))
        self.actionExpand.setText(_translate("MainWindow", "Expand View"))
        self.actionNormal_View.setText(_translate("MainWindow", "Normal View"))
        self.actionMininal_View.setText(_translate("MainWindow", "Mininal View"))
        self.actionOpen_Log.setText(_translate("MainWindow", "Open Log"))
        self.actionNN_List.setText(_translate("MainWindow", "Show NN List"))
        self.actionSave_Log.setText(_translate("MainWindow", "Save Log"))
        self.actionConnect_TaTu.setText(_translate("MainWindow", "Connect TaTu"))
        self.actioncollect_images.setText(_translate("MainWindow", "Collect images"))
        self.actionMerge_images.setText(_translate("MainWindow", "Merge images"))
