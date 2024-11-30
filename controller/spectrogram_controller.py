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
        Sxx_original_db = self.convert_to_db(Sxx_original)
        Sxx_updated_db = self.convert_to_db(Sxx_updated)
        input_signal_pcm = self.main_window.input_cine_signal_viewer.spectogram_ax.pcolormesh(t_original, f_original, Sxx_original_db, shading='auto')
        output_signal_pcm = self.main_window.output_cine_signal_viewer.spectogram_ax.pcolormesh(t_updated, f_updated,Sxx_updated_db, shading='auto')
        
        
        self.main_window.input_cine_signal_viewer.color_bar = self.main_window.input_cine_signal_viewer.spectrogram_figure.colorbar(input_signal_pcm, ax=self.main_window.input_cine_signal_viewer.spectogram_ax, label='Intensity [dB]')
        self.main_window.output_cine_signal_viewer.color_bar = self.main_window.output_cine_signal_viewer.spectrogram_figure.colorbar(output_signal_pcm, ax=self.main_window.output_cine_signal_viewer.spectogram_ax, label='Intensity [dB]')

        self.main_window.input_cine_signal_viewer.signal_spectrogram.draw()
        self.main_window.output_cine_signal_viewer.signal_spectrogram.draw()

    def convert_to_db(self,Sxx):
        Sxx_db = Sxx.copy()
        for i in range(len(Sxx)):
            for j in range(len(Sxx[0])):
                if(Sxx[i][j] != 0):
                    Sxx_db[i][j] = 10 * np.log10(Sxx[i][j])
        return Sxx_db