from PyQt5.QtWidgets import (
    QWidget,QVBoxLayout, QHBoxLayout, QLabel,QPushButton
)

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont
import pyqtgraph as pg



class WeinerFilterView(QWidget):
    def __init__(self):
        super().__init__()
        self.central_layout = QVBoxLayout(self)
        self.central_layout.setContentsMargins(0,0,0,0)
        self.main_widget = QWidget()
        self.main_widget_layout = QVBoxLayout(self.main_widget)
        self.main_widget_layout.setContentsMargins(0,0,0,0)
        self.central_layout.addWidget(self.main_widget)

        self.header_label = QLabel("Choose The Silent Segment")
        self.header_label.setAlignment(Qt.AlignCenter) 
        font = QFont()
        font.setPointSize(10)  # Set font size
        self.header_label.setFont(font)
        self.main_widget_layout.addWidget(self.header_label)
        self.weiner_filter_widget = pg.PlotWidget()
        # self.weiner_filter_widget.setTitle("Choose The Silent Segment")
        self.weiner_filter_widget.setFixedHeight(200)
        self.main_widget_layout.addWidget(self.weiner_filter_widget)
        self.weiner_filter_widget.setBackground("w")
        self.weiner_filter_widget.showGrid(x=True, y=True)
        self.weiner_filter_widget.getAxis('bottom').setPen(pg.mkPen('k'))  
        self.weiner_filter_widget.getAxis('left').setPen(pg.mkPen('k'))
        self.weiner_filter_widget.getAxis('bottom').setTextPen(pg.mkPen('k')) 
        self.weiner_filter_widget.getAxis('left').setTextPen(pg.mkPen('k'))  

        self.weiner_buttons_widget = QWidget()
        self.weiner_buttons_widget_layout = QHBoxLayout(self.weiner_buttons_widget)
        self.main_widget_layout.addStretch()
        self.main_widget_layout.addWidget(self.weiner_buttons_widget)
        
        self.apply_filter_button = QPushButton("Apply")
        self.reset_filter_button = QPushButton("Reset")
        self.weiner_buttons_widget_layout.addWidget(self.apply_filter_button)
        self.weiner_buttons_widget_layout.addWidget(self.reset_filter_button)

        self.apply_filter_button.setFixedHeight(30)
        self.reset_filter_button.setFixedHeight(30)