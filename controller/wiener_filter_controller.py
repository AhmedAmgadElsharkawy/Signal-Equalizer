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
        phase = np.angle(signal_fft)

        noise_fft = np.fft.rfft(selected_y, n=N)
        noise_power = (np.abs(noise_fft) ** 2) / N

        signal_power = (np.abs(signal_fft) ** 2) / N

        window_size = 25  
        kernel = np.ones(window_size) / window_size

        signal_power_smooth = np.convolve(signal_power, kernel, mode='same')
        noise_power_smooth = np.convolve(noise_power, kernel, mode='same')

        snr = signal_power_smooth / (noise_power_smooth + 1e-10)
        
        snr_threshold = 0.3 
        gain = np.maximum(1 - 1 / (snr + 1), 0)
        gain[snr < snr_threshold] *= 0.5 

        alpha = 10.0  
        gain = np.maximum(1 - alpha * (noise_power_smooth / (signal_power_smooth + 1e-10)), 0.1)
        gain = np.tanh(gain) 
        
        filtered_fft = signal_fft * gain
        filtered_fft = np.abs(filtered_fft) * np.exp(1j * phase)
        filtered_signal = np.fft.irfft(filtered_fft)
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
        
        

    
