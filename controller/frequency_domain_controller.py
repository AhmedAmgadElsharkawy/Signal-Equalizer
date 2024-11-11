import numpy as np
import pyqtgraph as pg

class FrequencyDomainController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.current_scale = 'linear'

    def convert_to_db(self, magnitude):
        if magnitude == 0:
            return - np.inf
        return 20 * np.log10(magnitude)

    def plot_freq_domain(self, freqs, magnitudes, scale=None):
        if scale is not None:
            self.current_scale = scale
        self.main_window.frequency_domain_viewer.frequency_domain_plot.clear()
        
        if scale == 'linear':
            # Linear scale plotting
            self.main_window.frequency_domain_viewer.frequency_domain_plot.plot(
                freqs, magnitudes, pen=pg.mkPen(color=(170, 0, 0))
            )
        elif scale == 'audiogram':
            # Audiogram (dB) scale plotting
            audiogram_mag = np.array([self.convert_to_db(mag) for mag in magnitudes])
            self.main_window.frequency_domain_viewer.frequency_domain_plot.plot(
                freqs, audiogram_mag, pen='b'
            )
            # self.main_window.frequency_domain_viewer.frequency_domain_plot.invertY()

        self.main_window.frequency_domain_viewer.frequency_domain_plot.setLabel('bottom', 'Frequency (Hz)')
        self.main_window.frequency_domain_viewer.frequency_domain_plot.setLabel('left', 'Magnitude')
