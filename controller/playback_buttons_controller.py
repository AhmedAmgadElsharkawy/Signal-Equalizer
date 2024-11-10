from PyQt5.QtWidgets import QFileDialog
from view.slider import Slider
import numpy as np
import pyqtgraph as pg
from scipy.io import wavfile
import sounddevice as sd
class PlaybackButtonsController:
    def __init__(self,main_window):
        self.main_widnow = main_window

    def loadSignal(self):
        file_path, _ = QFileDialog.getOpenFileName(self.main_widnow, "Open .wav file", "", "Audio Files (*.wav)")
        if file_path:
            self.main_widnow.file_path = file_path
            self.main_widnow.signal.calculate_data(file_path)
            self.plot_the_signal()
            self.set_all_sliders_to_one()

    def plot_the_signal(self):
        self.main_widnow.frequency_domain_viewer.frequency_domain_plot.clear()
        self.main_widnow.input_cine_signal_viewer.cine_signal_plot.clear()
        self.main_widnow.output_cine_signal_viewer.cine_signal_plot.clear()

        self.main_widnow.input_cine_signal_viewer.cine_signal_plot.plot(self.main_widnow.signal.time, self.main_widnow.signal.data, pen=pg.mkPen(color=(170, 0, 0)))
        self.main_widnow.output_cine_signal_viewer.cine_signal_plot.plot(self.main_widnow.signal.time, self.main_widnow.signal.modified_data, pen=pg.mkPen(color=(170, 0, 0)))
        self.main_widnow.frequency_domain_viewer.frequency_domain_plot.plot(self.main_widnow.signal.freqs, self.main_widnow.signal.magnitudes, pen=pg.mkPen(color=(170, 0, 0)))

    def set_all_sliders_to_one(self):
        # Loop through all widgets in sliders_widget_layout
        for i in range(self.main_widnow.sliders_widget_layout.count()):
            widget = self.main_widnow.sliders_widget_layout.itemAt(i).widget()
            
            # Check if the widget is an instance of your custom Slider class
            if isinstance(widget, Slider):
                # Set the slider value to 1
                widget.disconnect_value_changed()
                widget.slider_widget.setValue(1)
                widget.connect_value_changed()

    def save_and_play_wav(self, file_path, modified_data, sample_rate): 
        # Normalize the modified data to range [-32767, 32767] (16-bit PCM) 
        modified_data_int16 = np.int16(modified_data / np.max(np.abs(modified_data)) * 32767) 
        # Write the modified data to a .wav file 
        output_file_path = "modified_" + file_path 
        wavfile.write(output_file_path, sample_rate, modified_data_int16) 
        # Play the modified .wav file 
        sd.play(modified_data_int16, sample_rate) 
        sd.wait() 
        return output_file_path
        # Wait until the file is done playing return output_file_path