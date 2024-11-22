from scipy.signal import spectrogram
import numpy as np

class SpectrogramController:
    def __init__(self,main_window):
        self.main_window = main_window
    
    def plot_spectrogram(self):
        data = self.main_window.signal.data
        modified_data = self.main_window.signal.modified_data
        sample_rate = self.main_window.signal.sample_rate

        f_original, t_original, Sxx_original = spectrogram(data, sample_rate)
        f_updated, t_updated, Sxx_updated = spectrogram(modified_data, sample_rate)
        
        self.main_window.input_cine_signal_viewer.spectogram_ax.clear() 
        self.main_window.output_cine_signal_viewer.spectogram_ax.clear()
        """
            divide by zero error with the logarithm so we use small epsilon to plot
            zero-values signal's spectrogram with the minimum color 
        """
        epsilon = 1e-10
        self.main_window.output_cine_signal_viewer.spectogram_ax.pcolormesh(t_updated, f_updated, 10 * np.log10(Sxx_updated+epsilon), shading='auto')
        self.main_window.input_cine_signal_viewer.spectogram_ax.pcolormesh(t_original, f_original, 10 * np.log10(Sxx_original+epsilon), shading='auto')

        self.main_window.output_cine_signal_viewer.signal_spectrogram.draw()
        self.main_window.input_cine_signal_viewer.signal_spectrogram.draw()