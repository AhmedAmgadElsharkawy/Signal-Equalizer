from PyQt5.QtWidgets import QWidget, QHBoxLayout,QPushButton
import pyqtgraph as pg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtCore import QSize,Qt



class CineSignalViewer(QWidget):
    def __init__(self, main_window, name):
        super().__init__()
        self.sound_played = False
        self.color_bar = None
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


        self.play_icon = QIcon("assets/icons/play-button.png") 
        self.pause_icon = QIcon("assets/icons/pause-button.png")

        self.toggle_sound_play_button = QPushButton(parent = self.cine_signal_plot)
        self.toggle_sound_play_button.setVisible(False)
        self.toggle_sound_play_button.setIcon(self.play_icon)
        self.toggle_sound_play_button.setGeometry(60,20,30,30)
        self.toggle_sound_play_button.setIconSize(QSize(30, 30))  # Set icon size to 32x32
        self.toggle_sound_play_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.toggle_sound_play_button.clicked.connect(self.toggle_sound_play)

        self.spectrogram_figure, self.spectogram_ax = plt.subplots()
        self.signal_spectrogram = FigureCanvas(self.spectrogram_figure)
        self.main_layout.addWidget(self.signal_spectrogram)

        self.spectrogram_figure.subplots_adjust(left=0.12, right=0.95, top=0.95, bottom=0.12)


        self.toggle_sound_play_button.setStyleSheet("""
            QPushButton {
                border: none;
                background-color: transparent;
            }
            QPushButton:hover {
                background-color: none; /* Optional: hover effect */
            }
        """)



    def toggle_sound_play(self,event):
        if self.sound_played:
            self.stop_plot_sound()
        else:
            self.play_plot_sound()


    def play_plot_sound(self):
        self.main_window.toggle_plots_played_sound(self.name)
        self.toggle_sound_play_button.setIcon(self.pause_icon)
        if self.name == "input":
            self.main_window.signal.save_and_play_wav(True, self.main_window.signal.data, self.main_window.signal.sample_rate)
        else:
            self.main_window.signal.save_and_play_wav(False, self.main_window.signal.sound_data, self.main_window.signal.sample_rate)
        self.sound_played = True
        
    def stop_plot_sound(self):
        self.toggle_sound_play_button.setIcon(self.play_icon)
        self.sound_played = False
        self.main_window.signal.stop_sound()

    def hide_toggle_sound_play_button(self):
        self.toggle_sound_play_button.setVisible(False)
        self.main_window.signal.stop_sound()

    def show_toggle_sound_play_button(self):
        self.toggle_sound_play_button.setVisible(True)
        self.main_window.signal.stop_sound()


    def clear_the_plot(self):
        self.cine_signal_plot.clear()
        if self.color_bar is not None:
            self.color_bar.remove()
        self.spectogram_ax.clear()
        self.color_bar = None
        self.signal_spectrogram.draw()

        

