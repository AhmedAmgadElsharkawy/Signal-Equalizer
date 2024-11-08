from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QLabel, QSlider, QPushButton, QComboBox, QFrame, QGroupBox,QScrollArea,QCheckBox
)

from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Sampling Theory Studio')
        self.setGeometry(100, 100, 1400, 900)
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.main_layout = QHBoxLayout(self.main_widget)

        self.graphs_widget = QWidget()
        self.graphs_widget_layout = QVBoxLayout(self.graphs_widget)

        self.controls_widget = QWidget()
        self.controls_widget.setObjectName("controls_widget")
        self.controls_widget_layout = QVBoxLayout(self.controls_widget)
        self.controls_widget_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.controls_widget.setFixedWidth(350)

        self.main_layout.addWidget(self.graphs_widget)
        self.main_layout.addWidget(self.controls_widget)


        self.controls_buttons_widget = QWidget()
        self.controls_buttons_widget.setObjectName("controls_buttons_widget")
        self.controls_buttons_widget.setFixedHeight(170)
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
        self.play_button = QPushButton("play")
        self.rewind_button = QPushButton("rewind")
        self.play_rewind_widget_layout.addWidget(self.play_button)
        self.play_rewind_widget_layout.addWidget(self.rewind_button)
        self.speed_up_button = QPushButton("speed up")
        self.speed_down_button = QPushButton("speed down")
        self.speed_up_down_widget_layout.addWidget(self.speed_up_button)
        self.speed_up_down_widget_layout.addWidget(self.speed_down_button)



        
        

        
        
        
        self.setStyleSheet("""
            *{
                padding:0px;
                margin:0px;
            }

            #controls_widget{
                border:2px solid gray;
                border-radius:15px;
                padding:15px;
            }
            #controls_buttons_widget{
                border:2px solid gray;   
                border-radius:15px;      
                padding:0px;     
            }
            #controls_buttons_widget QPushButton{
                padding:4px 0px;                
            }
        """)




        