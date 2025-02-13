# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        Form.setMinimumSize(QtCore.QSize(800, 600))
        Form.setMaximumSize(QtCore.QSize(800, 600))
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 40, 670, 461))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_1 = QtWidgets.QLabel(self.layoutWidget)
        self.label_1.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.horizontalLayout.addWidget(self.label_1)
        self.SourceFilePathInput = QtWidgets.QLineEdit(self.layoutWidget)
        self.SourceFilePathInput.setMinimumSize(QtCore.QSize(250, 0))
        self.SourceFilePathInput.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SourceFilePathInput.setFont(font)
        self.SourceFilePathInput.setDragEnabled(True)
        self.SourceFilePathInput.setObjectName("SourceFilePathInput")
        self.horizontalLayout.addWidget(self.SourceFilePathInput)
        self.SourceFileSelect = QtWidgets.QPushButton(self.layoutWidget)
        self.SourceFileSelect.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.SourceFileSelect.setFont(font)
        self.SourceFileSelect.setObjectName("SourceFileSelect")
        self.horizontalLayout.addWidget(self.SourceFileSelect)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.TargetPathInput = QtWidgets.QLineEdit(self.layoutWidget)
        self.TargetPathInput.setMinimumSize(QtCore.QSize(250, 0))
        self.TargetPathInput.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TargetPathInput.setFont(font)
        self.TargetPathInput.setInputMask("")
        self.TargetPathInput.setText("")
        self.TargetPathInput.setDragEnabled(True)
        self.TargetPathInput.setObjectName("TargetPathInput")
        self.horizontalLayout_2.addWidget(self.TargetPathInput)
        self.TargetSelect = QtWidgets.QPushButton(self.layoutWidget)
        self.TargetSelect.setMinimumSize(QtCore.QSize(100, 0))
        self.TargetSelect.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.TargetSelect.setFont(font)
        self.TargetSelect.setObjectName("TargetSelect")
        self.horizontalLayout_2.addWidget(self.TargetSelect)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.TableNameInput = QtWidgets.QLineEdit(self.layoutWidget)
        self.TableNameInput.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.TableNameInput.setFont(font)
        self.TableNameInput.setObjectName("TableNameInput")
        self.horizontalLayout_4.addWidget(self.TableNameInput)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.customtitlecheckBox = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.customtitlecheckBox.setFont(font)
        self.customtitlecheckBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.customtitlecheckBox.setChecked(False)
        self.customtitlecheckBox.setTristate(False)
        self.customtitlecheckBox.setObjectName("customtitlecheckBox")
        self.verticalLayout_4.addWidget(self.customtitlecheckBox)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_9.addWidget(self.label_5)
        self.customTime = QtWidgets.QLineEdit(self.layoutWidget)
        self.customTime.setEnabled(False)
        self.customTime.setObjectName("customTime")
        self.horizontalLayout_9.addWidget(self.customTime)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_10.addWidget(self.label_6)
        self.customName = QtWidgets.QLineEdit(self.layoutWidget)
        self.customName.setEnabled(False)
        self.customName.setObjectName("customName")
        self.horizontalLayout_10.addWidget(self.customName)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_10)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.customVID = QtWidgets.QLineEdit(self.layoutWidget)
        self.customVID.setEnabled(False)
        self.customVID.setObjectName("customVID")
        self.horizontalLayout_5.addWidget(self.customVID)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.customContent = QtWidgets.QLineEdit(self.layoutWidget)
        self.customContent.setEnabled(False)
        self.customContent.setObjectName("customContent")
        self.horizontalLayout_6.addWidget(self.customContent)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.isTime = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.isTime.setFont(font)
        self.isTime.setChecked(True)
        self.isTime.setObjectName("isTime")
        self.verticalLayout.addWidget(self.isTime)
        self.isName = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.isName.setFont(font)
        self.isName.setChecked(True)
        self.isName.setObjectName("isName")
        self.verticalLayout.addWidget(self.isName)
        self.isContent = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.isContent.setFont(font)
        self.isContent.setChecked(True)
        self.isContent.setObjectName("isContent")
        self.verticalLayout.addWidget(self.isContent)
        self.isVID = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.isVID.setFont(font)
        self.isVID.setChecked(True)
        self.isVID.setObjectName("isVID")
        self.verticalLayout.addWidget(self.isVID)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.line_3 = QtWidgets.QFrame(self.layoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_3.addWidget(self.line_3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.isOnefile = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.isOnefile.setFont(font)
        self.isOnefile.setChecked(True)
        self.isOnefile.setObjectName("isOnefile")
        self.verticalLayout_3.addWidget(self.isOnefile)
        self.OutTypecomboBox = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.OutTypecomboBox.setFont(font)
        self.OutTypecomboBox.setDuplicatesEnabled(False)
        self.OutTypecomboBox.setObjectName("OutTypecomboBox")
        self.OutTypecomboBox.addItem("")
        self.OutTypecomboBox.addItem("")
        self.verticalLayout_3.addWidget(self.OutTypecomboBox)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.line_2 = QtWidgets.QFrame(self.layoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.StartButton = QtWidgets.QPushButton(self.layoutWidget)
        self.StartButton.setMinimumSize(QtCore.QSize(650, 40))
        self.StartButton.setMaximumSize(QtCore.QSize(650, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.StartButton.setFont(font)
        self.StartButton.setObjectName("StartButton")
        self.verticalLayout_2.addWidget(self.StartButton)
        self.progressBar = QtWidgets.QProgressBar(self.layoutWidget)
        self.progressBar.setEnabled(True)
        self.progressBar.setMinimumSize(QtCore.QSize(650, 40))
        self.progressBar.setMaximumSize(QtCore.QSize(650, 40))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar, 0, QtCore.Qt.AlignHCenter)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "QQtoExcel v1.1"))
        self.label_1.setText(_translate("Form", "聊天记录地址："))
        self.SourceFileSelect.setText(_translate("Form", "选择"))
        self.label_2.setText(_translate("Form", "保存文件夹："))
        self.TargetSelect.setText(_translate("Form", "选择"))
        self.label_3.setText(_translate("Form", "工作表名："))
        self.customtitlecheckBox.setText(_translate("Form", "自定义可选项标题"))
        self.label_5.setText(_translate("Form", "时间标题"))
        self.label_6.setText(_translate("Form", "昵称标题"))
        self.label.setText(_translate("Form", "VID标题"))
        self.label_4.setText(_translate("Form", "内容标题"))
        self.isTime.setText(_translate("Form", "导出时间"))
        self.isName.setText(_translate("Form", "导出昵称"))
        self.isContent.setText(_translate("Form", "导出内容"))
        self.isVID.setText(_translate("Form", "导出VID"))
        self.label_7.setText(_translate("Form", "导出模式："))
        self.isOnefile.setText(_translate("Form", "单文件"))
        self.OutTypecomboBox.setItemText(0, _translate("Form", "按好友导出"))
        self.OutTypecomboBox.setItemText(1, _translate("Form", "按分组导出"))
        self.StartButton.setText(_translate("Form", "开始"))
