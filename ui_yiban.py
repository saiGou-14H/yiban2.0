# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'yiban.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1205, 649)
        icon = QIcon()
        icon.addFile(u"x.ico", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout_6 = QVBoxLayout(Form)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setFixedSize(QSize(1178, 627))
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget_4 = QTabWidget(self.tab_2)
        self.tabWidget_4.setObjectName(u"tabWidget_4")
        self.tabWidget_4.setGeometry(QRect(30, 470, 601, 79))
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.horizontalLayout_3 = QHBoxLayout(self.tab_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit_3 = QLineEdit(self.tab_5)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_3.addWidget(self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(self.tab_5)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_3.addWidget(self.lineEdit_4)

        self.pushButton = QPushButton(self.tab_5)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.label = QLabel(self.tab_5)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.label_2 = QLabel(self.tab_5)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.tabWidget_4.addTab(self.tab_5, "")
        self.pushButton_run = QPushButton(self.tab_2)
        self.pushButton_run.setObjectName(u"pushButton_run")
        self.pushButton_run.setGeometry(QRect(650, 480, 491, 71))
        self.layoutWidget = QWidget(self.tab_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 30, 611, 401))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.layoutWidget)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 10):
            self.tableWidget.setRowCount(10)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(2)

        self.horizontalLayout.addWidget(self.tableWidget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget_2 = QTabWidget(self.layoutWidget)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_2 = QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.checkBox_qd = QCheckBox(self.tab_3)
        self.checkBox_qd.setObjectName(u"checkBox_qd")

        self.verticalLayout_2.addWidget(self.checkBox_qd)

        self.checkBox_dz = QCheckBox(self.tab_3)
        self.checkBox_dz.setObjectName(u"checkBox_dz")

        self.verticalLayout_2.addWidget(self.checkBox_dz)

        self.checkBox_mms = QCheckBox(self.tab_3)
        self.checkBox_mms.setObjectName(u"checkBox_mms")

        self.verticalLayout_2.addWidget(self.checkBox_mms)

        self.checkBox_mmp = QCheckBox(self.tab_3)
        self.checkBox_mmp.setObjectName(u"checkBox_mmp")

        self.verticalLayout_2.addWidget(self.checkBox_mmp)

        self.checkBox_ybyqd = QCheckBox(self.tab_3)
        self.checkBox_ybyqd.setObjectName(u"checkBox_ybyqd")

        self.verticalLayout_2.addWidget(self.checkBox_ybyqd)

        self.tabWidget_2.addTab(self.tab_3, "")

        self.verticalLayout.addWidget(self.tabWidget_2)

        self.tabWidget_3 = QTabWidget(self.layoutWidget)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_3 = QVBoxLayout(self.tab_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.checkBox_wsqp = QCheckBox(self.tab_4)
        self.checkBox_wsqp.setObjectName(u"checkBox_wsqp")

        self.verticalLayout_3.addWidget(self.checkBox_wsqp)

        self.checkBox_wsqs = QCheckBox(self.tab_4)
        self.checkBox_wsqs.setObjectName(u"checkBox_wsqs")

        self.verticalLayout_3.addWidget(self.checkBox_wsqs)

        self.tabWidget_3.addTab(self.tab_4, "")

        self.verticalLayout.addWidget(self.tabWidget_3)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(31, 570, 1111, 20))
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.layoutWidget1 = QWidget(self.tab_2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(650, 30, 491, 401))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.textBrowser = QTextBrowser(self.layoutWidget1)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_5.addWidget(self.textBrowser)

        self.pushButton_4 = QPushButton(self.layoutWidget1)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_5.addWidget(self.pushButton_4)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_4 = QHBoxLayout(self.tab)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)

        self.lineEdit_7 = QLineEdit(self.tab)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.verticalLayout_4.addWidget(self.lineEdit_7)

        self.pushButton_3 = QPushButton(self.tab)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_4.addWidget(self.pushButton_3)

        self.textBrowser_2 = QTextBrowser(self.tab)
        self.textBrowser_2.setObjectName(u"textBrowser_2")

        self.verticalLayout_4.addWidget(self.textBrowser_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        self.tabWidget.addTab(self.tab, "")

        self.verticalLayout_6.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"yiban2.0", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Form", u"\u8d26\u53f7", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Form", u"\u5bc6\u7801", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u767b\u5f55", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u4f59\u989d\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"0.0 ", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_5), QCoreApplication.translate("Form", u"\u6253\u7801\u5e73\u53f0", None))
        self.pushButton_run.setText(QCoreApplication.translate("Form", u"\u8fd0\u884c", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u8d26\u53f7", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u5bc6\u7801", None));
        self.checkBox_qd.setText(QCoreApplication.translate("Form", u"\u7b7e\u5230", None))
        self.checkBox_dz.setText(QCoreApplication.translate("Form", u"\u70b9\u8d5e", None))
        self.checkBox_mms.setText(QCoreApplication.translate("Form", u"\u6613\u55b5\u55b5\u53d1\u5e16", None))
        self.checkBox_mmp.setText(QCoreApplication.translate("Form", u"\u6613\u55b5\u55b5\u8bc4\u8bba", None))
        self.checkBox_ybyqd.setText(QCoreApplication.translate("Form", u"\u6613\u4f34\u4e91\u7b7e\u5230", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("Form", u"\u666e\u901a\u4efb\u52a1", None))
        self.checkBox_wsqp.setText(QCoreApplication.translate("Form", u"\u5fae\u793e\u533a\u8bc4\u8bba", None))
        self.checkBox_wsqs.setText(QCoreApplication.translate("Form", u"\u5fae\u793e\u533a\u53d1\u5e16", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_4), QCoreApplication.translate("Form", u"\u9a8c\u8bc1\u7801\u4efb\u52a1", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"--\u55ee\u72d7", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u6e05\u7a7a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u666e\u901a\u529f\u80fd", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"WCBOT\u81ea\u7528  \u6d88\u606f\u56de\u8c03\u7aef\u53e38005", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("Form", u"\u76d1\u542c\u7aef\u53e3 ", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u8fde\u63a5", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"\u63d2\u63a5\u8f6f", None))
    # retranslateUi


