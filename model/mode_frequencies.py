import math

class slider_data:
    def __init__(self,slider_label,min_freq,max_freq):
        self.slider_label = slider_label
        self.min_freq = min_freq
        self.max_freq = max_freq



mode_sliders_data = {
    "Uniform Range":[],

    "Musical Instruments":[slider_data("bass",0,550),slider_data("Guitar",0,1000),
                           slider_data("5",500,700),slider_data("7",700,900),slider_data("9",900, 1100),slider_data("11",1100,1300),
                           slider_data("1",6000,7000),slider_data("15",1500,1700),slider_data("17",1700,2500) ,slider_data("S",3500,11700)],

    "Animal Sounds":[slider_data("owl",1000,1200),slider_data("frog",1200,1400),
                    slider_data("canary",1400,1600),slider_data("insect",6000,20000)],

    "ECG Abnormalities":[slider_data("normal",0,150),slider_data("Aflut",40,60),
                    slider_data("Vt",95,155),slider_data("Afib",60,95)]
}


def generate_uniform_range(freqs):
    mode_sliders_data["Uniform Range"].clear()
    if len(freqs) == 0:
        return
    min_frequency = freqs[0]
    max_frequency = freqs[-1]
    Range = max_frequency - min_frequency
    step = Range / 10
    for i in range(10):
        begin  = math.floor(min_frequency+i*step)
        end = math.ceil(min_frequency+(i+1)*step)
        mode_sliders_data["Uniform Range"].append(slider_data(f"{begin}-{end}",begin,end))