class slider_data:
    def __init__(self,slider_label,min_freq,max_freq):
        self.slider_label = slider_label
        self.min_freq = min_freq
        self.max_freq = max_freq



mode_sliders_data = {
    "Uniform Range":[slider_data("0-2200",0,2200),slider_data("2200-4400",2200,4400),
                     slider_data("4400-6600",4400,6600),slider_data("6600-8800",6600,8800),
                     slider_data("8800-11000",8800,11000),slider_data("11000-13200",11000,13200),
                     slider_data("13200-15400",13200,15400),slider_data("15400-17600",15400,17600),
                     slider_data("19800-22000",19800,22000)],

    "Musical Instruments":[slider_data("bass",0,350),slider_data("triangle",351,1000),
                           slider_data("trombone",860,4000),slider_data("xylephone",4200,22000)],

    "Animal Sounds":[slider_data("owl",650,950),slider_data("frog",951,1900),
                    slider_data("canary",3000,5500),slider_data("insect",6000,20000)],

    "ECG Abnormalities":[slider_data("normal",39,190),slider_data("Aflut",51,60),
                    slider_data("Vt",120,200),slider_data("Afib",1101,1200)]
}
