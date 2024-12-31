from scipy.signal import spectrogram
import numpy as np

class SpectrogramController:
    def __init__(self, main_window):
        self.main_window = main_window
    
    def plot_spectrogram(self):
        data = self.main_window.signal.data
        modified_data = self.main_window.signal.modified_data
        sample_rate = self.main_window.signal.sample_rate

        f_original, t_original, Sxx_original = spectrogram(data, sample_rate)
        f_updated, t_updated, Sxx_updated = spectrogram(modified_data, sample_rate)


        Sxx_original = np.round(Sxx_original, 1)
        Sxx_updated = np.round(Sxx_updated, 1)

        self.main_window.input_cine_signal_viewer.spectogram_ax.clear()
        self.main_window.output_cine_signal_viewer.spectogram_ax.clear()

        epsilon = 1e-10
        input_signal_pcm = self.main_window.input_cine_signal_viewer.spectogram_ax.pcolormesh(
            t_original, f_original, 10 * np.log10(Sxx_original + epsilon), shading='auto'
        )
        output_signal_pcm = self.main_window.output_cine_signal_viewer.spectogram_ax.pcolormesh(
            t_updated, f_updated, 10 * np.log10(Sxx_updated + epsilon), shading='auto'
        )

        self.main_window.input_cine_signal_viewer.color_bar = self.main_window.input_cine_signal_viewer.spectrogram_figure.colorbar(
            input_signal_pcm, ax=self.main_window.input_cine_signal_viewer.spectogram_ax, label='Intensity [dB]'
        )
        self.main_window.output_cine_signal_viewer.color_bar = self.main_window.output_cine_signal_viewer.spectrogram_figure.colorbar(
            output_signal_pcm, ax=self.main_window.output_cine_signal_viewer.spectogram_ax, label='Intensity [dB]'
        )

        self.main_window.input_cine_signal_viewer.signal_spectrogram.draw()
        self.main_window.output_cine_signal_viewer.signal_spectrogram.draw()
