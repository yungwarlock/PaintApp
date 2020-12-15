# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from app.Draw import PaintingApplication


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(739, 611)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.side_bar = QtWidgets.QWidget(self.centralwidget)
        self.side_bar.setMaximumSize(QtCore.QSize(190, 16777215))
        self.side_bar.setObjectName("side_bar")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.side_bar)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.side_bar)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_4.addWidget(self.groupBox)
        self.cap_style_groupBox = QtWidgets.QGroupBox(self.side_bar)
        self.cap_style_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.cap_style_groupBox.setObjectName("cap_style_groupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.cap_style_groupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.cap_style_groupBox)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout_3.addWidget(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(self.cap_style_groupBox)
        self.radioButton_5.setObjectName("radioButton_5")
        self.verticalLayout_3.addWidget(self.radioButton_5)
        self.radioButton_6 = QtWidgets.QRadioButton(self.cap_style_groupBox)
        self.radioButton_6.setObjectName("radioButton_6")
        self.verticalLayout_3.addWidget(self.radioButton_6)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addWidget(self.cap_style_groupBox)
        self.line_style_groupBox = QtWidgets.QGroupBox(self.side_bar)
        self.line_style_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.line_style_groupBox.setObjectName("line_style_groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.line_style_groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_4.addWidget(self.line_style_groupBox)
        self.join_style_groupBox = QtWidgets.QGroupBox(self.side_bar)
        self.join_style_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.join_style_groupBox.setObjectName("join_style_groupBox")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.join_style_groupBox)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.radioButton_7 = QtWidgets.QRadioButton(self.join_style_groupBox)
        self.radioButton_7.setObjectName("radioButton_7")
        self.verticalLayout_6.addWidget(self.radioButton_7)
        self.radioButton_9 = QtWidgets.QRadioButton(self.join_style_groupBox)
        self.radioButton_9.setObjectName("radioButton_9")
        self.verticalLayout_6.addWidget(self.radioButton_9)
        self.radioButton_8 = QtWidgets.QRadioButton(self.join_style_groupBox)
        self.radioButton_8.setObjectName("radioButton_8")
        self.verticalLayout_6.addWidget(self.radioButton_8)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.verticalLayout_4.addWidget(self.join_style_groupBox)
        self.pen_color_groupBox = QtWidgets.QGroupBox(self.side_bar)
        self.pen_color_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.pen_color_groupBox.setObjectName("pen_color_groupBox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.pen_color_groupBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.verticalLayout_4.addWidget(self.pen_color_groupBox)
        self.app_name = QtWidgets.QLabel(self.side_bar)
        self.app_name.setMaximumSize(QtCore.QSize(16777215, 40))
        self.app_name.setFrameShape(QtWidgets.QFrame.Box)
        self.app_name.setFrameShadow(QtWidgets.QFrame.Plain)
        self.app_name.setLineWidth(10)
        self.app_name.setObjectName("app_name")
        self.verticalLayout_4.addWidget(self.app_name)
        self.horizontalLayout_2.addWidget(self.side_bar)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.paint_layout = PaintingApplication(self.centralwidget)
        self.paint_layout.setObjectName("paint_layout")
        self.widget = QtWidgets.QWidget(self.paint_layout)
        self.widget.setGeometry(QtCore.QRect(50, 100, 120, 80))
        self.widget.setObjectName("widget")
        self.horizontalLayout.addWidget(self.paint_layout)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 739, 29))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.main_toolBar = QtWidgets.QToolBar(MainWindow)
        self.main_toolBar.setMovable(False)
        self.main_toolBar.setFloatable(False)
        self.main_toolBar.setObjectName("main_toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.main_toolBar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_new = QtWidgets.QAction(MainWindow)
        self.action_new.setObjectName("action_new")
        self.action_open = QtWidgets.QAction(MainWindow)
        self.action_open.setObjectName("action_open")
        self.action_save = QtWidgets.QAction(MainWindow)
        self.action_save.setObjectName("action_save")
        self.action_print = QtWidgets.QAction(MainWindow)
        self.action_print.setObjectName("action_print")
        self.action_zoom_In = QtWidgets.QAction(MainWindow)
        self.action_zoom_In.setObjectName("action_zoom_In")
        self.action_zoom_out = QtWidgets.QAction(MainWindow)
        self.action_zoom_out.setObjectName("action_zoom_out")
        self.action_full_screen = QtWidgets.QAction(MainWindow)
        self.action_full_screen.setObjectName("action_full_screen")
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.action_help = QtWidgets.QAction(MainWindow)
        self.action_help.setObjectName("action_help")
        self.toolbar_action_brush = QtWidgets.QAction(MainWindow)
        self.toolbar_action_brush.setObjectName("toolbar_action_brush")
        self.toolbar_action_text = QtWidgets.QAction(MainWindow)
        self.toolbar_action_text.setObjectName("toolbar_action_text")
        self.toolbar_action_new = QtWidgets.QAction(MainWindow)
        self.toolbar_action_new.setObjectName("toolbar_action_new")
        self.action_spray_paint = QtWidgets.QAction(MainWindow)
        self.action_spray_paint.setObjectName("action_spray_paint")
        self.toolbar_action_full_screen = QtWidgets.QAction(MainWindow)
        self.toolbar_action_full_screen.setObjectName("toolbar_action_full_screen")
        self.toolbar_action_undo = QtWidgets.QAction(MainWindow)
        self.toolbar_action_undo.setObjectName("toolbar_action_undo")
        self.toolbar_action_redo = QtWidgets.QAction(MainWindow)
        self.toolbar_action_redo.setObjectName("toolbar_action_redo")
        self.toolbar_action_clear = QtWidgets.QAction(MainWindow)
        self.toolbar_action_clear.setObjectName("toolbar_action_clear")
        self.menuFile.addAction(self.action_new)
        self.menuFile.addAction(self.action_open)
        self.menuFile.addAction(self.action_save)
        self.menuFile.addAction(self.action_print)
        self.menuView.addAction(self.action_zoom_In)
        self.menuView.addAction(self.action_zoom_out)
        self.menuView.addAction(self.action_full_screen)
        self.menuHelp.addAction(self.action_about)
        self.menuHelp.addAction(self.action_help)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.main_toolBar.addAction(self.toolbar_action_brush)
        self.main_toolBar.addAction(self.action_spray_paint)
        self.main_toolBar.addAction(self.toolbar_action_text)
        self.main_toolBar.addSeparator()
        self.main_toolBar.addAction(self.toolbar_action_new)
        self.main_toolBar.addAction(self.toolbar_action_clear)
        self.main_toolBar.addSeparator()
        self.main_toolBar.addAction(self.toolbar_action_full_screen)
        self.main_toolBar.addAction(self.toolbar_action_undo)
        self.main_toolBar.addAction(self.toolbar_action_redo)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Shapes"))
        self.cap_style_groupBox.setTitle(_translate("MainWindow", "Cap Style"))
        self.radioButton_4.setText(_translate("MainWindow", "Flat"))
        self.radioButton_5.setText(_translate("MainWindow", "Square"))
        self.radioButton_6.setText(_translate("MainWindow", "Round"))
        self.line_style_groupBox.setTitle(_translate("MainWindow", "Line Style"))
        self.join_style_groupBox.setTitle(_translate("MainWindow", "Join Style"))
        self.radioButton_7.setText(_translate("MainWindow", "Bevel"))
        self.radioButton_9.setText(_translate("MainWindow", "Miter"))
        self.radioButton_8.setText(_translate("MainWindow", "Round"))
        self.pen_color_groupBox.setTitle(_translate("MainWindow", "Pen color"))
        self.app_name.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">PyQt5 Paint v1.0</p></body></html>"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.main_toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_new.setText(_translate("MainWindow", "&New"))
        self.action_new.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.action_open.setText(_translate("MainWindow", "&Open"))
        self.action_open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_save.setText(_translate("MainWindow", "&Save"))
        self.action_save.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_print.setText(_translate("MainWindow", "&Print"))
        self.action_print.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.action_zoom_In.setText(_translate("MainWindow", "Zoom &In"))
        self.action_zoom_In.setShortcut(_translate("MainWindow", "Ctrl+="))
        self.action_zoom_out.setText(_translate("MainWindow", "Zoom o&ut"))
        self.action_zoom_out.setShortcut(_translate("MainWindow", "Ctrl+-"))
        self.action_full_screen.setText(_translate("MainWindow", "F&ull screen"))
        self.action_full_screen.setShortcut(_translate("MainWindow", "F11"))
        self.action_about.setText(_translate("MainWindow", "&About"))
        self.action_about.setShortcut(_translate("MainWindow", "Alt+A"))
        self.action_help.setText(_translate("MainWindow", "&Help"))
        self.toolbar_action_brush.setText(_translate("MainWindow", "Brush"))
        self.toolbar_action_text.setText(_translate("MainWindow", "Text"))
        self.toolbar_action_text.setToolTip(_translate("MainWindow", "Start editing with text"))
        self.toolbar_action_new.setText(_translate("MainWindow", "New"))
        self.action_spray_paint.setText(_translate("MainWindow", "Spray Paint"))
        self.toolbar_action_full_screen.setText(_translate("MainWindow", "full screen"))
        self.toolbar_action_undo.setText(_translate("MainWindow", "Undo"))
        self.toolbar_action_redo.setText(_translate("MainWindow", "Redo"))
        self.toolbar_action_clear.setText(_translate("MainWindow", "Clear"))