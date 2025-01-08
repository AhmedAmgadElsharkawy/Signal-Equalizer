import pyqtgraph as pg
import numpy as np

class WienerFilterController:
    def __init__(self,wiener_filter_view,main_window):
        self.main_window = main_window
        self.wiener_filter_view = wiener_filter_view
        self.wiener_filter_view.apply_filter_button.clicked.connect(self.apply_filter)
        self.wiener_filter_view.reset_filter_button.clicked.connect(self.reset_filter)

        


    def apply_filter(self):
        self.main_window.signal.reset_modified_data()
        selected_y = self.extract_the_selected_region()

        N = len(self.main_window.signal.data)
        signal_fft = self.main_window.signal.freq_coeffs

        noise_fft = np.fft.rfft(selected_y, n=N)

        signal_psd = np.abs(signal_fft)**2
        noise_psd = np.abs(noise_fft)**2
        alpha = 30

        window_size = 25
        kernel = np.hanning(window_size)

        signal_psd = np.convolve(signal_psd, kernel, mode='same')
        noise_psd = np.convolve(noise_psd, kernel, mode='same')

        weights = signal_psd / (signal_psd + alpha * noise_psd)

        weighted_signal = signal_fft * weights

        filtered_signal = np.fft.irfft(weighted_signal)
        filtered_signal = filtered_signal[:N]

        self.main_window.signal.modified_data = filtered_signal
        self.main_window.signal.freq_coeffs = np.fft.rfft(filtered_signal)
        self.main_window.signal.magnitudes = 10 / N * np.abs(self.main_window.signal.freq_coeffs)

        self.main_window.signal.sound_data = self.main_window.signal.modified_data / np.max(np.abs(self.main_window.signal.modified_data)) 

        self.main_window.buttons_controller.plot_the_signal()

    def reset_filter(self):
        self.main_window.signal.reset_modified_data()
        self.main_window.buttons_controller.plot_the_signal()

    def plot_the_wiener(self):
        self.wiener_filter_view.wiener_plot_widget.clear()
        self.wiener_filter_view.wiener_linear_region_item = pg.LinearRegionItem(movable=True)
        self.wiener_filter_view.wiener_plot_widget.addItem(self.wiener_filter_view.wiener_linear_region_item)
        self.wiener_filter_view.wiener_plot_widget.plot(self.main_window.signal.time, self.main_window.signal.data, pen=pg.mkPen(color=(170, 0, 0)))
        self.wiener_filter_view.wiener_plot_widget.setLimits(xMin=0, xMax=self.main_window.signal.time[len(self.main_window.signal.time)-1], yMin=self.main_window.signal.min_data_point, yMax=self.main_window.signal.max_data_point)
        self.wiener_filter_view.wiener_linear_region_item.setBounds([0,self.main_window.signal.time[len(self.main_window.signal.time)-1]])
        self.wiener_filter_view.wiener_linear_region_item.setRegion([0,self.main_window.signal.time[len(self.main_window.signal.time)-1]/2])
    
    def extract_the_selected_region(self):
        region = self.wiener_filter_view.wiener_linear_region_item.getRegion()
        start, end = region[0], region[1]
        selected_indices = (self.main_window.signal.time >= start) & (self.main_window.signal.time <= end)
        return self.main_window.signal.data[selected_indices]
        
        

    
