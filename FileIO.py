import numpy as np
class FileIO:
    def __init__(self, filePath):
        self.filePath = filePath

    def Read_File(self):
        return np.loadtxt(self.filePath, delimiter=',', skiprows=1, usecols=(0, 1, 2, 3, 4), dtype=np.float)
        



