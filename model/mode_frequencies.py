import math

class slider_data:
    def __init__(self,slider_label,min_freq,max_freq):
        self.slider_label = slider_label
        self.min_freq = min_freq
        self.max_freq = max_freq



mode_sliders_data = {
    "Uniform Range":[],

    "Musical Instruments":[slider_data("bass",0,350),slider_data("triangle",351,1000),
                           slider_data("trombone",860,4000),slider_data("xylephone",4200,22000)],

    "Animal Sounds":[slider_data("owl",650,950),slider_data("frog",951,1900),
                    slider_data("canary",3000,5500),slider_data("insect",6000,20000)],

    "ECG Abnormalities":[slider_data("normal", 0, 150),slider_data("Aflut",51,60),
                    slider_data("Vt",120,200),slider_data("Afib",1101,1200)]
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