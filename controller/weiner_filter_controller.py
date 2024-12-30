import pyqtgraph as pg

class WeinerFilterController:
    def __init__(self,weiner_filter_view,main_window):
        self.main_window = main_window
        self.weiner_filter_view = weiner_filter_view
        self.weiner_filter_view.apply_filter_button.clicked.connect(self.apply_filter)
        self.weiner_filter_view.reset_filter_button.clicked.connect(self.reset_filter)


    def apply_filter(self):
        pass

    def reset_filter(self):
        pass

    def plot_the_weiner(self):
        self.weiner_filter_view.weiner_plot_widget.clear()
        self.weiner_filter_view.weiner_linear_region_item = pg.LinearRegionItem(movable=True)
        self.weiner_filter_view.weiner_plot_widget.addItem(self.weiner_filter_view.weiner_linear_region_item)
        self.weiner_filter_view.weiner_plot_widget.plot(self.main_window.signal.time, self.main_window.signal.data, pen=pg.mkPen(color=(170, 0, 0)))
        self.weiner_filter_view.weiner_plot_widget.setLimits(xMin=0, xMax=self.main_window.signal.time[len(self.main_window.signal.time)-1], yMin=self.main_window.signal.min_data_point, yMax=self.main_window.signal.max_data_point)
        self.weiner_filter_view.weiner_linear_region_item.setBounds([0,self.main_window.signal.time[len(self.main_window.signal.time)-1]])
        self.weiner_filter_view.weiner_linear_region_item.setRegion([0,self.main_window.signal.time[len(self.main_window.signal.time)-1]/2])
    

    
