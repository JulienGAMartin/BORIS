# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'observation.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(967, 770)
        self.verticalLayout_12 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.leObservationId = QtGui.QLineEdit(Form)
        self.leObservationId.setObjectName(_fromUtf8("leObservationId"))
        self.horizontalLayout_2.addWidget(self.leObservationId)
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_2.addWidget(self.label_8)
        self.dteDate = QtGui.QDateTimeEdit(Form)
        self.dteDate.setCalendarPopup(True)
        self.dteDate.setObjectName(_fromUtf8("dteDate"))
        self.horizontalLayout_2.addWidget(self.dteDate)
        self.verticalLayout_12.addLayout(self.horizontalLayout_2)
        self.splitter_2 = QtGui.QSplitter(Form)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.splitter = QtGui.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_9 = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_2.addWidget(self.label_9)
        self.teDescription = QtGui.QTextEdit(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.teDescription.sizePolicy().hasHeightForWidth())
        self.teDescription.setSizePolicy(sizePolicy)
        self.teDescription.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.teDescription.setAcceptDrops(False)
        self.teDescription.setObjectName(_fromUtf8("teDescription"))
        self.verticalLayout_2.addWidget(self.teDescription)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.lbTimeOffset = QtGui.QLabel(self.layoutWidget)
        self.lbTimeOffset.setObjectName(_fromUtf8("lbTimeOffset"))
        self.horizontalLayout_6.addWidget(self.lbTimeOffset)
        self.rbAdd = QtGui.QRadioButton(self.layoutWidget)
        self.rbAdd.setChecked(True)
        self.rbAdd.setObjectName(_fromUtf8("rbAdd"))
        self.horizontalLayout_6.addWidget(self.rbAdd)
        self.rbSubstract = QtGui.QRadioButton(self.layoutWidget)
        self.rbSubstract.setObjectName(_fromUtf8("rbSubstract"))
        self.horizontalLayout_6.addWidget(self.rbSubstract)
        self.leTimeOffset = QtGui.QLineEdit(self.layoutWidget)
        self.leTimeOffset.setObjectName(_fromUtf8("leTimeOffset"))
        self.horizontalLayout_6.addWidget(self.leTimeOffset)
        self.teTimeOffset = QtGui.QTimeEdit(self.layoutWidget)
        self.teTimeOffset.setObjectName(_fromUtf8("teTimeOffset"))
        self.horizontalLayout_6.addWidget(self.teTimeOffset)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.label_3 = QtGui.QLabel(self.layoutWidget1)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_11.addWidget(self.label_3)
        self.twIndepVariables = QtGui.QTableWidget(self.layoutWidget1)
        self.twIndepVariables.setObjectName(_fromUtf8("twIndepVariables"))
        self.twIndepVariables.setColumnCount(3)
        self.twIndepVariables.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.twIndepVariables.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.twIndepVariables.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.twIndepVariables.setHorizontalHeaderItem(2, item)
        self.verticalLayout_11.addWidget(self.twIndepVariables)
        self.layoutWidget2 = QtGui.QWidget(self.splitter_2)
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.tabProjectType = QtGui.QTabWidget(self.layoutWidget2)
        self.tabProjectType.setEnabled(True)
        self.tabProjectType.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabProjectType.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabProjectType.setUsesScrollButtons(False)
        self.tabProjectType.setDocumentMode(False)
        self.tabProjectType.setTabsClosable(False)
        self.tabProjectType.setMovable(False)
        self.tabProjectType.setObjectName(_fromUtf8("tabProjectType"))
        self.tabVideo = QtGui.QWidget()
        self.tabVideo.setObjectName(_fromUtf8("tabVideo"))
        self.verticalLayout_14 = QtGui.QVBoxLayout(self.tabVideo)
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.tabWidget = QtGui.QTabWidget(self.tabVideo)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_player_1 = QtGui.QWidget()
        self.tab_player_1.setObjectName(_fromUtf8("tab_player_1"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_player_1)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.splitter_3 = QtGui.QSplitter(self.tab_player_1)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.layoutWidget3 = QtGui.QWidget(self.splitter_3)
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_5 = QtGui.QLabel(self.layoutWidget3)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_3.addWidget(self.label_5)
        self.twVideo1 = QtGui.QTableWidget(self.layoutWidget3)
        self.twVideo1.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.twVideo1.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.twVideo1.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.twVideo1.setObjectName(_fromUtf8("twVideo1"))
        self.twVideo1.setColumnCount(5)
        self.twVideo1.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.twVideo1.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.twVideo1.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.twVideo1.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.twVideo1.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.twVideo1.setHorizontalHeaderItem(4, item)
        self.verticalLayout_3.addWidget(self.twVideo1)
        self.layoutWidget4 = QtGui.QWidget(self.splitter_3)
        self.layoutWidget4.setObjectName(_fromUtf8("layoutWidget4"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pbAddVideo = QtGui.QPushButton(self.layoutWidget4)
        self.pbAddVideo.setObjectName(_fromUtf8("pbAddVideo"))
        self.horizontalLayout_3.addWidget(self.pbAddVideo)
        self.pbRemoveVideo = QtGui.QPushButton(self.layoutWidget4)
        self.pbRemoveVideo.setObjectName(_fromUtf8("pbRemoveVideo"))
        self.horizontalLayout_3.addWidget(self.pbRemoveVideo)
        self.pbAddMediaFromDir = QtGui.QPushButton(self.layoutWidget4)
        self.pbAddMediaFromDir.setObjectName(_fromUtf8("pbAddMediaFromDir"))
        self.horizontalLayout_3.addWidget(self.pbAddMediaFromDir)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.cbVisualizeSpectrogram = QtGui.QCheckBox(self.layoutWidget4)
        self.cbVisualizeSpectrogram.setObjectName(_fromUtf8("cbVisualizeSpectrogram"))
        self.verticalLayout.addWidget(self.cbVisualizeSpectrogram)
        self.cbCloseCurrentBehaviorsBetweenVideo = QtGui.QCheckBox(self.layoutWidget4)
        self.cbCloseCurrentBehaviorsBetweenVideo.setObjectName(_fromUtf8("cbCloseCurrentBehaviorsBetweenVideo"))
        self.verticalLayout.addWidget(self.cbCloseCurrentBehaviorsBetweenVideo)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        self.verticalLayout.addItem(spacerItem2)
        self.verticalLayout_5.addWidget(self.splitter_3)
        self.tabWidget.addTab(self.tab_player_1, _fromUtf8(""))
        self.tab_player_2 = QtGui.QWidget()
        self.tab_player_2.setObjectName(_fromUtf8("tab_player_2"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.tab_player_2)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.splitter_4 = QtGui.QSplitter(self.tab_player_2)
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName(_fromUtf8("splitter_4"))
        self.layoutWidget5 = QtGui.QWidget(self.splitter_4)
        self.layoutWidget5.setObjectName(_fromUtf8("layoutWidget5"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_2 = QtGui.QLabel(self.layoutWidget5)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_4.addWidget(self.label_2)
        self.twVideo2 = QtGui.QTableWidget(self.layoutWidget5)
        self.twVideo2.setObjectName(_fromUtf8("twVideo2"))
        self.twVideo2.setColumnCount(5)
        self.twVideo2.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.twVideo2.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.twVideo2.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.twVideo2.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.twVideo2.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.twVideo2.setHorizontalHeaderItem(4, item)
        self.verticalLayout_4.addWidget(self.twVideo2)
        self.layoutWidget6 = QtGui.QWidget(self.splitter_4)
        self.layoutWidget6.setObjectName(_fromUtf8("layoutWidget6"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.layoutWidget6)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.pbAddVideo_2 = QtGui.QPushButton(self.layoutWidget6)
        self.pbAddVideo_2.setObjectName(_fromUtf8("pbAddVideo_2"))
        self.horizontalLayout_4.addWidget(self.pbAddVideo_2)
        self.pbRemoveVideo_2 = QtGui.QPushButton(self.layoutWidget6)
        self.pbRemoveVideo_2.setObjectName(_fromUtf8("pbRemoveVideo_2"))
        self.horizontalLayout_4.addWidget(self.pbRemoveVideo_2)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.lbTimeOffset_2 = QtGui.QLabel(self.layoutWidget6)
        self.lbTimeOffset_2.setObjectName(_fromUtf8("lbTimeOffset_2"))
        self.horizontalLayout_7.addWidget(self.lbTimeOffset_2)
        self.rbEarlier = QtGui.QRadioButton(self.layoutWidget6)
        self.rbEarlier.setChecked(True)
        self.rbEarlier.setObjectName(_fromUtf8("rbEarlier"))
        self.horizontalLayout_7.addWidget(self.rbEarlier)
        self.rbLater = QtGui.QRadioButton(self.layoutWidget6)
        self.rbLater.setObjectName(_fromUtf8("rbLater"))
        self.horizontalLayout_7.addWidget(self.rbLater)
        self.leTimeOffset_2 = QtGui.QLineEdit(self.layoutWidget6)
        self.leTimeOffset_2.setObjectName(_fromUtf8("leTimeOffset_2"))
        self.horizontalLayout_7.addWidget(self.leTimeOffset_2)
        self.teTimeOffset_2 = QtGui.QTimeEdit(self.layoutWidget6)
        self.teTimeOffset_2.setObjectName(_fromUtf8("teTimeOffset_2"))
        self.horizontalLayout_7.addWidget(self.teTimeOffset_2)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem5)
        self.verticalLayout_7.addWidget(self.splitter_4)
        self.tabWidget.addTab(self.tab_player_2, _fromUtf8(""))
        self.tab_data_files = QtGui.QWidget()
        self.tab_data_files.setObjectName(_fromUtf8("tab_data_files"))
        self.verticalLayout_17 = QtGui.QVBoxLayout(self.tab_data_files)
        self.verticalLayout_17.setObjectName(_fromUtf8("verticalLayout_17"))
        self.splitter_5 = QtGui.QSplitter(self.tab_data_files)
        self.splitter_5.setOrientation(QtCore.Qt.Vertical)
        self.splitter_5.setObjectName(_fromUtf8("splitter_5"))
        self.layoutWidget7 = QtGui.QWidget(self.splitter_5)
        self.layoutWidget7.setObjectName(_fromUtf8("layoutWidget7"))
        self.verticalLayout_15 = QtGui.QVBoxLayout(self.layoutWidget7)
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.label_7 = QtGui.QLabel(self.layoutWidget7)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_15.addWidget(self.label_7)
        self.tw_data_files = QtGui.QTableWidget(self.layoutWidget7)
        self.tw_data_files.setObjectName(_fromUtf8("tw_data_files"))
        self.tw_data_files.setColumnCount(8)
        self.tw_data_files.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tw_data_files.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tw_data_files.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tw_data_files.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tw_data_files.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tw_data_files.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tw_data_files.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tw_data_files.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tw_data_files.setHorizontalHeaderItem(7, item)
        self.verticalLayout_15.addWidget(self.tw_data_files)
        self.layoutWidget8 = QtGui.QWidget(self.splitter_5)
        self.layoutWidget8.setObjectName(_fromUtf8("layoutWidget8"))
        self.verticalLayout_16 = QtGui.QVBoxLayout(self.layoutWidget8)
        self.verticalLayout_16.setObjectName(_fromUtf8("verticalLayout_16"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.pb_add_data_file = QtGui.QPushButton(self.layoutWidget8)
        self.pb_add_data_file.setObjectName(_fromUtf8("pb_add_data_file"))
        self.horizontalLayout_5.addWidget(self.pb_add_data_file)
        self.pb_view_data_head = QtGui.QPushButton(self.layoutWidget8)
        self.pb_view_data_head.setObjectName(_fromUtf8("pb_view_data_head"))
        self.horizontalLayout_5.addWidget(self.pb_view_data_head)
        self.pb_plot_data = QtGui.QPushButton(self.layoutWidget8)
        self.pb_plot_data.setObjectName(_fromUtf8("pb_plot_data"))
        self.horizontalLayout_5.addWidget(self.pb_plot_data)
        self.pb_remove_data_file = QtGui.QPushButton(self.layoutWidget8)
        self.pb_remove_data_file.setObjectName(_fromUtf8("pb_remove_data_file"))
        self.horizontalLayout_5.addWidget(self.pb_remove_data_file)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.verticalLayout_16.addLayout(self.horizontalLayout_5)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_16.addItem(spacerItem7)
        self.verticalLayout_17.addWidget(self.splitter_5)
        self.tabWidget.addTab(self.tab_data_files, _fromUtf8(""))
        self.verticalLayout_14.addWidget(self.tabWidget)
        self.tabProjectType.addTab(self.tabVideo, _fromUtf8(""))
        self.tabLive = QtGui.QWidget()
        self.tabLive.setObjectName(_fromUtf8("tabLive"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.tabLive)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_4 = QtGui.QLabel(self.tabLive)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_8.addWidget(self.label_4)
        self.sbScanSampling = QtGui.QSpinBox(self.tabLive)
        self.sbScanSampling.setMaximum(1000000)
        self.sbScanSampling.setObjectName(_fromUtf8("sbScanSampling"))
        self.horizontalLayout_8.addWidget(self.sbScanSampling)
        self.label_6 = QtGui.QLabel(self.tabLive)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_8.addWidget(self.label_6)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem8)
        self.verticalLayout_8.addLayout(self.horizontalLayout_8)
        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem9)
        self.verticalLayout_10.addLayout(self.verticalLayout_8)
        self.tabProjectType.addTab(self.tabLive, _fromUtf8(""))
        self.verticalLayout_9.addWidget(self.tabProjectType)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem10)
        self.pbCancel = QtGui.QPushButton(self.layoutWidget2)
        self.pbCancel.setObjectName(_fromUtf8("pbCancel"))
        self.horizontalLayout.addWidget(self.pbCancel)
        self.pbSave = QtGui.QPushButton(self.layoutWidget2)
        self.pbSave.setObjectName(_fromUtf8("pbSave"))
        self.horizontalLayout.addWidget(self.pbSave)
        self.pbLaunch = QtGui.QPushButton(self.layoutWidget2)
        self.pbLaunch.setObjectName(_fromUtf8("pbLaunch"))
        self.horizontalLayout.addWidget(self.pbLaunch)
        self.verticalLayout_9.addLayout(self.horizontalLayout)
        self.verticalLayout_12.addWidget(self.splitter_2)

        self.retranslateUi(Form)
        self.tabProjectType.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "New observation", None))
        self.label.setText(_translate("Form", "Observation id", None))
        self.label_8.setText(_translate("Form", "Date", None))
        self.dteDate.setDisplayFormat(_translate("Form", "yyyy-MM-dd hh:mm", None))
        self.label_9.setText(_translate("Form", "Description", None))
        self.lbTimeOffset.setText(_translate("Form", "Time offset", None))
        self.rbAdd.setText(_translate("Form", "Add", None))
        self.rbSubstract.setText(_translate("Form", "Substract", None))
        self.leTimeOffset.setText(_translate("Form", "0", None))
        self.teTimeOffset.setDisplayFormat(_translate("Form", "hh:mm:ss.zzz", None))
        self.label_3.setText(_translate("Form", "Independent variables", None))
        item = self.twIndepVariables.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Variable", None))
        item = self.twIndepVariables.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Type", None))
        item = self.twIndepVariables.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Value", None))
        self.label_5.setText(_translate("Form", "Media file paths (first player)", None))
        item = self.twVideo1.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Path", None))
        item = self.twVideo1.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Duration", None))
        item = self.twVideo1.horizontalHeaderItem(2)
        item.setText(_translate("Form", "FPS", None))
        item = self.twVideo1.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Video", None))
        item = self.twVideo1.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Audio", None))
        self.pbAddVideo.setText(_translate("Form", "Add media", None))
        self.pbRemoveVideo.setText(_translate("Form", "Remove media", None))
        self.pbAddMediaFromDir.setText(_translate("Form", "Add all media from directory", None))
        self.cbVisualizeSpectrogram.setText(_translate("Form", "Visualize spectrogram", None))
        self.cbCloseCurrentBehaviorsBetweenVideo.setText(_translate("Form", "Stop ongoing state events between successive media files", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_player_1), _translate("Form", "Player 1", None))
        self.label_2.setText(_translate("Form", "Media file paths for second player (will be played simultaneously)", None))
        item = self.twVideo2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Path", None))
        item = self.twVideo2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Duration", None))
        item = self.twVideo2.horizontalHeaderItem(2)
        item.setText(_translate("Form", "FPS", None))
        item = self.twVideo2.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Video", None))
        item = self.twVideo2.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Audio", None))
        self.pbAddVideo_2.setText(_translate("Form", "Add media", None))
        self.pbRemoveVideo_2.setText(_translate("Form", "Remove media", None))
        self.lbTimeOffset_2.setText(_translate("Form", "Time offset for second player", None))
        self.rbEarlier.setText(_translate("Form", "Earlier", None))
        self.rbLater.setText(_translate("Form", "Later", None))
        self.leTimeOffset_2.setText(_translate("Form", "0", None))
        self.teTimeOffset_2.setDisplayFormat(_translate("Form", "hh:mm:ss.zzz", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_player_2), _translate("Form", "Player 2", None))
        self.label_7.setText(_translate("Form", "Data files to plot", None))
        item = self.tw_data_files.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Path", None))
        item = self.tw_data_files.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Columns to plot", None))
        item = self.tw_data_files.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Plot title", None))
        item = self.tw_data_files.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Variable name", None))
        item = self.tw_data_files.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Time interval (s)", None))
        item = self.tw_data_files.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Start position (s)", None))
        item = self.tw_data_files.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Substract first value", None))
        item = self.tw_data_files.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Color", None))
        self.pb_add_data_file.setText(_translate("Form", "Add data file", None))
        self.pb_view_data_head.setText(_translate("Form", "View first rows", None))
        self.pb_plot_data.setText(_translate("Form", "Check data", None))
        self.pb_remove_data_file.setText(_translate("Form", "Remove data file", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_data_files), _translate("Form", "Data files", None))
        self.tabProjectType.setTabText(self.tabProjectType.indexOf(self.tabVideo), _translate("Form", "Media", None))
        self.label_4.setText(_translate("Form", "Scan sampling every", None))
        self.label_6.setText(_translate("Form", "seconds", None))
        self.tabProjectType.setTabText(self.tabProjectType.indexOf(self.tabLive), _translate("Form", "Live", None))
        self.pbCancel.setText(_translate("Form", "Cancel", None))
        self.pbSave.setText(_translate("Form", "Save", None))
        self.pbLaunch.setText(_translate("Form", "Start", None))

