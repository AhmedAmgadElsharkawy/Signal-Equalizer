import math

class slider_data:
    def __init__(self,slider_label,ranges):
        self.slider_label = slider_label
        self.ranges = ranges



mode_sliders_data = {
    "Uniform Range":[],

    "Musical Instruments":[slider_data("bass",[(0,550)]),slider_data("Guitar",[(0,1000)]),slider_data("S",[(3500,11700)]),
                            slider_data("A", [(300, 400), (550, 750), (800, 1000), (1300, 1500), (1600, 1800)]), 
                            slider_data("W", [(260, 380), (400, 480), (520, 620), (650, 720), (870, 920), (975, 1050), (1150, 1230), (1450, 1500), (1750, 1790), (2900, 3000), (3120, 3300), (3450, 3580), (3750, 3870)])],

    "Animal Sounds":[slider_data("owl",[(1000,1200)]),slider_data("frog",[(1200,1400)]),
                    slider_data("canary",[(1400,1600)]),slider_data("insect",[(6000,20000)]), slider_data("Cat", [(600, 620), (1100, 1200), (1700, 2160), (4500, 6000)]),
                    slider_data("Bat", [(6000, 20000)]), slider_data("Bird", [(2600, 4500)])],
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