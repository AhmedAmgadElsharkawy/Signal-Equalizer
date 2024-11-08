from PyQt5.QtWidgets import (QWidget, QHBoxLayout)
import pyqtgraph as pg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class CineSignalViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QHBoxLayout(self)

        self.cine_signal_plot = pg.PlotWidget()
        self.main_layout.addWidget(self.cine_signal_plot)
        self.cine_signal_plot.setBackground("w")
        self.cine_signal_plot.showGrid(x=True, y=True)
        self.cine_signal_plot.getAxis('bottom').setPen(pg.mkPen('k'))  
        self.cine_signal_plot.getAxis('left').setPen(pg.mkPen('k'))
        self.cine_signal_plot.getAxis('bottom').setTextPen(pg.mkPen('k')) 
        self.cine_signal_plot.getAxis('left').setTextPen(pg.mkPen('k'))  

        self.spectrogram_figure, self.spectogram_ax = plt.subplots()
        self.signal_spectrogram = FigureCanvas(self.spectrogram_figure)
        self.main_layout.addWidget(self.signal_spectrogram)

        self.spectrogram_figure.subplots_adjust(left=0.07, right=0.95, top=0.95, bottom=0.1)


        

        
        

        
