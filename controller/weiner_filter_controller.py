import pyqtgraph as pg

class wienerFilterController:
    def __init__(self,wiener_filter_view,main_window):
        self.main_window = main_window
        self.wiener_filter_view = wiener_filter_view
        self.wiener_filter_view.apply_filter_button.clicked.connect(self.apply_filter)
        self.wiener_filter_view.reset_filter_button.clicked.connect(self.reset_filter)


    def apply_filter(self):
        pass

    def reset_filter(self):
        pass

    def plot_the_wiener(self):
        self.wiener_filter_view.wiener_plot_widget.clear()
        self.wiener_filter_view.wiener_linear_region_item = pg.LinearRegionItem(movable=True)
        self.wiener_filter_view.wiener_plot_widget.addItem(self.wiener_filter_view.wiener_linear_region_item)
        self.wiener_filter_view.wiener_plot_widget.plot(self.main_window.signal.time, self.main_window.signal.data, pen=pg.mkPen(color=(170, 0, 0)))
        self.wiener_filter_view.wiener_plot_widget.setLimits(xMin=0, xMax=self.main_window.signal.time[len(self.main_window.signal.time)-1], yMin=self.main_window.signal.min_data_point, yMax=self.main_window.signal.max_data_point)
        self.wiener_filter_view.wiener_linear_region_item.setBounds([0,self.main_window.signal.time[len(self.main_window.signal.time)-1]])
        self.wiener_filter_view.wiener_linear_region_item.setRegion([0,self.main_window.signal.time[len(self.main_window.signal.time)-1]/2])
    

    
