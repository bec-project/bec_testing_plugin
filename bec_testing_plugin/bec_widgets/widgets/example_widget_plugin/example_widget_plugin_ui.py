# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'example_widget_plugin.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from qtpy.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from qtpy.QtWidgets import (QApplication, QHBoxLayout, QSizePolicy, QSplitter,
    QTabWidget, QVBoxLayout, QWidget)

from bec_widgets.widgets.services.bec_queue.bec_queue import BECQueue
from bec_widgets.widgets.utility.logpanel.logpanel import LogPanel
from bec_widgets.widgets.control.buttons.button_resume.button_resume import ResumeButton
from bec_widgets.widgets.control.scan_control.scan_control import ScanControl
from bec_widgets.widgets.utility.signal_label.signal_label import SignalLabel
from bec_widgets.widgets.control.buttons.stop_button.stop_button import StopButton
from bec_widgets.widgets.editors.text_box.text_box import TextBox
from bec_widgets.widgets.plots.waveform.waveform import Waveform

class Ui_exampleWidgetPlugin(object):
    def setupUi(self, exampleWidgetPlugin):
        if not exampleWidgetPlugin.objectName():
            exampleWidgetPlugin.setObjectName(u"exampleWidgetPlugin")
        exampleWidgetPlugin.resize(1851, 1169)
        self.verticalLayout = QVBoxLayout(exampleWidgetPlugin)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter = QSplitter(exampleWidgetPlugin)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.signal_label_3 = SignalLabel(self.widget_3)
        self.signal_label_3.setObjectName(u"signal_label_3")

        self.horizontalLayout_3.addWidget(self.signal_label_3)

        self.signal_label = SignalLabel(self.widget_3)
        self.signal_label.setObjectName(u"signal_label")

        self.horizontalLayout_3.addWidget(self.signal_label)

        self.signal_label_2 = SignalLabel(self.widget_3)
        self.signal_label_2.setObjectName(u"signal_label_2")
        self.signal_label_2.setMaximumSize(QSize(16777215, 65))

        self.horizontalLayout_3.addWidget(self.signal_label_2)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.widget_6 = QWidget(self.widget)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.horizontalLayout_7 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.stop_button = StopButton(self.widget_6)
        self.stop_button.setObjectName(u"stop_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stop_button.sizePolicy().hasHeightForWidth())
        self.stop_button.setSizePolicy(sizePolicy1)

        self.horizontalLayout_7.addWidget(self.stop_button)

        self.resume_button = ResumeButton(self.widget_6)
        self.resume_button.setObjectName(u"resume_button")
        sizePolicy1.setHeightForWidth(self.resume_button.sizePolicy().hasHeightForWidth())
        self.resume_button.setSizePolicy(sizePolicy1)

        self.horizontalLayout_7.addWidget(self.resume_button)


        self.verticalLayout_2.addWidget(self.widget_6)

        self.splitter_2 = QSplitter(self.widget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Orientation.Horizontal)
        self.tabWidget = QTabWidget(self.splitter_2)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy2)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_3 = QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.bec_queue = BECQueue(self.tab)
        self.bec_queue.setObjectName(u"bec_queue")

        self.verticalLayout_3.addWidget(self.bec_queue)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_4 = QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.scan_control = ScanControl(self.tab_2)
        self.scan_control.setObjectName(u"scan_control")

        self.verticalLayout_4.addWidget(self.scan_control)

        self.tabWidget.addTab(self.tab_2, "")
        self.splitter_2.addWidget(self.tabWidget)
        self.waveform = Waveform(self.splitter_2)
        self.waveform.setObjectName(u"waveform")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.waveform.sizePolicy().hasHeightForWidth())
        self.waveform.setSizePolicy(sizePolicy3)
        self.splitter_2.addWidget(self.waveform)

        self.verticalLayout_2.addWidget(self.splitter_2)

        self.splitter.addWidget(self.widget)
        self.log_panel = LogPanel(self.splitter)
        self.log_panel.setObjectName(u"log_panel")
        sizePolicy1.setHeightForWidth(self.log_panel.sizePolicy().hasHeightForWidth())
        self.log_panel.setSizePolicy(sizePolicy1)
        self.log_panel.setMaximumSize(QSize(16777215, 902))
        self.splitter.addWidget(self.log_panel)

        self.verticalLayout.addWidget(self.splitter)


        self.retranslateUi(exampleWidgetPlugin)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(exampleWidgetPlugin)
    # setupUi

    def retranslateUi(self, exampleWidgetPlugin):
        self.signal_label_3.setProperty(u"device", QCoreApplication.translate("exampleWidgetPlugin", u"bpm3i", None))
        self.signal_label_3.setProperty(u"signal", QCoreApplication.translate("exampleWidgetPlugin", u"bpm3i", None))
        self.signal_label.setProperty(u"device", QCoreApplication.translate("exampleWidgetPlugin", u"bpm4i", None))
        self.signal_label.setProperty(u"signal", QCoreApplication.translate("exampleWidgetPlugin", u"bpm4i", None))
        self.signal_label_2.setProperty(u"device", QCoreApplication.translate("exampleWidgetPlugin", u"samy", None))
        self.signal_label_2.setProperty(u"signal", QCoreApplication.translate("exampleWidgetPlugin", u"readback", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("exampleWidgetPlugin", u"Queue", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("exampleWidgetPlugin", u"Scan Control", None))
        pass
    # retranslateUi

