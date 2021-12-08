import csv 
import numpy as np

def getdata(datapath):
    Sizetv=[]
    Hoursspent=[]

    with open (datapath)as cvfile:
        cvreader=csv.DictReader(cvfile)
        for row in cvreader:
            Sizetv.append(float(row['Size of TV']))
            Hoursspent.append(float(row['	Average time spent watching TV']))
    return{'x':Sizetv,'y':Hoursspent} 

def cof(datasource):
    correlation=np.corrcoef(datasource['x'],datasource ['y']) 
    print("Correlation between Size of Tv and Average time spent watching Tv in a week :-  \n--->",correlation[0,1])
def setup():
    datapath="tv.csv"
    datasource=getdata(datapath)
    cof(datasource)    


setup()  