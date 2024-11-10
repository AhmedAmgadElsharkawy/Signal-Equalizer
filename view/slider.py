from PyQt5.QtWidgets import (
    QWidget, QHBoxLayout, QLabel, QSlider
)

from PyQt5.QtCore import Qt, pyqtSignal


class Slider(QWidget):
    valueChanged = pyqtSignal(int)
    
    def __init__(self,min_range_value = 0,max_range_value = 100,name = "slider"):
        super().__init__()
        self.main_layout = QHBoxLayout(self)
        self.min_range_value = min_range_value
        self.max_range_value = max_range_value
        
        self.slider_name = QLabel(name)
        # self.slider_value = QLabel(f"{min_range_value}")
        self.slider_widget = QSlider(Qt.Orientation.Horizontal)
        self.slider_widget.setFixedWidth(200)
        
        # self.slider_widget.setRange(min_range_value,max_range_value)

        # for 10 ticks
        # tick_interval = (max_range_value-min_range_value)//9
        # self.slider_widget.setTickInterval(tick_interval)

        self.slider_widget.setTickPosition(QSlider.TickPosition.TicksBelow) 
        self.slider_widget.setRange(0,10)
        self.slider_widget.setTickInterval(1)

        
        
        self.main_layout.addWidget(self.slider_name)
        self.main_layout.addWidget(self.slider_widget)
        # self.main_layout.addWidget(self.slider_value)

        self.connect_value_changed()
        
    def emit_value_changed(self, value):
        # Emit the custom signal with the slider value
        self.valueChanged.emit(value)

    def connect_value_changed(self):
        # Disconnect the slider's valueChanged signal from emit_value_changed
        self.slider_widget.valueChanged.connect(self.emit_value_changed)

    def disconnect_value_changed(self):
        # Disconnect the slider's valueChanged signal from emit_value_changed
        self.slider_widget.valueChanged.disconnect(self.emit_value_changed)
        

        
