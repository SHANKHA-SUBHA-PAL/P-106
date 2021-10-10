import csv
import numpy as np
import plotly_express as px

def getDataSource(data_path):
    temperature = []
    icecream_sales = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            temperature.append(float(row["Temperature"]))
            icecream_sales.append(float(row["Ice-cream Sales"]))

    return {"x" : temperature, "y": icecream_sales}

def plotFig():
    
    with open("P-106\ICE-CREAM VS COLD DRINK.csv") as csv_file:
        df = csv.reader(csv_file)
        fig = px.scatter(df,x = "Temperature", y = "Ice-cream Sales")
        fig.show()


def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Marks in percentage and Days present :-  \n--->",correlation[0,1])

def setup():
    data_path  = "P-106\ICE-CREAM VS COLD DRINK.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFig()

setup()
