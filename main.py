import numpy as np
from FileIO import FileIO
from Date import Date
from TemperatureData import TemperatureData
from WeatherAnalyzer import WeatherAnalyzer
from Chart import Chart


def PrintAnnualData(AnnualInfo):
    for i in range(0, len(AnnualInfo)):
        print(f"{AnnualInfo[i][0]}: {AnnualInfo[i][1]}")

def userInput():
    print("1- Get Minimum Temperature of 1990-2019")
    print("2- Get Maximum Temperature of 1990-2019")
    print("3- Get Minimum Temperature of 1990-2019 Annually")
    print("4- Get Maximum Temperature of 1990-2019 Annually")
    print("5- Get Average Snowfall between 1990-2019 Annually")
    print("6- Get Average Temperature between 1990-2019 Annually ")
    print("7- LineChart Minimum Temperature of 1990-2019 Annually")
    print("8- LineChart Maximum Temperature of 1990-2019 Annually")
    print("9- BarChart Average Snowfall between 1990-2019 Annually")
    print("10- BarChart Average Temperature between 1990-2019 Annually")

    choice = int(input("Please choose from the above options: "))
    return choice


def main():
    while True: 
        CalgaryWeather = FileIO("CalgaryWeather.csv")
        dataTable = CalgaryWeather.Read_File()

        DateList = []
        for i in range(0, len(dataTable)):
            DateList.append(Date(dataTable[i][1], dataTable[i][0]))
    
        TemperatureDataList = []
        for i in range(0, len(dataTable)):
            TemperatureDataList.append(TemperatureData(DateList[i], dataTable[i][3], dataTable[i][2], dataTable[i][4]))

        Analyzer = WeatherAnalyzer(TemperatureDataList)
        choice = userInput()

        while True:
            if choice == 1:
                print(Analyzer.getMinTemp())
                break
            elif choice == 2:
                print(Analyzer.getMaxTemp())
                break
            elif choice == 3:
                PrintAnnualData(Analyzer.getMinTempAnnually())
                break
            elif choice == 4:
                PrintAnnualData(Analyzer.getMaxTempAnnually())
                break
            elif choice == 5:
                PrintAnnualData(Analyzer.getAvgSnowFallAnnually())
                break
            elif choice == 6:
                PrintAnnualData(Analyzer.getAvgTempAnually())
                break
            elif choice == 7:
                MinTempAnnually = Analyzer.getMinTempAnnually()
                x = []
                y = []
                title = "Minimum Temperature of 1990-2019 Annually"
                xlabel = "Year"
                ylabel = "Minimum Temperature (°C)"

                for i in range(len(MinTempAnnually)):
                    x.append(MinTempAnnually[i][0])
                    y.append(MinTempAnnually[i][1])

                MinChart = Chart(x, y)
                MinChart.drawLineChart(title, xlabel, ylabel)
                break
            elif choice == 8:
                MaxTempAnnually = Analyzer.getMaxTempAnnually()
                x = []
                y = []
                title = "Maximum Temperature of 1990-2019 Annually"
                xlabel = "Year"
                ylabel = "Maximum Temperature (°C)"

                for i in range(len(MaxTempAnnually)):
                    x.append(MaxTempAnnually[i][0])
                    y.append(MaxTempAnnually[i][1])

                MaxChart = Chart(x, y)
                MaxChart.drawLineChart(title, xlabel, ylabel)
                break
            elif choice == 9:
                AverageSnowfallAnnually = Analyzer.getAvgSnowFallAnnually()
                x = []
                y = []
                title = "Average Snowfall between 1990-2019 Annually"
                xlabel = "Year"
                ylabel = "Average Snowfall (cm)"

                for i in range(len(AverageSnowfallAnnually)):
                    x.append(AverageSnowfallAnnually[i][0])
                    y.append(AverageSnowfallAnnually[i][1])

                SnowBarChart = Chart(x, y)
                SnowBarChart.drawBarChart(title, xlabel, ylabel)
                break
            elif choice == 10:
                AverageTempAnnually = Analyzer.getAvgTempAnually()
                x = []
                y = []
                title = "Average Temperature between 1990-2019 Annually"
                xlabel = "Year"
                ylabel = "Average Temperature (°C)"

                for i in range(len(AverageTempAnnually)):
                    x.append(AverageTempAnnually[i][0])
                    y.append(AverageTempAnnually[i][1])

                AvgBarChart = Chart(x, y)
                AvgBarChart.drawBarChart(title, xlabel, ylabel)
                break
            else:
                choice = int(input("Please input a valid number!: "))
                continue

        cont = input("Would You Like To Continue (Press Y to continue. Press any other key to exit): ")
        print("")
        if cont == "y" or cont == "Y":
            continue
        else:
            break



if __name__ == "__main__":
    main()
 
