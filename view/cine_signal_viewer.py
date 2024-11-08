from PyQt5.QtWidgets import QWidget, QHBoxLayout
import pyqtgraph as pg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap

class CineSignalViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.sound_played = False
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

        # Load the icon from the assets folder
        self.muted_pixmap = QPixmap('assets/icons/mute.png')
        self.unmuted_pixmap = QPixmap('assets/icons/unmute.png')

        # Create the icon item and add it to the scene
        self.muted_sound_icon_item = QGraphicsPixmapItem(self.muted_pixmap)
        self.muted_sound_icon_item.mousePressEvent = self.click_icon

        self.unmuted_sound_icon_item = QGraphicsPixmapItem(self.unmuted_pixmap)
        self.unmuted_sound_icon_item.mousePressEvent = self.click_icon
        
        # Scale the icon to 40x40 pixels
        self.muted_sound_icon_item.setScale(30 / self.muted_pixmap.width())
        self.unmuted_sound_icon_item.setScale(30 / self.unmuted_pixmap.width())
        
        # Add the icon item to the plot's scene
        self.cine_signal_plot.scene().addItem(self.muted_sound_icon_item)
        


        # Create the spectrogram figure
        self.spectrogram_figure, self.spectogram_ax = plt.subplots()
        self.signal_spectrogram = FigureCanvas(self.spectrogram_figure)
        self.main_layout.addWidget(self.signal_spectrogram)

        self.spectrogram_figure.subplots_adjust(left=0.07, right=0.95, top=0.95, bottom=0.1)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.reposition_icon()

    def reposition_icon(self):
        # Get the current size of the PlotWidget
        plot_width = self.cine_signal_plot.width()
        plot_height = self.cine_signal_plot.height()

        # Calculate icon position for bottom-right corner
        icon_width = 40
        icon_height = 40
        self.muted_sound_icon_item.setPos(plot_width - icon_width - 10, plot_height - icon_height - 15)  # Small offset for padding
        self.unmuted_sound_icon_item.setPos(plot_width - icon_width - 10, plot_height - icon_height - 15)  # Small offset for padding

    def click_icon(self,event):
        if self.sound_played:
            self.cine_signal_plot.scene().removeItem(self.unmuted_sound_icon_item)
            self.cine_signal_plot.scene().addItem(self.muted_sound_icon_item)
        else:
            self.cine_signal_plot.scene().removeItem(self.muted_sound_icon_item)
            self.cine_signal_plot.scene().addItem(self.unmuted_sound_icon_item)
        self.sound_played = not self.sound_played
