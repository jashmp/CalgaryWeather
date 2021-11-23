import matplotlib.pyplot as pyplot
import numpy as np

class Chart:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def drawLineChart(self, title, xlabel, ylabel):
        pyplot.figure()
        pyplot.title(title)
        pyplot.xlabel(xlabel)
        pyplot.ylabel(ylabel)

        pyplot.plot(self.x, self.y, marker = 'o')
        pyplot.show()

    def drawBarChart(self, title, xlabel, ylabel):
        pyplot.bar(self.x, self.y, align='center', alpha=0.7)
        pyplot.title(title)
        pyplot.xlabel(xlabel)
        pyplot.ylabel(ylabel)
        pyplot.show()