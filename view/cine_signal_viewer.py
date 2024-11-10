from PyQt5.QtWidgets import QWidget, QHBoxLayout
import pyqtgraph as pg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap

class CineSignalViewer(QWidget):
    def __init__(self, main_window, name):
        super().__init__()
        self.sound_played = False
        self.name = name
        self.main_window = main_window
        self.main_layout = QHBoxLayout(self)

        # Create the plot widget
        self.cine_signal_plot = pg.PlotWidget()
        self.main_layout.addWidget(self.cine_signal_plot)
        self.cine_signal_plot.setBackground("w")
        self.cine_signal_plot.showGrid(x=True, y=True)
        self.cine_signal_plot.getAxis('bottom').setPen(pg.mkPen('k'))  
        self.cine_signal_plot.getAxis('left').setPen(pg.mkPen('k'))
        self.cine_signal_plot.getAxis('bottom').setTextPen(pg.mkPen('k')) 
        self.cine_signal_plot.getAxis('left').setTextPen(pg.mkPen('k'))  

        self.muted_pixmap = QPixmap('assets/icons/mute.png')
        self.unmuted_pixmap = QPixmap('assets/icons/unmute.png')

        self.muted_sound_icon_item = QGraphicsPixmapItem(self.muted_pixmap)
        self.muted_sound_icon_item.mousePressEvent = self.click_icon

        self.unmuted_sound_icon_item = QGraphicsPixmapItem(self.unmuted_pixmap)
        self.unmuted_sound_icon_item.mousePressEvent = self.click_icon
        
        self.muted_sound_icon_item.setScale(30 / self.muted_pixmap.width())
        self.unmuted_sound_icon_item.setScale(30 / self.unmuted_pixmap.width())
        
        self.cine_signal_plot.scene().addItem(self.muted_sound_icon_item)
        


        self.spectrogram_figure, self.spectogram_ax = plt.subplots()
        self.signal_spectrogram = FigureCanvas(self.spectrogram_figure)
        self.main_layout.addWidget(self.signal_spectrogram)

        self.spectrogram_figure.subplots_adjust(left=0.07, right=0.95, top=0.95, bottom=0.1)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.reposition_icon()

    def reposition_icon(self):
        plot_width = self.cine_signal_plot.width()
        plot_height = self.cine_signal_plot.height()

        icon_width = 40
        icon_height = 40
        # self.muted_sound_icon_item.setPos(plot_width - icon_width - 10, plot_height - icon_height - 15) 
        # self.unmuted_sound_icon_item.setPos(plot_width - icon_width - 10, plot_height - icon_height - 15) 

        
        self.muted_sound_icon_item.setPos(icon_width + 10,icon_height -25 ) 
        self.unmuted_sound_icon_item.setPos(icon_width + 10,icon_height -25 ) 

    def click_icon(self,event):
        if self.sound_played:
            self.cine_signal_plot.scene().removeItem(self.unmuted_sound_icon_item)
            self.cine_signal_plot.scene().addItem(self.muted_sound_icon_item)
            self.main_window.signal.stop_sound()
        else:
            self.cine_signal_plot.scene().removeItem(self.muted_sound_icon_item)
            self.cine_signal_plot.scene().addItem(self.unmuted_sound_icon_item)
            if self.name == "input":
                self.main_window.signal.save_and_play_wav(True, self.main_window.signal.data, self.main_window.signal.sample_rate)
            else:
                self.main_window.signal.save_and_play_wav(False, self.main_window.signal.sound_data, self.main_window.signal.sample_rate)
        self.sound_played = not self.sound_played
