import numpy as np
from scipy.io import wavfile
import sounddevice as sd
class OutputController:
    def __init__(self,main_window):
        self.main_widnow = main_window

    def sliderChanged(self, value, min_freq, max_freq):
        self.main_widnow.signal.signal_processing(value, min_freq, max_freq)
        self.main_widnow.buttons_controller.plot_the_signal()

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