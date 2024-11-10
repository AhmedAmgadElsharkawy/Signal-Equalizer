from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QComboBox, QScrollArea, QCheckBox, QButtonGroup, QRadioButton, QFileDialog
from PyQt5.QtCore import Qt
from view.slider import Slider
from model.mode_frequencies import mode_sliders_data
from view.cine_signal_viewer import CineSignalViewer
from view.frequency_domain_viewer import FrequencyDomainViewer
from controller.frequency_domain_controller import FrequencyDomainController
from controller.mode_controller import ModeController
from controller.output_controller import OutputController
from controller.playback_buttons_controller import PlaybackButtonsController
from controller.spectrogram_controller import SpectrogramController
import numpy as np
from scipy.fft import fft
import pyqtgraph as pg
from scipy.io import wavfile


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Sampling Theory Studio')
        self.setGeometry(100, 100, 1400, 900)
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.main_layout = QHBoxLayout(self.main_widget)

        self.graphs_widget = QWidget()
        self.graphs_widget.setObjectName("graphs_widget")
        self.graphs_widget_layout = QVBoxLayout(self.graphs_widget)

        self.controls_widget = QWidget()
        self.controls_widget.setObjectName("controls_widget")
        self.controls_widget_layout = QVBoxLayout(self.controls_widget)
        self.controls_widget_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.controls_widget.setFixedWidth(350)
        self.controls_widget_layout.setSpacing(15)

        self.main_layout.addWidget(self.graphs_widget)
        self.main_layout.addWidget(self.controls_widget)

        self.controls_buttons_widget = QWidget()
        self.controls_buttons_widget.setObjectName("controls_buttons_widget")
        self.controls_buttons_widget.setFixedHeight(250)
        self.controls_buttons_widget_layout = QVBoxLayout(self.controls_buttons_widget)
        self.controls_buttons_widget_layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.controls_widget_layout.addWidget(self.controls_buttons_widget)

        self.load_reset_widget = QWidget()
        self.load_reset_widget_layout = QHBoxLayout(self.load_reset_widget)
        self.play_rewind_widget = QWidget()
        self.play_rewind_widget_layout = QHBoxLayout(self.play_rewind_widget)
        self.speed_up_down_widget = QWidget()
        self.speed_up_down_widget_layout = QHBoxLayout(self.speed_up_down_widget)
        self.controls_buttons_widget_layout.addWidget(self.load_reset_widget)
        self.controls_buttons_widget_layout.addWidget(self.play_rewind_widget)
        self.controls_buttons_widget_layout.addWidget(self.speed_up_down_widget)

        self.load_signal_button = QPushButton("load")
        self.clear_signal_button = QPushButton("clear")
        self.load_reset_widget_layout.addWidget(self.load_signal_button)
        self.load_reset_widget_layout.addWidget(self.clear_signal_button)
        self.load_signal_button.clicked.connect(self.loadSignal)
        self.play_button = QPushButton("play")
        self.rewind_button = QPushButton("rewind")
        self.play_rewind_widget_layout.addWidget(self.play_button)
        self.play_rewind_widget_layout.addWidget(self.rewind_button)
        self.speed_up_button = QPushButton("speed up")
        self.speed_down_button = QPushButton("speed down")
        self.speed_up_down_widget_layout.addWidget(self.speed_up_button)
        self.speed_up_down_widget_layout.addWidget(self.speed_down_button)

        self.spectrograms_visibility_widget = QWidget()
        self.spectrograms_visibility_layout = QHBoxLayout(self.spectrograms_visibility_widget)
        self.visible_label = QLabel("Spectrograms")
        self.visible_checkbox = QCheckBox()
        self.visible_checkbox.setChecked(True)
        self.visible_checkbox.stateChanged.connect(self.toggle_spectrograms)
        self.spectrograms_visibility_layout.addWidget(self.visible_label)
        self.spectrograms_visibility_layout.addStretch()
        self.spectrograms_visibility_layout.addWidget(self.visible_checkbox)
        self.controls_buttons_widget_layout.addWidget(self.spectrograms_visibility_widget)

        self.mode_widget = QWidget()
        self.mode_widget.setObjectName("mode_widget")
        self.mode_widget.setFixedHeight(80)
        self.mode_widget_layout = QVBoxLayout(self.mode_widget)
        self.mode_widget_layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.controls_widget_layout.addWidget(self.mode_widget)

        self.mode_label = QLabel("Choose Mode")
        self.mode_label.setObjectName("mode_label")
        self.mode_combobox = QComboBox()
        self.mode_combobox.setObjectName("mode_combobox")
        self.mode_combobox.addItems(["Uniform Range", "Musical Instruments", "Animal Sounds", "ECG Abnormalities"])
        self.mode_widget_layout.addWidget(self.mode_label)
        self.mode_widget_layout.addWidget(self.mode_combobox)

        self.sliders_widget = QScrollArea()
        self.sliders_widget.setObjectName("sliders_widget")
        self.sliders_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.sliders_widget.setWidgetResizable(True) 
        self.sliders_content_widget = QWidget()
        self.sliders_widget.setWidget(self.sliders_content_widget)  
        self.sliders_widget_layout = QVBoxLayout(self.sliders_content_widget)
        self.sliders_widget_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.controls_widget_layout.addWidget(self.sliders_widget)

        self.frequency_plot_scale_widget = QWidget()
        self.frequency_plot_scale_widget.setObjectName("frequency_plot_scale_widget")
        self.frequency_plot_scale_widget_layout = QVBoxLayout(self.frequency_plot_scale_widget)
        self.choose_scale_label = QLabel("Choose frequency plot scale")
        self.choose_scale_label.setObjectName("choose_scale_label")
        self.scale_radio_buttons_group = QButtonGroup()
        self.linear_scale_radio_button = QRadioButton("Linear Scale")
        self.audiogram_scale_radio_button = QRadioButton("Audiogram Scale")
        self.scale_radio_buttons_group.addButton(self.linear_scale_radio_button)
        self.scale_radio_buttons_group.addButton(self.audiogram_scale_radio_button)
        self.frequency_plot_scale_widget_layout.addWidget(self.choose_scale_label)
        self.frequency_plot_scale_widget_layout.addWidget(self.linear_scale_radio_button)
        self.frequency_plot_scale_widget_layout.addWidget(self.audiogram_scale_radio_button)
        self.controls_widget_layout.addWidget(self.frequency_plot_scale_widget)
        self.linear_scale_radio_button.setChecked(True)

        self.load_mode_sliders()

        self.input_cine_signal_viewer = CineSignalViewer()
        self.output_cine_signal_viewer = CineSignalViewer()
        self.graphs_widget_layout.addWidget(self.input_cine_signal_viewer)
        self.graphs_widget_layout.addWidget(self.output_cine_signal_viewer)

        self.frequency_domain_viewer = FrequencyDomainViewer()
        self.graphs_widget_layout.addWidget(self.frequency_domain_viewer)

        self.mode_combobox.currentIndexChanged.connect(self.load_mode_sliders)

        self.mode_controller = ModeController(self)
        self.playback_buttons_controller = PlaybackButtonsController(self)
        self.spectrogram_controller = SpectrogramController(self)
        self.frequency_domain_controller = FrequencyDomainController(self)
        self.output_controller = OutputController(self)


        self.sliders_widget.verticalScrollBar().setStyleSheet("""
            QScrollBar:vertical {
                border: none;
                background: #f0f0f0;
                width: 6px;
                border-radius: 3px;
            }
            QScrollBar::handle:vertical {
                background: #888;
                min-height: 30px;
                border-radius: 5px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                background: none;
            }
            QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
                background: none;
            }
        """)

        self.setStyleSheet("""
            *{
                padding:0px;
                margin:0px;
            }
            #controls_widget{
                border:2px solid gray;
                border-radius:15px;
                padding:10px 15px;
            }
            #controls_buttons_widget{
                border:1px solid gray;   
                border-radius:15px;      
            }
            #controls_buttons_widget QPushButton{
                padding:7px 0px;                
            }
            #mode_widget{
                border:1px solid gray;   
                border-radius:15px;   
            }
            #mode_combobox{
                padding:3px 6px;               
            }
            #mode_label{
                padding:0px 3px;
            }
            #sliders_widget{
                border:1px solid gray;              
            }
            #graphs_widget{
                border:2px solid gray;
                border-radius:15px;      
            }
            #frequency_plot_scale_widget{
                border:1px solid gray;         
                border-radius:15px;
            }
        """)

    def load_mode_sliders(self):
        for i in reversed(range(self.sliders_widget_layout.count())):
            widget = self.sliders_widget_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        mode = self.mode_combobox.currentText()
        mode_sliders_list = mode_sliders_data[mode]
        for slider_object in mode_sliders_list:
            slider = Slider(name=slider_object.slider_label, min_range_value=slider_object.min_freq, max_range_value=slider_object.max_freq)
            self.sliders_widget_layout.addWidget(slider)

    def toggle_spectrograms(self,state):
        if state == Qt.Unchecked:
            self.input_cine_signal_viewer.signal_spectrogram.setVisible(False)
            self.output_cine_signal_viewer.signal_spectrogram.setVisible(False)
        else:
            self.input_cine_signal_viewer.signal_spectrogram.setVisible(True)
            self.output_cine_signal_viewer.signal_spectrogram.setVisible(True)

    def loadSignal(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open .wav file", "", "Audio Files (*.wav)")
        if file_path:
            self.plot_fourier_transform(file_path)
            

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
        self.frequency_domain_viewer.frequency_domain_plot.plot(xf, magnitudes, pen=pg.mkPen(color=(170, 0, 0)))
        self.input_cine_signal_viewer.cine_signal_plot.plot(x, data, pen=pg.mkPen(color=(170, 0, 0)))


