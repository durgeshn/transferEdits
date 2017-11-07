# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\user\durgesh.n\workspace\transferEdits\transferEdits\ui\EditsIEWin.ui'
#
# Created: Mon Nov 06 14:20:25 2017
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(375, 304)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.proj_cb = QtGui.QComboBox(self.centralwidget)
        self.proj_cb.setObjectName("proj_cb")
        self.horizontalLayout.addWidget(self.proj_cb)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.ep_cb = QtGui.QComboBox(self.centralwidget)
        self.ep_cb.setObjectName("ep_cb")
        self.horizontalLayout_2.addWidget(self.ep_cb)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.sh_cb = QtGui.QComboBox(self.centralwidget)
        self.sh_cb.setObjectName("sh_cb")
        self.horizontalLayout_3.addWidget(self.sh_cb)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.importEdits_pb = QtGui.QPushButton(self.centralwidget)
        self.importEdits_pb.setObjectName("importEdits_pb")
        self.horizontalLayout_4.addWidget(self.importEdits_pb)
        self.close_pb = QtGui.QPushButton(self.centralwidget)
        self.close_pb.setObjectName("close_pb")
        self.horizontalLayout_4.addWidget(self.close_pb)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.finaliz_pb = QtGui.QPushButton(self.centralwidget)
        self.finaliz_pb.setObjectName("finaliz_pb")
        self.gridLayout.addWidget(self.finaliz_pb, 4, 0, 1, 1)
        self.assetRefTree_wt = QtGui.QTreeWidget(self.centralwidget)
        self.assetRefTree_wt.setObjectName("assetRefTree_wt")
        self.assetRefTree_wt.headerItem().setText(0, "1")
        self.gridLayout.addWidget(self.assetRefTree_wt, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Apply Edits :                                                         PCGI", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Project :", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Episode :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Shot :", None, QtGui.QApplication.UnicodeUTF8))
        self.importEdits_pb.setText(QtGui.QApplication.translate("MainWindow", "Import Edits", None, QtGui.QApplication.UnicodeUTF8))
        self.close_pb.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.finaliz_pb.setText(QtGui.QApplication.translate("MainWindow", "Finalize", None, QtGui.QApplication.UnicodeUTF8))

