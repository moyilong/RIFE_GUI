# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\RIFE_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RIFEDialog(object):
    def setupUi(self, RIFEDialog):
        RIFEDialog.setObjectName("RIFEDialog")
        RIFEDialog.setWindowModality(QtCore.Qt.WindowModal)
        RIFEDialog.resize(876, 467)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RIFEDialog.sizePolicy().hasHeightForWidth())
        RIFEDialog.setSizePolicy(sizePolicy)
        self.gridLayout_10 = QtWidgets.QGridLayout(RIFEDialog)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.MainFrame = QtWidgets.QFrame(RIFEDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainFrame.sizePolicy().hasHeightForWidth())
        self.MainFrame.setSizePolicy(sizePolicy)
        self.MainFrame.setObjectName("MainFrame")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.MainFrame)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.tabWidget = QtWidgets.QTabWidget(self.MainFrame)
        self.tabWidget.setObjectName("tabWidget")
        self.step1 = QtWidgets.QWidget()
        self.step1.setEnabled(True)
        self.step1.setObjectName("step1")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.step1)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.InputBrowser = QtWidgets.QPushButton(self.step1)
        self.InputBrowser.setObjectName("InputBrowser")
        self.gridLayout.addWidget(self.InputBrowser, 0, 1, 1, 1)
        self.OutputBrowser = QtWidgets.QPushButton(self.step1)
        self.OutputBrowser.setObjectName("OutputBrowser")
        self.gridLayout.addWidget(self.OutputBrowser, 1, 1, 1, 1)
        self.OneLineShotPath = QtWidgets.QTextEdit(self.step1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OneLineShotPath.sizePolicy().hasHeightForWidth())
        self.OneLineShotPath.setSizePolicy(sizePolicy)
        self.OneLineShotPath.setObjectName("OneLineShotPath")
        self.gridLayout.addWidget(self.OneLineShotPath, 4, 0, 1, 1)
        self.FFmpegPath = QtWidgets.QTextEdit(self.step1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FFmpegPath.sizePolicy().hasHeightForWidth())
        self.FFmpegPath.setSizePolicy(sizePolicy)
        self.FFmpegPath.setObjectName("FFmpegPath")
        self.gridLayout.addWidget(self.FFmpegPath, 2, 0, 1, 1)
        self.FFmpegBrowser = QtWidgets.QPushButton(self.step1)
        self.FFmpegBrowser.setObjectName("FFmpegBrowser")
        self.gridLayout.addWidget(self.FFmpegBrowser, 2, 1, 1, 1)
        self.RIFEBrowser = QtWidgets.QPushButton(self.step1)
        self.RIFEBrowser.setObjectName("RIFEBrowser")
        self.gridLayout.addWidget(self.RIFEBrowser, 3, 1, 1, 1)
        self.InputFileName = QtWidgets.QTextEdit(self.step1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputFileName.sizePolicy().hasHeightForWidth())
        self.InputFileName.setSizePolicy(sizePolicy)
        self.InputFileName.setObjectName("InputFileName")
        self.gridLayout.addWidget(self.InputFileName, 0, 0, 1, 1)
        self.OneLineShotBrowser = QtWidgets.QPushButton(self.step1)
        self.OneLineShotBrowser.setObjectName("OneLineShotBrowser")
        self.gridLayout.addWidget(self.OneLineShotBrowser, 4, 1, 1, 1)
        self.RIFEPath = QtWidgets.QTextEdit(self.step1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RIFEPath.sizePolicy().hasHeightForWidth())
        self.RIFEPath.setSizePolicy(sizePolicy)
        self.RIFEPath.setObjectName("RIFEPath")
        self.gridLayout.addWidget(self.RIFEPath, 3, 0, 1, 1)
        self.OutputFolder = QtWidgets.QTextEdit(self.step1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OutputFolder.sizePolicy().hasHeightForWidth())
        self.OutputFolder.setSizePolicy(sizePolicy)
        self.OutputFolder.setObjectName("OutputFolder")
        self.gridLayout.addWidget(self.OutputFolder, 1, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.InputFPS = QtWidgets.QLineEdit(self.step1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputFPS.sizePolicy().hasHeightForWidth())
        self.InputFPS.setSizePolicy(sizePolicy)
        self.InputFPS.setObjectName("InputFPS")
        self.horizontalLayout.addWidget(self.InputFPS)
        self.InterpExpReminder = QtWidgets.QLabel(self.step1)
        self.InterpExpReminder.setObjectName("InterpExpReminder")
        self.horizontalLayout.addWidget(self.InterpExpReminder)
        self.ExpSelecter = QtWidgets.QComboBox(self.step1)
        self.ExpSelecter.setObjectName("ExpSelecter")
        self.ExpSelecter.addItem("")
        self.ExpSelecter.addItem("")
        self.ExpSelecter.addItem("")
        self.horizontalLayout.addWidget(self.ExpSelecter)
        self.OutputFPSReminder = QtWidgets.QLabel(self.step1)
        self.OutputFPSReminder.setObjectName("OutputFPSReminder")
        self.horizontalLayout.addWidget(self.OutputFPSReminder)
        self.gridLayout_9.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.tabWidget.addTab(self.step1, "")
        self.step2 = QtWidgets.QWidget()
        self.step2.setObjectName("step2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.step2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.PresetReminder = QtWidgets.QLabel(self.step2)
        self.PresetReminder.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.PresetReminder.setObjectName("PresetReminder")
        self.gridLayout_3.addWidget(self.PresetReminder, 0, 12, 1, 1)
        self.BitrateSelector = QtWidgets.QDoubleSpinBox(self.step2)
        self.BitrateSelector.setObjectName("BitrateSelector")
        self.gridLayout_3.addWidget(self.BitrateSelector, 0, 4, 1, 1)
        self.ScdetReminder = QtWidgets.QLabel(self.step2)
        self.ScdetReminder.setObjectName("ScdetReminder")
        self.gridLayout_3.addWidget(self.ScdetReminder, 0, 7, 1, 1)
        self.ScdetSelector = QtWidgets.QSpinBox(self.step2)
        self.ScdetSelector.setMinimum(1)
        self.ScdetSelector.setObjectName("ScdetSelector")
        self.gridLayout_3.addWidget(self.ScdetSelector, 0, 8, 1, 1)
        self.PresetSelector = QtWidgets.QComboBox(self.step2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PresetSelector.sizePolicy().hasHeightForWidth())
        self.PresetSelector.setSizePolicy(sizePolicy)
        self.PresetSelector.setObjectName("PresetSelector")
        self.PresetSelector.addItem("")
        self.PresetSelector.addItem("")
        self.PresetSelector.addItem("")
        self.PresetSelector.addItem("")
        self.PresetSelector.addItem("")
        self.PresetSelector.addItem("")
        self.PresetSelector.addItem("")
        self.gridLayout_3.addWidget(self.PresetSelector, 0, 13, 1, 1)
        self.TargetBitrateReminder = QtWidgets.QLabel(self.step2)
        self.TargetBitrateReminder.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.TargetBitrateReminder.setObjectName("TargetBitrateReminder")
        self.gridLayout_3.addWidget(self.TargetBitrateReminder, 0, 3, 1, 1)
        self.ScdetTSelector = QtWidgets.QDoubleSpinBox(self.step2)
        self.ScdetTSelector.setObjectName("ScdetTSelector")
        self.gridLayout_3.addWidget(self.ScdetTSelector, 0, 10, 1, 1)
        self.CRFReminder = QtWidgets.QLabel(self.step2)
        self.CRFReminder.setObjectName("CRFReminder")
        self.gridLayout_3.addWidget(self.CRFReminder, 0, 0, 1, 1)
        self.ScedetTReminder = QtWidgets.QLabel(self.step2)
        self.ScedetTReminder.setObjectName("ScedetTReminder")
        self.gridLayout_3.addWidget(self.ScedetTReminder, 0, 9, 1, 1)
        self.TargetBitrateMeasure = QtWidgets.QLabel(self.step2)
        self.TargetBitrateMeasure.setObjectName("TargetBitrateMeasure")
        self.gridLayout_3.addWidget(self.TargetBitrateMeasure, 0, 5, 1, 1)
        self.CRFSelector = QtWidgets.QSpinBox(self.step2)
        self.CRFSelector.setMinimum(1)
        self.CRFSelector.setMaximum(51)
        self.CRFSelector.setObjectName("CRFSelector")
        self.gridLayout_3.addWidget(self.CRFSelector, 0, 1, 1, 1)
        self.ScdetTMark = QtWidgets.QLabel(self.step2)
        self.ScdetTMark.setObjectName("ScdetTMark")
        self.gridLayout_3.addWidget(self.ScdetTMark, 0, 11, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.DebugChecker = QtWidgets.QCheckBox(self.step2)
        self.DebugChecker.setObjectName("DebugChecker")
        self.gridLayout_11.addWidget(self.DebugChecker, 7, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.UHDChecker = QtWidgets.QCheckBox(self.step2)
        self.UHDChecker.setObjectName("UHDChecker")
        self.gridLayout_5.addWidget(self.UHDChecker, 0, 0, 1, 1)
        self.CropReminder = QtWidgets.QLabel(self.step2)
        self.CropReminder.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.CropReminder.setObjectName("CropReminder")
        self.gridLayout_5.addWidget(self.CropReminder, 0, 1, 1, 1)
        self.ResizeReminder = QtWidgets.QLabel(self.step2)
        self.ResizeReminder.setObjectName("ResizeReminder")
        self.gridLayout_5.addWidget(self.ResizeReminder, 0, 3, 1, 1)
        self.HwaccelChecker = QtWidgets.QCheckBox(self.step2)
        self.HwaccelChecker.setObjectName("HwaccelChecker")
        self.gridLayout_5.addWidget(self.HwaccelChecker, 0, 5, 1, 1)
        self.CropSettings = QtWidgets.QLineEdit(self.step2)
        self.CropSettings.setObjectName("CropSettings")
        self.gridLayout_5.addWidget(self.CropSettings, 0, 2, 1, 1)
        self.ResizeSettings = QtWidgets.QLineEdit(self.step2)
        self.ResizeSettings.setObjectName("ResizeSettings")
        self.gridLayout_5.addWidget(self.ResizeSettings, 0, 4, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_5, 2, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.step2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_11.addWidget(self.line, 5, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.StartFrame = QtWidgets.QLineEdit(self.step2)
        self.StartFrame.setObjectName("StartFrame")
        self.gridLayout_4.addWidget(self.StartFrame, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.step2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 1, 1, 1)
        self.StartCntFrame = QtWidgets.QLineEdit(self.step2)
        self.StartCntFrame.setObjectName("StartCntFrame")
        self.gridLayout_4.addWidget(self.StartCntFrame, 1, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.step2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 4, 1, 1)
        self.StartChunk = QtWidgets.QLineEdit(self.step2)
        self.StartChunk.setObjectName("StartChunk")
        self.gridLayout_4.addWidget(self.StartChunk, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.step2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 2, 1, 1)
        self.AutoSet = QtWidgets.QPushButton(self.step2)
        self.AutoSet.setObjectName("AutoSet")
        self.gridLayout_4.addWidget(self.AutoSet, 1, 0, 1, 1)
        self.AutoSetReminder = QtWidgets.QLabel(self.step2)
        self.AutoSetReminder.setObjectName("AutoSetReminder")
        self.gridLayout_4.addWidget(self.AutoSetReminder, 0, 0, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_4, 1, 0, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.AccurateChecker = QtWidgets.QCheckBox(self.step2)
        self.AccurateChecker.setObjectName("AccurateChecker")
        self.gridLayout_7.addWidget(self.AccurateChecker, 0, 0, 1, 1)
        self.ReverseChecker = QtWidgets.QCheckBox(self.step2)
        self.ReverseChecker.setObjectName("ReverseChecker")
        self.gridLayout_7.addWidget(self.ReverseChecker, 0, 1, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_7, 6, 0, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.RenderOnlyChecker = QtWidgets.QCheckBox(self.step2)
        self.RenderOnlyChecker.setObjectName("RenderOnlyChecker")
        self.gridLayout_6.addWidget(self.RenderOnlyChecker, 0, 6, 1, 1)
        self.RIFEOnlyChecker = QtWidgets.QCheckBox(self.step2)
        self.RIFEOnlyChecker.setObjectName("RIFEOnlyChecker")
        self.gridLayout_6.addWidget(self.RIFEOnlyChecker, 0, 5, 1, 1)
        self.QuickExtractChecker = QtWidgets.QCheckBox(self.step2)
        self.QuickExtractChecker.setObjectName("QuickExtractChecker")
        self.gridLayout_6.addWidget(self.QuickExtractChecker, 0, 3, 1, 1)
        self.PauseChecker = QtWidgets.QCheckBox(self.step2)
        self.PauseChecker.setObjectName("PauseChecker")
        self.gridLayout_6.addWidget(self.PauseChecker, 0, 2, 1, 1)
        self.ExtractOnlyChecker = QtWidgets.QCheckBox(self.step2)
        self.ExtractOnlyChecker.setObjectName("ExtractOnlyChecker")
        self.gridLayout_6.addWidget(self.ExtractOnlyChecker, 0, 4, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_6, 4, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.step2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_11.addWidget(self.line_2, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_11, 0, 0, 1, 1)
        self.tabWidget.addTab(self.step2, "")
        self.step3 = QtWidgets.QWidget()
        self.step3.setAcceptDrops(True)
        self.step3.setWhatsThis("")
        self.step3.setObjectName("step3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.step3)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.OptionCheck = QtWidgets.QTextEdit(self.step3)
        self.OptionCheck.setObjectName("OptionCheck")
        self.verticalLayout_5.addWidget(self.OptionCheck)
        self.ProcessStart = QtWidgets.QPushButton(self.step3)
        self.ProcessStart.setObjectName("ProcessStart")
        self.verticalLayout_5.addWidget(self.ProcessStart)
        self.gridLayout_8.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.tabWidget.addTab(self.step3, "")
        self.gridLayout_12.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.CloseButton = QtWidgets.QPushButton(self.MainFrame)
        self.CloseButton.setObjectName("CloseButton")
        self.gridLayout_12.addWidget(self.CloseButton, 1, 0, 1, 1)
        self.gridLayout_10.addWidget(self.MainFrame, 0, 0, 1, 1)

        self.retranslateUi(RIFEDialog)
        self.tabWidget.setCurrentIndex(0)
        self.CloseButton.clicked.connect(RIFEDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(RIFEDialog)
        RIFEDialog.setTabOrder(self.tabWidget, self.InputBrowser)
        RIFEDialog.setTabOrder(self.InputBrowser, self.InputFileName)
        RIFEDialog.setTabOrder(self.InputFileName, self.OutputBrowser)
        RIFEDialog.setTabOrder(self.OutputBrowser, self.OutputFolder)
        RIFEDialog.setTabOrder(self.OutputFolder, self.FFmpegBrowser)
        RIFEDialog.setTabOrder(self.FFmpegBrowser, self.FFmpegPath)
        RIFEDialog.setTabOrder(self.FFmpegPath, self.RIFEBrowser)
        RIFEDialog.setTabOrder(self.RIFEBrowser, self.RIFEPath)
        RIFEDialog.setTabOrder(self.RIFEPath, self.OneLineShotBrowser)
        RIFEDialog.setTabOrder(self.OneLineShotBrowser, self.OneLineShotPath)
        RIFEDialog.setTabOrder(self.OneLineShotPath, self.ExpSelecter)
        RIFEDialog.setTabOrder(self.ExpSelecter, self.InputFPS)
        RIFEDialog.setTabOrder(self.InputFPS, self.CRFSelector)
        RIFEDialog.setTabOrder(self.CRFSelector, self.StartFrame)
        RIFEDialog.setTabOrder(self.StartFrame, self.StartCntFrame)
        RIFEDialog.setTabOrder(self.StartCntFrame, self.UHDChecker)
        RIFEDialog.setTabOrder(self.UHDChecker, self.HwaccelChecker)
        RIFEDialog.setTabOrder(self.HwaccelChecker, self.RenderOnlyChecker)
        RIFEDialog.setTabOrder(self.RenderOnlyChecker, self.AccurateChecker)
        RIFEDialog.setTabOrder(self.AccurateChecker, self.ReverseChecker)
        RIFEDialog.setTabOrder(self.ReverseChecker, self.DebugChecker)
        RIFEDialog.setTabOrder(self.DebugChecker, self.OptionCheck)
        RIFEDialog.setTabOrder(self.OptionCheck, self.ProcessStart)
        RIFEDialog.setTabOrder(self.ProcessStart, self.CloseButton)

    def retranslateUi(self, RIFEDialog):
        _translate = QtCore.QCoreApplication.translate
        RIFEDialog.setWindowTitle(_translate("RIFEDialog", "RIFE一条龙服务"))
        self.InputBrowser.setText(_translate("RIFEDialog", "设置输入文件路径"))
        self.OutputBrowser.setText(_translate("RIFEDialog", "设置输出文件夹"))
        self.OneLineShotPath.setPlaceholderText(_translate("RIFEDialog", "one_line_shot_args.exe路径"))
        self.FFmpegPath.setPlaceholderText(_translate("RIFEDialog", "FFmpeg.exe路径"))
        self.FFmpegBrowser.setText(_translate("RIFEDialog", "设置FFmpeg路径"))
        self.RIFEBrowser.setText(_translate("RIFEDialog", "设置RIFE核心路径"))
        self.InputFileName.setPlaceholderText(_translate("RIFEDialog", "打开文件(推荐.mp4, .mkv)"))
        self.OneLineShotBrowser.setText(_translate("RIFEDialog", "一条龙程序路径"))
        self.RIFEPath.setPlaceholderText(_translate("RIFEDialog", "inference_img_only.py路径"))
        self.OutputFolder.setPlaceholderText(_translate("RIFEDialog", "输出文件夹(随便输入一个文件)"))
        self.InputFPS.setPlaceholderText(_translate("RIFEDialog", "输入视频的帧率"))
        self.InterpExpReminder.setText(_translate("RIFEDialog", "选择补帧倍率："))
        self.ExpSelecter.setItemText(0, _translate("RIFEDialog", "x2"))
        self.ExpSelecter.setItemText(1, _translate("RIFEDialog", "x4"))
        self.ExpSelecter.setItemText(2, _translate("RIFEDialog", "x8"))
        self.OutputFPSReminder.setText(_translate("RIFEDialog", "预计输出帧率："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.step1), _translate("RIFEDialog", "Step1：输入文件"))
        self.PresetReminder.setText(_translate("RIFEDialog", "  选择压制预设："))
        self.ScdetReminder.setText(_translate("RIFEDialog", "转场灵敏度："))
        self.PresetSelector.setItemText(0, _translate("RIFEDialog", "fast[软编、硬编]"))
        self.PresetSelector.setItemText(1, _translate("RIFEDialog", "medium[软编、硬编]"))
        self.PresetSelector.setItemText(2, _translate("RIFEDialog", "slow[软编、硬编]"))
        self.PresetSelector.setItemText(3, _translate("RIFEDialog", "veryslow[软编]"))
        self.PresetSelector.setItemText(4, _translate("RIFEDialog", "hq[硬编，高质量]"))
        self.PresetSelector.setItemText(5, _translate("RIFEDialog", "llhq[硬编，低延迟编码，压缩率低]"))
        self.PresetSelector.setItemText(6, _translate("RIFEDialog", "loseless[硬编，无损]"))
        self.TargetBitrateReminder.setText(_translate("RIFEDialog", "目标码率："))
        self.CRFReminder.setText(_translate("RIFEDialog", "恒定质量控制参数(CRF)："))
        self.ScedetTReminder.setText(_translate("RIFEDialog", "转场最低间隔"))
        self.TargetBitrateMeasure.setText(_translate("RIFEDialog", "M "))
        self.ScdetTMark.setText(_translate("RIFEDialog", "s"))
        self.DebugChecker.setText(_translate("RIFEDialog", "Debug"))
        self.UHDChecker.setText(_translate("RIFEDialog", "UHD适配模式"))
        self.CropReminder.setText(_translate("RIFEDialog", "   裁切参数(不裁切填0)"))
        self.ResizeReminder.setText(_translate("RIFEDialog", "   缩放大小"))
        self.HwaccelChecker.setText(_translate("RIFEDialog", "开启硬件加速（废话）"))
        self.CropSettings.setPlaceholderText(_translate("RIFEDialog", "UHD默认3840:1608:0:276, HD默认1920:804:0:138"))
        self.ResizeSettings.setPlaceholderText(_translate("RIFEDialog", "如320x180"))
        self.StartFrame.setPlaceholderText(_translate("RIFEDialog", "起始帧数(startframe)"))
        self.label_2.setText(_translate("RIFEDialog", "起始块数："))
        self.StartCntFrame.setPlaceholderText(_translate("RIFEDialog", "补帧序列起始帧数"))
        self.label_3.setText(_translate("RIFEDialog", "补帧序列起始帧数："))
        self.StartChunk.setPlaceholderText(_translate("RIFEDialog", "起始块数(chunk)"))
        self.label.setText(_translate("RIFEDialog", "原视频起始帧数："))
        self.AutoSet.setText(_translate("RIFEDialog", "点我！"))
        self.AutoSetReminder.setText(_translate("RIFEDialog", "自动设置"))
        self.AccurateChecker.setText(_translate("RIFEDialog", "精确光流（慢）"))
        self.ReverseChecker.setText(_translate("RIFEDialog", "反向光流"))
        self.RenderOnlyChecker.setText(_translate("RIFEDialog", "只进行渲染"))
        self.RIFEOnlyChecker.setText(_translate("RIFEDialog", "只进行补帧"))
        self.QuickExtractChecker.setText(_translate("RIFEDialog", "快速拆帧"))
        self.PauseChecker.setText(_translate("RIFEDialog", "暂停模式"))
        self.ExtractOnlyChecker.setText(_translate("RIFEDialog", "只进行拆帧"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.step2), _translate("RIFEDialog", "Step2：选择模式、功能"))
        self.ProcessStart.setText(_translate("RIFEDialog", "一条龙开始"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.step3), _translate("RIFEDialog", "Step3：确认选项，渲染"))
        self.CloseButton.setText(_translate("RIFEDialog", "保存设置并关闭"))
