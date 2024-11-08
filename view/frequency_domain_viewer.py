import pyqtgraph as pg
from PyQt5.QtWidgets import (QWidget, QHBoxLayout)


class FrequencyDomainViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QHBoxLayout(self)
        self.frequency_domain_plot = pg.PlotWidget()
        self.frequency_domain_plot.setBackground("w")
        self.frequency_domain_plot.showGrid(x=True, y=True)
        self.frequency_domain_plot.getAxis('bottom').setPen(pg.mkPen('k'))  
        self.frequency_domain_plot.getAxis('left').setPen(pg.mkPen('k'))
        self.frequency_domain_plot.getAxis('bottom').setTextPen(pg.mkPen('k')) 
        self.frequency_domain_plot.getAxis('left').setTextPen(pg.mkPen('k'))  
        self.main_layout.addWidget(self.frequency_domain_plot)
    
    def plot_data(self, scale_type):
        self.frequency_domain_plot.clear()
        if scale_type == 'linear':
            self.frequency_domain_plot.setLabel('bottom', 'Frequency (Hz)', color='black')
        elif scale_type == 'audiogram':
            self.frequency_domain_plot.setLabel('bottom', 'Frequency (Audiogram Scale)', color='black')

    
