# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'observation.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1032, 812)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.leObservationId = QtWidgets.QLineEdit(Form)
        self.leObservationId.setObjectName("leObservationId")
        self.horizontalLayout_2.addWidget(self.leObservationId)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.dteDate = QtWidgets.QDateTimeEdit(Form)
        self.dteDate.setCalendarPopup(True)
        self.dteDate.setObjectName("dteDate")
        self.horizontalLayout_2.addWidget(self.dteDate)
        self.verticalLayout_12.addLayout(self.horizontalLayout_2)
        self.splitter_2 = QtWidgets.QSplitter(Form)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.teDescription = QtWidgets.QTextEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.teDescription.sizePolicy().hasHeightForWidth())
        self.teDescription.setSizePolicy(sizePolicy)
        self.teDescription.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.teDescription.setAcceptDrops(False)
        self.teDescription.setObjectName("teDescription")
        self.verticalLayout_2.addWidget(self.teDescription)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lbTimeOffset = QtWidgets.QLabel(self.layoutWidget)
        self.lbTimeOffset.setObjectName("lbTimeOffset")
        self.horizontalLayout_6.addWidget(self.lbTimeOffset)
        self.rbAdd = QtWidgets.QRadioButton(self.layoutWidget)
        self.rbAdd.setChecked(True)
        self.rbAdd.setObjectName("rbAdd")
        self.horizontalLayout_6.addWidget(self.rbAdd)
        self.rbSubstract = QtWidgets.QRadioButton(self.layoutWidget)
        self.rbSubstract.setObjectName("rbSubstract")
        self.horizontalLayout_6.addWidget(self.rbSubstract)
        self.leTimeOffset = QtWidgets.QLineEdit(self.layoutWidget)
        self.leTimeOffset.setObjectName("leTimeOffset")
        self.horizontalLayout_6.addWidget(self.leTimeOffset)
        self.teTimeOffset = QtWidgets.QTimeEdit(self.layoutWidget)
        self.teTimeOffset.setObjectName("teTimeOffset")
        self.horizontalLayout_6.addWidget(self.teTimeOffset)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_11.addWidget(self.label_3)
        self.twIndepVariables = QtWidgets.QTableWidget(self.layoutWidget1)
        self.twIndepVariables.setObjectName("twIndepVariables")
        self.twIndepVariables.setColumnCount(3)
        self.twIndepVariables.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.twIndepVariables.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.twIndepVariables.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.twIndepVariables.setHorizontalHeaderItem(2, item)
        self.verticalLayout_11.addWidget(self.twIndepVariables)
        self.layoutWidget2 = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.tabProjectType = QtWidgets.QTabWidget(self.layoutWidget2)
        self.tabProjectType.setEnabled(True)
        self.tabProjectType.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabProjectType.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabProjectType.setUsesScrollButtons(False)
        self.tabProjectType.setDocumentMode(False)
        self.tabProjectType.setTabsClosable(False)
        self.tabProjectType.setMovable(False)
        self.tabProjectType.setObjectName("tabProjectType")
        self.tabVideo = QtWidgets.QWidget()
        self.tabVideo.setObjectName("tabVideo")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.tabVideo)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.tabWidget = QtWidgets.QTabWidget(self.tabVideo)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_player_1 = QtWidgets.QWidget()
        self.tab_player_1.setObjectName("tab_player_1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_player_1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.splitter_3 = QtWidgets.QSplitter(self.tab_player_1)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.layoutWidget3 = QtWidgets.QWidget(self.splitter_3)
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.twVideo1 = QtWidgets.QTableWidget(self.layoutWidget3)
        self.twVideo1.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.twVideo1.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.twVideo1.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.twVideo1.setObjectName("twVideo1")
        self.twVideo1.setColumnCount(5)
        self.twVideo1.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.twVideo1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.twVideo1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.twVideo1.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.twVideo1.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.twVideo1.setHorizontalHeaderItem(4, item)
        self.verticalLayout_3.addWidget(self.twVideo1)
        self.layoutWidget4 = QtWidgets.QWidget(self.splitter_3)
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pbAddVideo = QtWidgets.QPushButton(self.layoutWidget4)
        self.pbAddVideo.setObjectName("pbAddVideo")
        self.horizontalLayout_3.addWidget(self.pbAddVideo)
        self.pbRemoveVideo = QtWidgets.QPushButton(self.layoutWidget4)
        self.pbRemoveVideo.setObjectName("pbRemoveVideo")
        self.horizontalLayout_3.addWidget(self.pbRemoveVideo)
        self.pbAddMediaFromDir = QtWidgets.QPushButton(self.layoutWidget4)
        self.pbAddMediaFromDir.setObjectName("pbAddMediaFromDir")
        self.horizontalLayout_3.addWidget(self.pbAddMediaFromDir)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.cbVisualizeSpectrogram = QtWidgets.QCheckBox(self.layoutWidget4)
        self.cbVisualizeSpectrogram.setObjectName("cbVisualizeSpectrogram")
        self.verticalLayout.addWidget(self.cbVisualizeSpectrogram)
        self.cbCloseCurrentBehaviorsBetweenVideo = QtWidgets.QCheckBox(self.layoutWidget4)
        self.cbCloseCurrentBehaviorsBetweenVideo.setObjectName("cbCloseCurrentBehaviorsBetweenVideo")
        self.verticalLayout.addWidget(self.cbCloseCurrentBehaviorsBetweenVideo)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout.addItem(spacerItem2)
        self.verticalLayout_5.addWidget(self.splitter_3)
        self.tabWidget.addTab(self.tab_player_1, "")
        self.tab_player_2 = QtWidgets.QWidget()
        self.tab_player_2.setObjectName("tab_player_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_player_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.splitter_4 = QtWidgets.QSplitter(self.tab_player_2)
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.layoutWidget5 = QtWidgets.QWidget(self.splitter_4)
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget5)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.twVideo2 = QtWidgets.QTableWidget(self.layoutWidget5)
        self.twVideo2.setObjectName("twVideo2")
        self.twVideo2.setColumnCount(5)
        self.twVideo2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.twVideo2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.twVideo2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.twVideo2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.twVideo2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.twVideo2.setHorizontalHeaderItem(4, item)
        self.verticalLayout_4.addWidget(self.twVideo2)
        self.layoutWidget6 = QtWidgets.QWidget(self.splitter_4)
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pbAddVideo_2 = QtWidgets.QPushButton(self.layoutWidget6)
        self.pbAddVideo_2.setObjectName("pbAddVideo_2")
        self.horizontalLayout_4.addWidget(self.pbAddVideo_2)
        self.pbRemoveVideo_2 = QtWidgets.QPushButton(self.layoutWidget6)
        self.pbRemoveVideo_2.setObjectName("pbRemoveVideo_2")
        self.horizontalLayout_4.addWidget(self.pbRemoveVideo_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lbTimeOffset_2 = QtWidgets.QLabel(self.layoutWidget6)
        self.lbTimeOffset_2.setObjectName("lbTimeOffset_2")
        self.horizontalLayout_7.addWidget(self.lbTimeOffset_2)
        self.rbEarlier = QtWidgets.QRadioButton(self.layoutWidget6)
        self.rbEarlier.setChecked(True)
        self.rbEarlier.setObjectName("rbEarlier")
        self.horizontalLayout_7.addWidget(self.rbEarlier)
        self.rbLater = QtWidgets.QRadioButton(self.layoutWidget6)
        self.rbLater.setObjectName("rbLater")
        self.horizontalLayout_7.addWidget(self.rbLater)
        self.leTimeOffset_2 = QtWidgets.QLineEdit(self.layoutWidget6)
        self.leTimeOffset_2.setObjectName("leTimeOffset_2")
        self.horizontalLayout_7.addWidget(self.leTimeOffset_2)
        self.teTimeOffset_2 = QtWidgets.QTimeEdit(self.layoutWidget6)
        self.teTimeOffset_2.setObjectName("teTimeOffset_2")
        self.horizontalLayout_7.addWidget(self.teTimeOffset_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem5)
        self.verticalLayout_7.addWidget(self.splitter_4)
        self.tabWidget.addTab(self.tab_player_2, "")
        self.tab_data_files = QtWidgets.QWidget()
        self.tab_data_files.setObjectName("tab_data_files")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.tab_data_files)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.splitter_5 = QtWidgets.QSplitter(self.tab_data_files)
        self.splitter_5.setOrientation(QtCore.Qt.Vertical)
        self.splitter_5.setObjectName("splitter_5")
        self.layoutWidget7 = QtWidgets.QWidget(self.splitter_5)
        self.layoutWidget7.setObjectName("layoutWidget7")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.layoutWidget7)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget7)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_15.addWidget(self.label_7)
        self.tw_data_files = QtWidgets.QTableWidget(self.layoutWidget7)
        self.tw_data_files.setObjectName("tw_data_files")
        self.tw_data_files.setColumnCount(9)
        self.tw_data_files.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tw_data_files.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_data_files.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_data_files.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_data_files.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_data_files.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_data_files.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_data_files.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_data_files.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_data_files.setHorizontalHeaderItem(8, item)
        self.verticalLayout_15.addWidget(self.tw_data_files)
        self.layoutWidget8 = QtWidgets.QWidget(self.splitter_5)
        self.layoutWidget8.setObjectName("layoutWidget8")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.layoutWidget8)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pb_add_data_file = QtWidgets.QPushButton(self.layoutWidget8)
        self.pb_add_data_file.setObjectName("pb_add_data_file")
        self.horizontalLayout_5.addWidget(self.pb_add_data_file)
        self.pb_view_data_head = QtWidgets.QPushButton(self.layoutWidget8)
        self.pb_view_data_head.setObjectName("pb_view_data_head")
        self.horizontalLayout_5.addWidget(self.pb_view_data_head)
        self.pb_plot_data = QtWidgets.QPushButton(self.layoutWidget8)
        self.pb_plot_data.setObjectName("pb_plot_data")
        self.horizontalLayout_5.addWidget(self.pb_plot_data)
        self.pb_remove_data_file = QtWidgets.QPushButton(self.layoutWidget8)
        self.pb_remove_data_file.setObjectName("pb_remove_data_file")
        self.horizontalLayout_5.addWidget(self.pb_remove_data_file)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.verticalLayout_16.addLayout(self.horizontalLayout_5)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_16.addItem(spacerItem7)
        self.verticalLayout_17.addWidget(self.splitter_5)
        self.tabWidget.addTab(self.tab_data_files, "")
        self.verticalLayout_14.addWidget(self.tabWidget)
        self.tabProjectType.addTab(self.tabVideo, "")
        self.tabLive = QtWidgets.QWidget()
        self.tabLive.setObjectName("tabLive")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tabLive)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_4 = QtWidgets.QLabel(self.tabLive)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        self.sbScanSampling = QtWidgets.QSpinBox(self.tabLive)
        self.sbScanSampling.setMaximum(1000000)
        self.sbScanSampling.setObjectName("sbScanSampling")
        self.horizontalLayout_8.addWidget(self.sbScanSampling)
        self.label_6 = QtWidgets.QLabel(self.tabLive)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem8)
        self.verticalLayout_8.addLayout(self.horizontalLayout_8)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem9)
        self.verticalLayout_10.addLayout(self.verticalLayout_8)
        self.tabProjectType.addTab(self.tabLive, "")
        self.verticalLayout_9.addWidget(self.tabProjectType)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem10)
        self.pbCancel = QtWidgets.QPushButton(self.layoutWidget2)
        self.pbCancel.setObjectName("pbCancel")
        self.horizontalLayout.addWidget(self.pbCancel)
        self.pbSave = QtWidgets.QPushButton(self.layoutWidget2)
        self.pbSave.setObjectName("pbSave")
        self.horizontalLayout.addWidget(self.pbSave)
        self.pbLaunch = QtWidgets.QPushButton(self.layoutWidget2)
        self.pbLaunch.setObjectName("pbLaunch")
        self.horizontalLayout.addWidget(self.pbLaunch)
        self.verticalLayout_9.addLayout(self.horizontalLayout)
        self.verticalLayout_12.addWidget(self.splitter_2)

        self.retranslateUi(Form)
        self.tabProjectType.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "New observation"))
        self.label.setText(_translate("Form", "Observation id"))
        self.label_8.setText(_translate("Form", "Date"))
        self.dteDate.setDisplayFormat(_translate("Form", "yyyy-MM-dd hh:mm"))
        self.label_9.setText(_translate("Form", "Description"))
        self.lbTimeOffset.setText(_translate("Form", "Time offset"))
        self.rbAdd.setText(_translate("Form", "Add"))
        self.rbSubstract.setText(_translate("Form", "Substract"))
        self.leTimeOffset.setText(_translate("Form", "0"))
        self.teTimeOffset.setDisplayFormat(_translate("Form", "hh:mm:ss.zzz"))
        self.label_3.setText(_translate("Form", "Independent variables"))
        item = self.twIndepVariables.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Variable"))
        item = self.twIndepVariables.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Type"))
        item = self.twIndepVariables.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Value"))
        self.label_5.setText(_translate("Form", "Media file paths (first player)"))
        item = self.twVideo1.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Path"))
        item = self.twVideo1.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Duration"))
        item = self.twVideo1.horizontalHeaderItem(2)
        item.setText(_translate("Form", "FPS"))
        item = self.twVideo1.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Video"))
        item = self.twVideo1.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Audio"))
        self.pbAddVideo.setText(_translate("Form", "Add media"))
        self.pbRemoveVideo.setText(_translate("Form", "Remove media"))
        self.pbAddMediaFromDir.setText(_translate("Form", "Add all media from directory"))
        self.cbVisualizeSpectrogram.setText(_translate("Form", "Visualize spectrogram"))
        self.cbCloseCurrentBehaviorsBetweenVideo.setText(_translate("Form", "Stop ongoing state events between successive media files"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_player_1), _translate("Form", "Player 1"))
        self.label_2.setText(_translate("Form", "Media file paths for second player (will be played simultaneously)"))
        item = self.twVideo2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Path"))
        item = self.twVideo2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Duration"))
        item = self.twVideo2.horizontalHeaderItem(2)
        item.setText(_translate("Form", "FPS"))
        item = self.twVideo2.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Video"))
        item = self.twVideo2.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Audio"))
        self.pbAddVideo_2.setText(_translate("Form", "Add media"))
        self.pbRemoveVideo_2.setText(_translate("Form", "Remove media"))
        self.lbTimeOffset_2.setText(_translate("Form", "Time offset for second player"))
        self.rbEarlier.setText(_translate("Form", "Earlier"))
        self.rbLater.setText(_translate("Form", "Later"))
        self.leTimeOffset_2.setText(_translate("Form", "0"))
        self.teTimeOffset_2.setDisplayFormat(_translate("Form", "hh:mm:ss.zzz"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_player_2), _translate("Form", "Player 2"))
        self.label_7.setText(_translate("Form", "Data files to plot"))
        item = self.tw_data_files.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Path"))
        item = self.tw_data_files.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Columns to plot"))
        item = self.tw_data_files.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Plot title"))
        item = self.tw_data_files.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Variable name"))
        item = self.tw_data_files.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Converters"))
        item = self.tw_data_files.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Time interval (s)"))
        item = self.tw_data_files.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Start position (s)"))
        item = self.tw_data_files.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Substract first value"))
        item = self.tw_data_files.horizontalHeaderItem(8)
        item.setText(_translate("Form", "Color"))
        self.pb_add_data_file.setText(_translate("Form", "Add data file"))
        self.pb_view_data_head.setText(_translate("Form", "View first rows"))
        self.pb_plot_data.setText(_translate("Form", "Show plot"))
        self.pb_remove_data_file.setText(_translate("Form", "Remove data file"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_data_files), _translate("Form", "Data files"))
        self.tabProjectType.setTabText(self.tabProjectType.indexOf(self.tabVideo), _translate("Form", "Media"))
        self.label_4.setText(_translate("Form", "Scan sampling every"))
        self.label_6.setText(_translate("Form", "seconds"))
        self.tabProjectType.setTabText(self.tabProjectType.indexOf(self.tabLive), _translate("Form", "Live"))
        self.pbCancel.setText(_translate("Form", "Cancel"))
        self.pbSave.setText(_translate("Form", "Save"))
        self.pbLaunch.setText(_translate("Form", "Start"))

