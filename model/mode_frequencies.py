import math

class slider_data:
    def __init__(self,slider_label,ranges):
        self.slider_label = slider_label
        self.ranges = ranges



mode_sliders_data = {
    "Uniform Range":[],

    "Musical Instruments":[slider_data("bass",[(0,550)]),slider_data("Guitar",[(0,1000)]),slider_data("S",[(3500,11700)]),
                            slider_data("A", [(300, 400), (550, 750), (800, 1000), (1300, 1500), (1600, 1800)]), 
                            slider_data("U", [(350, 600), (800, 1000), (1200, 1500), (1800, 1900), (4000, 5000)]),
                            slider_data("I", [(800, 950), (1350, 1450), (1600, 1700), (1100, 1150)])],

    "Animal Sounds":[slider_data("owl",[(1000,1200)]),slider_data("frog",[(1200,1400)]),
                    slider_data("canary",[(1400,1600)]),slider_data("insect",[(6000,20000)]), slider_data("Cat", [(600, 620), (1100, 1200), (1700, 2160), (4500, 6000)]),
                    slider_data("Bat", [(6000, 20000)]), slider_data("Bird", [(2600, 4500)])],

    "ECG Abnormalities":[slider_data("normal",[(0,150)]),slider_data("Aflut",[(40,60)]),
                    slider_data("Vt",[(95,155)]),slider_data("Afib",[(60,95)])]
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
        mode_sliders_data["Uniform Range"].append(slider_data(f"{begin}-{end}",[(begin,end)]))