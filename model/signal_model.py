import numpy as np
from scipy.io import wavfile
import sounddevice as sd
import pandas as pd
import math

class Signal:
    def __init__(self):
        self.file_path = None
        self.file_extension = None
        self.sample_rate = None
        self.data = []
        self.time = []
        self.freq_coeffs = []
        self.static_freq_coeffs = []
        self.freqs = []
        self.modified_data = []
        self.magnitudes = []
        self.static_magnitudes = []
        self.sound_data = []
        self.freq_range_indices = []
        self.N = None
        self.T = None


    def load_csv_data(self, file_path,file_extension):
        self.file_path = file_path
        self.file_extension = file_extension
        self.data = pd.read_csv(file_path)
        self.data = self.data.to_numpy()
        file_data = pd.read_csv(file_path).iloc[:,0:2]
        self.time = file_data.iloc[:,0]
        self.data = file_data.iloc[:,1]
        self.sample_rate = int(math.ceil(1/(self.time[1]-self.time[0])))
        self.calculate_data()

    def load_wav_data(self,file_path,file_extension):
        self.file_path = file_path
        self.file_extension = file_extension
        self.sample_rate, self.data = wavfile.read(file_path)
        self.time = np.arange(0, len(self.data)) / self.sample_rate
        self.calculate_data()


    def calculate_data(self):
        # Use only one channel if stereo
        if len(self.data.shape) > 1:
            self.data = self.data[:, 0]
        
        # Fourier Transform
        self.N = len(self.data)
        self.T = 1.0 / self.sample_rate
        self.freq_coeffs = np.fft.rfft(self.data)
        self.static_freq_coeffs = self.freq_coeffs.copy()
        self.freqs = np.fft.rfftfreq(self.N, self.T)
        self.magnitudes = 10 / self.N * np.abs(self.freq_coeffs)
        self.static_magnitudes = self.magnitudes.copy()
        self.signal_processing(1, 0, 0)

    def signal_processing(self, value, min_freq, max_freq):
        self.freq_range_indices = np.where((self.freqs >= min_freq) & (self.freqs <= max_freq))
        if value > 1:
            value = 1 + value / 10
        self.magnitudes[self.freq_range_indices] = self.static_magnitudes[self.freq_range_indices] * value
        self.freq_coeffs[self.freq_range_indices] = self.static_freq_coeffs[self.freq_range_indices] * value
        self.modified_data = np.fft.irfft(self.freq_coeffs)
        self.sound_data = self.modified_data / np.max(np.abs(self.modified_data)) 

    def save_and_play_wav(self, main_file, modified_data, sample_rate): 
        # Normalize the modified data to range [-32767, 32767] (16-bit PCM) 
        modified_data_int16 = np.int16(modified_data / np.max(np.abs(modified_data)) * 32767) 
        # Write the modified data to a .wav file 
        if main_file:
            output_file_path = self.file_path
        else:
            output_file_path = "modified_input.wav"
        wavfile.write(output_file_path, sample_rate, modified_data_int16) 
        # Play the modified .wav file 
        sd.play(modified_data_int16, sample_rate) 
        return output_file_path
        # Wait until the file is done playing return output_file_path

    def stop_sound(self):
        sd.stop()
