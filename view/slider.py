from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QLabel, QSlider, QPushButton, QComboBox, QFrame, QGroupBox,QScrollArea,QCheckBox
)

from PyQt5.QtCore import Qt


class Slider(QWidget):
    def __init__(self,min_range_value = 0,max_range_value = 100,name = "slider"):
        super().__init__()
        self.main_layout = QHBoxLayout(self)
        
        self.slider_name = QLabel(name)
        self.slider_value = QLabel(f"{min_range_value}")
        self.slider_widget = QSlider(Qt.Orientation.Horizontal)
        self.slider_widget.setRange(min_range_value,max_range_value)

        # for 10 ticks
        tick_interval = (max_range_value-min_range_value)//9
        self.slider_widget.setTickInterval(tick_interval)
        self.slider_widget.setTickPosition(QSlider.TickPosition.TicksBelow) 
        
        
        self.main_layout.addWidget(self.slider_name)
        self.main_layout.addWidget(self.slider_widget)
        self.main_layout.addWidget(self.slider_value)
        
        

        
