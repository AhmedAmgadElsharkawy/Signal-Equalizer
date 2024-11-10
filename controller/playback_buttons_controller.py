from PyQt5.QtWidgets import QFileDialog
from view.slider import Slider
import numpy as np
from scipy.fft import fft
import pyqtgraph as pg
from scipy.io import wavfile
class PlaybackButtonsController:
    def __init__(self,main_window):
        self.main_widnow = main_window

    def loadSignal(self):
        file_path, _ = QFileDialog.getOpenFileName(self.main_widnow, "Open .wav file", "", "Audio Files (*.wav)")
        if file_path:
            self.plot_fourier_transform(file_path)
            self.set_all_sliders_to_one()            

    def plot_fourier_transform(self, file_path):
        # Read the .wav file
        sample_rate, data = wavfile.read(file_path)
        x = np.arange(0, len(data)) / sample_rate  # Create the time axis
        
        # Use only one channel if stereo
        if len(data.shape) > 1:
            data = data[:, 0]
        
        # Fourier Transform
        N = len(data)
        T = 1.0 / sample_rate
        yf = fft(data)
        xf = np.fft.fftfreq(N, T)[:N//2]
        magnitudes = 2.0 / N * np.abs(yf[:N // 2])
        
        # Plot the Fourier Transform
        self.main_widnow.frequency_domain_viewer.frequency_domain_plot.plot(xf, magnitudes, pen=pg.mkPen(color=(170, 0, 0)))
        self.main_widnow.input_cine_signal_viewer.cine_signal_plot.plot(x, data, pen=pg.mkPen(color=(170, 0, 0)))
        self.main_widnow.output_cine_signal_viewer.cine_signal_plot.plot(x, data, pen=pg.mkPen(color=(170, 0, 0)))

    def set_all_sliders_to_one(self):
        # Loop through all widgets in sliders_widget_layout
        for i in range(self.main_widnow.sliders_widget_layout.count()):
            widget = self.main_widnow.sliders_widget_layout.itemAt(i).widget()
            
            # Check if the widget is an instance of your custom Slider class
            if isinstance(widget, Slider):
                # Set the slider value to 1
                widget.slider_widget.setValue(1)

