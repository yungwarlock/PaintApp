# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from widgets.Draw import PaintingApplication


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(737, 580)
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
        self.cap_style_groupBox = QtWidgets.QGroupBox(self.side_bar)
        self.cap_style_groupBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cap_style_groupBox.setToolTipDuration(4)
        self.cap_style_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.cap_style_groupBox.setObjectName("cap_style_groupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.cap_style_groupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.flat_cap_radio = QtWidgets.QRadioButton(self.cap_style_groupBox)
        self.flat_cap_radio.setObjectName("flat_cap_radio")
        self.verticalLayout_3.addWidget(self.flat_cap_radio)
        self.square_cap_radio = QtWidgets.QRadioButton(self.cap_style_groupBox)
        self.square_cap_radio.setObjectName("square_cap_radio")
        self.verticalLayout_3.addWidget(self.square_cap_radio)
        self.round_cap_radio = QtWidgets.QRadioButton(self.cap_style_groupBox)
        self.round_cap_radio.setObjectName("round_cap_radio")
        self.verticalLayout_3.addWidget(self.round_cap_radio)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addWidget(self.cap_style_groupBox)
        self.line_style_groupBox = QtWidgets.QGroupBox(self.side_bar)
        self.line_style_groupBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.line_style_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.line_style_groupBox.setObjectName("line_style_groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.line_style_groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.dotted_line_radio = QtWidgets.QRadioButton(self.line_style_groupBox)
        self.dotted_line_radio.setObjectName("dotted_line_radio")
        self.verticalLayout.addWidget(self.dotted_line_radio)
        self.solid_line_radio = QtWidgets.QRadioButton(self.line_style_groupBox)
        self.solid_line_radio.setObjectName("solid_line_radio")
        self.verticalLayout.addWidget(self.solid_line_radio)
        self.dashed_line_radio = QtWidgets.QRadioButton(self.line_style_groupBox)
        self.dashed_line_radio.setObjectName("dashed_line_radio")
        self.verticalLayout.addWidget(self.dashed_line_radio)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_4.addWidget(self.line_style_groupBox)
        self.join_style_groupBox = QtWidgets.QGroupBox(self.side_bar)
        self.join_style_groupBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.join_style_groupBox.setAcceptDrops(True)
        self.join_style_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.join_style_groupBox.setObjectName("join_style_groupBox")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.join_style_groupBox)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.bevel_join_radio = QtWidgets.QRadioButton(self.join_style_groupBox)
        self.bevel_join_radio.setObjectName("bevel_join_radio")
        self.verticalLayout_6.addWidget(self.bevel_join_radio)
        self.miter_join_radio = QtWidgets.QRadioButton(self.join_style_groupBox)
        self.miter_join_radio.setObjectName("miter_join_radio")
        self.verticalLayout_6.addWidget(self.miter_join_radio)
        self.round_join_radio = QtWidgets.QRadioButton(self.join_style_groupBox)
        self.round_join_radio.setObjectName("round_join_radio")
        self.verticalLayout_6.addWidget(self.round_join_radio)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.verticalLayout_4.addWidget(self.join_style_groupBox)
        self.horizontalLayout_2.addWidget(self.side_bar)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.paint_layout = PaintingApplication(self.centralwidget)
        self.paint_layout.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.paint_layout.setObjectName("paint_layout")
        self.widget = QtWidgets.QWidget(self.paint_layout)
        self.widget.setGeometry(QtCore.QRect(50, 100, 120, 80))
        self.widget.setObjectName("widget")
        self.horizontalLayout.addWidget(self.paint_layout)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 737, 29))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.main_toolBar = QtWidgets.QToolBar(MainWindow)
        self.main_toolBar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.main_toolBar.setMovable(False)
        self.main_toolBar.setFloatable(False)
        self.main_toolBar.setObjectName("main_toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.main_toolBar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_open = QtWidgets.QAction(MainWindow)
        self.action_open.setObjectName("action_open")
        self.action_save = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_save.setIcon(icon)
        self.action_save.setObjectName("action_save")
        self.action_saveAs = QtWidgets.QAction(MainWindow)
        self.action_saveAs.setIcon(icon)
        self.action_saveAs.setObjectName("action_saveAs")
        self.action_zoomIn = QtWidgets.QAction(MainWindow)
        self.action_zoomIn.setObjectName("action_zoomIn")
        self.action_zoomOut = QtWidgets.QAction(MainWindow)
        self.action_zoomOut.setObjectName("action_zoomOut")
        self.action_fullScreen = QtWidgets.QAction(MainWindow)
        self.action_fullScreen.setObjectName("action_fullScreen")
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.action_help = QtWidgets.QAction(MainWindow)
        self.action_help.setObjectName("action_help")
        self.action_brush = QtWidgets.QAction(MainWindow)
        self.action_brush.setObjectName("action_brush")
        self.action_new = QtWidgets.QAction(MainWindow)
        self.action_new.setObjectName("action_new")
        self.action_sprayPaint = QtWidgets.QAction(MainWindow)
        self.action_sprayPaint.setObjectName("action_sprayPaint")
        self.action_clear = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_clear.setIcon(icon1)
        self.action_clear.setObjectName("action_clear")
        self.action_eraser = QtWidgets.QAction(MainWindow)
        self.action_eraser.setObjectName("action_eraser")
        self.action_exit = QtWidgets.QAction(MainWindow)
        self.action_exit.setObjectName("action_exit")
        self.menuFile.addAction(self.action_new)
        self.menuFile.addAction(self.action_open)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_save)
        self.menuFile.addAction(self.action_saveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_clear)
        self.menuFile.addAction(self.action_exit)
        self.menuView.addAction(self.action_zoomIn)
        self.menuView.addAction(self.action_zoomOut)
        self.menuView.addAction(self.action_fullScreen)
        self.menuHelp.addAction(self.action_about)
        self.menuHelp.addAction(self.action_help)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.main_toolBar.addAction(self.action_brush)
        self.main_toolBar.addAction(self.action_sprayPaint)
        self.main_toolBar.addAction(self.action_eraser)
        self.main_toolBar.addSeparator()
        self.main_toolBar.addAction(self.action_new)
        self.main_toolBar.addAction(self.action_clear)
        self.main_toolBar.addSeparator()
        self.main_toolBar.addAction(self.action_fullScreen)
        self.main_toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cap_style_groupBox.setToolTip(_translate("MainWindow", "Hello World"))
        self.cap_style_groupBox.setStatusTip(_translate("MainWindow", "Change the cap at the end of a lines\'s curve"))
        self.cap_style_groupBox.setTitle(_translate("MainWindow", "Cap Style"))
        self.flat_cap_radio.setText(_translate("MainWindow", "Flat"))
        self.square_cap_radio.setText(_translate("MainWindow", "Square"))
        self.round_cap_radio.setText(_translate("MainWindow", "Round"))
        self.line_style_groupBox.setStatusTip(_translate("MainWindow", "Changes how the line gets painted on the canvas"))
        self.line_style_groupBox.setTitle(_translate("MainWindow", "Line Style"))
        self.dotted_line_radio.setText(_translate("MainWindow", "Dotted"))
        self.solid_line_radio.setText(_translate("MainWindow", "Solid"))
        self.dashed_line_radio.setText(_translate("MainWindow", "Dashed"))
        self.join_style_groupBox.setStatusTip(_translate("MainWindow", "Changes the way the bends to another direction"))
        self.join_style_groupBox.setTitle(_translate("MainWindow", "Join Style"))
        self.bevel_join_radio.setText(_translate("MainWindow", "Bevel"))
        self.miter_join_radio.setText(_translate("MainWindow", "Miter"))
        self.round_join_radio.setText(_translate("MainWindow", "Round"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.main_toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_open.setText(_translate("MainWindow", "&Open"))
        self.action_open.setToolTip(_translate("MainWindow", "Open an existing paint project"))
        self.action_open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_save.setText(_translate("MainWindow", "&Save"))
        self.action_save.setToolTip(_translate("MainWindow", "Save current project"))
        self.action_save.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_saveAs.setText(_translate("MainWindow", "Save as"))
        self.action_saveAs.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.action_zoomIn.setText(_translate("MainWindow", "Zoom &In"))
        self.action_zoomIn.setShortcut(_translate("MainWindow", "Ctrl+="))
        self.action_zoomOut.setText(_translate("MainWindow", "Zoom o&ut"))
        self.action_zoomOut.setShortcut(_translate("MainWindow", "Ctrl+-"))
        self.action_fullScreen.setText(_translate("MainWindow", "F&ull screen"))
        self.action_fullScreen.setStatusTip(_translate("MainWindow", "Immersive screen size for the application"))
        self.action_fullScreen.setShortcut(_translate("MainWindow", "F11"))
        self.action_about.setText(_translate("MainWindow", "&About"))
        self.action_about.setShortcut(_translate("MainWindow", "Alt+A"))
        self.action_help.setText(_translate("MainWindow", "&Help"))
        self.action_brush.setText(_translate("MainWindow", "Line paint"))
        self.action_brush.setStatusTip(_translate("MainWindow", "Changes to painter to line mode"))
        self.action_new.setText(_translate("MainWindow", "New"))
        self.action_sprayPaint.setText(_translate("MainWindow", "Spray paint"))
        self.action_clear.setText(_translate("MainWindow", "Clear"))
        self.action_eraser.setText(_translate("MainWindow", "Eraser"))
        self.action_eraser.setToolTip(_translate("MainWindow", "Eraser tool"))
        self.action_exit.setText(_translate("MainWindow", "&Exit"))
        self.action_exit.setToolTip(_translate("MainWindow", "Exit the application"))
import icons_rc
