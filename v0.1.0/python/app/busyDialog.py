#!python2
# -*- coding:utf-8 -*-
#coding=gbk

from sgtk.platform.pyqt import QtCore, QtGui, QtWidgets
import sgtk
logger = sgtk.platform.get_logger(__name__)

class BusyDialog(QtWidgets.QWidget):
    def __init__(self, parent, icon_path):
        super(BusyDialog, self).__init__(parent)
        # self.setWindowModality(QtCore.Qt.WindowModal)
        logger.info('Get Asset Information...')
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint| QtCore.Qt.Window)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        # self.setAttribute(QtCore.Qt.WA_NoSystemBackground)
        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setSpacing(15)

        self.vLayout = QtWidgets.QVBoxLayout()
        self.vLayout.setContentsMargins(0,0,0,0)
        self.vLayout.setSpacing(2)

        self.hLayoutA = QtWidgets.QHBoxLayout()
        self.hLayoutA.setContentsMargins(0,0,0,0)
        self.hLayoutA.setSpacing(50)

        self.hLayoutB = QtWidgets.QHBoxLayout()
        self.hLayoutB.setContentsMargins(0,0,0,0)
        self.hLayoutB.setAlignment(QtCore.Qt.AlignRight)


        self.label = QtWidgets.QLabel()
        self.info_label = QtWidgets.QLabel()

        self.progressbar = QtWidgets.QProgressBar()
        self.progressbar.setFixedSize(400, 2)
        self.progressbar.setTextVisible(False)
        self.progressbar.hide()
        
        self.hLayoutA.addWidget(self.label)
        self.hLayoutB.addWidget(self.progressbar)
        self.hLayoutA.addLayout(self.hLayoutB)
        self.vLayout.addLayout(self.hLayoutA)
        self.vLayout.addWidget(self.info_label)

        self.movie = QtGui.QMovie(icon_path)
        self.image = QtWidgets.QLabel()
        self.image.setEnabled(False)
        self.image.setFixedSize(30,30)
        
        self.image.setStyleSheet('background:transparent; border:none;')

        self.layout.addWidget(self.image)
        self.layout.addLayout(self.vLayout)
        
    @QtCore.Slot(unicode, unicode, float, bool)
    def set_info(self, label, info, value, typ):
        if typ: 
            self.progressbar.hide()
        else: 
            self.progressbar.show()
            self.progressbar.setValue(value)
        self.label.setText(label)
        self.info_label.setText(info)
    
    @QtCore.Slot(bool)
    def set_progress_direction(self, typ):
        if typ: self.progressbar.setInvertedAppearance(False)
        else: self.progressbar.setInvertedAppearance(True)

    def showEvent(self, event):
        self.image.setMovie(self.movie)
        self.movie.start()
    
    def hideEvent(self, event):
        self.image.clear()
        self.movie.stop()
    
    # def paintEvent(self, event):
    #     painter = QtGui.QPainter(self)
    #     painter.setRenderHint(QtGui.QPainter.Antialiasing)
    #     painter.setBrush(QtGui.QColor(30,30,30,150))
    #     pen = QtGui.QPen(QtGui.QColor(10,10,10,150), 3, QtCore.Qt.SolidLine)
    #     painter.setPen(pen)
    #     painter.drawRoundedRect(2, 2, self.width()-3, self.height()-3, 70, 70)



