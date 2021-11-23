import numpy as np

class WeatherAnalyzer:
    def __init__(self, TemperatureDataList):
        self.TemperatureDataList = TemperatureDataList


    def getMinTemp(self):
        MinTemp = []
        for i in range(0, len(self.TemperatureDataList)):
            MinTemp.append(self.TemperatureDataList[i].minTemperature)
        return np.amin(MinTemp)


    def getMaxTemp(self):
        MaxTemp = []
        for i in range(0, len(self.TemperatureDataList)):
            MaxTemp.append(self.TemperatureDataList[i].maxTemperature)
        return np.amax(MaxTemp)


    def getMinTempAnnually(self):
        x = 0
        y = 12
        MonthlyMinTemp = []
        AnnualMinTemp = []
        for i in range (1990, 2020):
            if i == 2019:
                for j in range (x, y-1):
                    MonthlyMinTemp.append(self.TemperatureDataList[j].minTemperature)
                LowestYearTemp = np.amin(MonthlyMinTemp)
                YearTempPair = [i, LowestYearTemp]
                AnnualMinTemp.append(YearTempPair)     

                MonthlyMinTemp = []        
                x += 12
                y += 12   

            else:
                for j in range (x, y):
                    MonthlyMinTemp.append(self.TemperatureDataList[j].minTemperature)
                LowestYearTemp = np.amin(MonthlyMinTemp)
                YearTempPair = [i, LowestYearTemp]
                AnnualMinTemp.append(YearTempPair)
            
                MonthlyMinTemp = []        
                x += 12
                y += 12
        return AnnualMinTemp


    def getMaxTempAnnually(self):
        x = 0
        y = 12
        MonthlyMaxTemp = []
        AnnualMaxTemp = []
        for i in range (1990, 2020):
            if i == 2019:
                for j in range (x, y-1):
                    MonthlyMaxTemp.append(self.TemperatureDataList[j].maxTemperature)
                HighestYearTemp = np.amax(MonthlyMaxTemp)
                YearTempPair = [i, HighestYearTemp]
                AnnualMaxTemp.append(YearTempPair)    

                MonthlyMaxTemp = []        
                x += 12
                y += 12

            else:
                for j in range (x, y):
                    MonthlyMaxTemp.append(self.TemperatureDataList[j].maxTemperature)
                HighestYearTemp = np.amax(MonthlyMaxTemp)
                YearTempPair = [i, HighestYearTemp]
                AnnualMaxTemp.append(YearTempPair)
            
                MonthlyMaxTemp = []        
                x += 12
                y += 12
        return AnnualMaxTemp

    
    def getAvgSnowFallAnnually(self):
        x = 0
        y = 12
        MonthlySnowFall = []
        AnnualAvgSnowFall = []
        for i in range (1990, 2020):
            if i == 2019:
                for j in range (x, y-1):
                    MonthlySnowFall.append(self.TemperatureDataList[j].snowFall)
                AvgYearSnowFall = np.average(MonthlySnowFall)
                YearSnowFallPair = [i, AvgYearSnowFall]
                AnnualAvgSnowFall.append(YearSnowFallPair)

                MonthlySnowFall = []        
                x += 12
                y += 12

            else:
                for j in range (x, y):
                    MonthlySnowFall.append(self.TemperatureDataList[j].snowFall)
                AvgYearSnowFall = np.average(MonthlySnowFall)
                YearSnowFallPair = [i, AvgYearSnowFall]
                AnnualAvgSnowFall.append(YearSnowFallPair)
            
                MonthlySnowFall = []        
                x += 12
                y += 12
        return AnnualAvgSnowFall   


    def getAvgTempAnually(self):
        x = 0
        y = 12
        YearTemps = []
        AnnualAvgTemp = []
        for i in range(1990, 2020):
            if i == 2019:
                for j in range(x, y-1):
                    MonthlyTemps = [self.TemperatureDataList[j].minTemperature, self.TemperatureDataList[j].maxTemperature]
                    MonthAvg = np.average(MonthlyTemps)
                    YearTemps.append(MonthAvg)
                YearAvg = np.average(YearTemps)
                YearAvgTempPair = [i, YearAvg]
                AnnualAvgTemp.append(YearAvgTempPair)

                YearTemps = []
                x += 12
                y += 12

            else:
                for j in range(x, y):
                    MonthlyTemps = [self.TemperatureDataList[j].minTemperature, self.TemperatureDataList[j].maxTemperature]
                    MonthAvg = np.average(MonthlyTemps)
                    YearTemps.append(MonthAvg)
                YearAvg = np.average(YearTemps)
                YearAvgTempPair = [i, YearAvg]
                AnnualAvgTemp.append(YearAvgTempPair)

                YearTemps = []
                x += 12
                y += 12
        return AnnualAvgTemp

    



