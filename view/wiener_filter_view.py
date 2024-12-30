from PyQt5.QtWidgets import (
    QWidget,QVBoxLayout, QHBoxLayout, QLabel,QPushButton
)

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont
import pyqtgraph as pg
from controller.wiener_filter_controller import WienerFilterController




class wienerFilterView(QWidget):
    def __init__(self,main_window):
        super().__init__()
        self.main_window = main_window
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
        self.wiener_plot_widget = pg.PlotWidget()
        # self.wiener_filter_widget.setTitle("Choose The Silent Segment")
        self.wiener_plot_widget.setFixedHeight(200)
        self.main_widget_layout.addWidget(self.wiener_plot_widget)
        self.wiener_plot_widget.setBackground("w")
        self.wiener_plot_widget.showGrid(x=True, y=True)
        self.wiener_plot_widget.getAxis('bottom').setPen(pg.mkPen('k'))  
        self.wiener_plot_widget.getAxis('left').setPen(pg.mkPen('k'))
        self.wiener_plot_widget.getAxis('bottom').setTextPen(pg.mkPen('k')) 
        self.wiener_plot_widget.getAxis('left').setTextPen(pg.mkPen('k'))  

        self.wiener_linear_region_item = pg.LinearRegionItem(movable=True)

        self.wiener_buttons_widget = QWidget()
        self.wiener_buttons_widget_layout = QHBoxLayout(self.wiener_buttons_widget)
        self.main_widget_layout.addStretch()
        self.main_widget_layout.addWidget(self.wiener_buttons_widget)
        
        self.apply_filter_button = QPushButton("Apply")
        self.reset_filter_button = QPushButton("Reset")
        self.wiener_buttons_widget_layout.addWidget(self.apply_filter_button)
        self.wiener_buttons_widget_layout.addWidget(self.reset_filter_button)

        self.apply_filter_button.setFixedHeight(30)
        self.reset_filter_button.setFixedHeight(30)



        self.wiener_filter_controller = WienerFilterController(self,self.main_window)


