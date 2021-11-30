import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

file = pd.read_excel("ProjectData.xls")
print(file)

CPI1 = list(file['CPI 1'])
UR1 = list(file['Unemployment Rate 1'])
CPI2 = list(file['CPI 2'])
UR2 = list(file['Unemployment Rate 2'])
CPI3 = list(file['CPI 3'])
UR3 = list(file['Unemployment Rate 3'])
CPI4 = list(file['CPI 4'])
UR4 = list(file['Unemployment Rate 4'])
CPI5 = list(file['CPI 5'])
UR5 = list(file['Unemployment Rate 5'])



def Begin(CPI1, CPI2, CPI3, CPI4, CPI5,UR1, UR2, UR3, UR4, UR5):  
    run = True
    while run == True:
        print("1 for 1, 2 for 2, 3 for 3, 4 for 4, 5 for 5, 6 for all, or n to stop.")
        start = str(input("Please enter the number of the store you would like the results\n" 
                           + "of, or if you would like to see the overall results or n to stop:"))
        if start.upper() == 'N':
            run = False
            break
        elif start == '1':
            GraphStore1(CPI1, UR1)
        elif start == '2':
            GraphStore2(CPI2, UR2)
        elif start == '3':
            GraphStore3(CPI3, UR3)
        elif start == '4':
            GraphStore4(CPI4, UR4)
        elif start == '5':
            GraphStore5(CPI5, UR5)
        elif start == '6':
            OverallCPI = CPIlist(CPI1, CPI2, CPI3, CPI4, CPI5)
            OverallUR = URlist(UR1, UR2, UR3, UR4, UR5)
            PlotOverall(CPI1, CPI2, CPI3, CPI4, CPI5,UR1, UR2, UR3, UR4, UR5,OverallCPI, OverallUR)
        CalcCov(CPI1, CPI2, CPI3, CPI4, CPI5,UR1, UR2, UR3, UR4, UR5)
        VarCalc(CPI1, CPI2, CPI3, CPI4, CPI5,UR1, UR2, UR3, UR4, UR5)
        
        
        




def CPIlist(CPI1, CPI2, CPI3, CPI4, CPI5):
    overalllistCPI = []
    for i in range(len(CPI1)):
        avg = ((CPI1[i] + CPI2[i] + CPI3[i] + CPI4[i] + CPI5[i])/5)
        overalllistCPI.append(avg)

    return overalllistCPI

def URlist(UR1, UR2, UR3, UR4, UR5):
    overalllistUR = []
    for i in range(len(UR1)):
        avg = ((UR1[i] + UR2[i] + UR3[i] + UR4[i] + UR5[i])/5)
        overalllistUR.append(avg)
    return overalllistUR

def CalcCov(CPI1, CPI2, CPI3, CPI4, CPI5,UR1, UR2, UR3, UR4, UR5):
    templist = [CPI1, CPI2, CPI3, CPI4, CPI5]
    templist2 = [UR1, UR2, UR3, UR4, UR5]
    CPIlist = []
    URlist = []
    for i in range(len(templist)):
        x = templist[i]
        y = templist2[i]
        for j in range(len(x)):
            CPIlist.append(x[j])
            URlist.append(y[j])
    CPIavg = 0
    URavg = 0
    for i in range(len(CPIlist)):
        CPIavg += CPIlist[i]
        URavg += URlist[i]
    CPIavg = CPIavg / len(CPIlist)
    URavg = URavg / len(URlist)
    cov = 0
    for i in range(len(CPIlist)):
        cov += ((CPIlist[i]-CPIavg)*(URlist[i]-URavg))
    cov = cov/len(URlist)
    print("Covariance :" + str(cov))
    print("CPI average :" + str(CPIavg))
    print("UR average :" + str(URavg))

def VarCalc(CPI1, CPI2, CPI3, CPI4, CPI5,UR1, UR2, UR3, UR4, UR5):
    templist = [CPI1, CPI2, CPI3, CPI4, CPI5]
    templist2 = [UR1, UR2, UR3, UR4, UR5]
    CPIlist = []
    URlist = []
    for i in range(len(templist)):
        x = templist[i]
        y = templist2[i]
        for j in range(len(x)):
            CPIlist.append(x[j])
            URlist.append(y[j])
    CPIavg = 0
    URavg = 0
    for i in range(len(CPIlist)):
        CPIavg += CPIlist[i]
        URavg += URlist[i]
    CPIavg = CPIavg / len(CPIlist)
    URavg = URavg / len(URlist)
    CPIvar = 0
    URvar = 0
    
    for i in range(len(CPIlist)):
        CPIvar += ((CPIlist[i] - CPIavg)**2)
        URvar += ((URlist[i] - URavg)**2)
    cov = 0
    for i in range(len(CPIlist)):
        cov += ((CPIlist[i]-CPIavg)*(URlist[i]-URavg))
    cov = cov/len(URlist)
    CPIvar = CPIvar / len(CPIlist)
    URvar = URvar / len(URlist)
    CPIsd = math.sqrt(CPIvar)
    URsd = math.sqrt(URvar)
    r = cov/(CPIsd*URsd)
    
    print("R^2 :" + str(r))
    print("CPI variance :" + str(CPIvar))
    print("UR variance :" + str(URvar))
    print("CPI standard deviation :" + str(CPIsd))
    print("UR standard deviation :" + str(URsd))
        
        

def PlotOverall(CPI1, CPI2, CPI3, CPI4, CPI5,UR1, UR2, UR3, UR4, UR5,OverallCPI, OverallUR):
    plt.figure(figsize = (10,10))
    plt.style.use('seaborn')
    plt.scatter(OverallCPI,OverallUR,marker = ".", s=100, edgecolors = "black", c = "yellow")
    x = np.array(OverallCPI)
    y = np.array(OverallUR)
    m , b = np.polyfit(x,y,1)
    plt.plot(x, m*x + b)
    plt.title("Average Change in Unemployment Rate as CPI Increases Across 5 Stores")
    plt.xlabel("CPI")
    plt.ylabel("Unemployment Rate")
    plt.show()

def GraphStore1(CPI1, UR1):
    plt.figure(figsize = (10,10))
    plt.style.use('seaborn')
    plt.scatter(CPI1,UR1,marker = ".", s=100, edgecolors = "black", c = "yellow")
    x = np.array(CPI1)
    y = np.array(UR1)
    m , b = np.polyfit(x,y,1)
    plt.plot(x, m*x + b)
    plt.title("Store 1 Change in Unemployment Rate as CPI Increases")
    plt.xlabel('CPI')
    plt.ylabel("Unemployment Rate")
    plt.show()

def GraphStore2(CPI2, UR2):
    plt.figure(figsize = (10,10))
    plt.style.use('seaborn')
    plt.scatter(CPI2,UR2,marker = ".", s=100, edgecolors = "black", c = "yellow")
    x = np.array(CPI2)
    y = np.array(UR2)
    m , b = np.polyfit(x,y,1)
    plt.plot(x, m*x + b)
    plt.title("Store 2 Change in Unemployment Rate as CPI Increases")
    plt.xlabel('CPI')
    plt.ylabel("Unemployment Rate")
    plt.show()

def GraphStore3(CPI3, UR3):
    plt.figure(figsize = (10,10))
    plt.style.use('seaborn')
    plt.scatter(CPI3,UR3,marker = ".", s=100, edgecolors = "black", c = "yellow")
    x = np.array(CPI3)
    y = np.array(UR3)
    m , b = np.polyfit(x,y,1)
    plt.plot(x, m*x + b)
    plt.title("Store 3 Change in Unemployment Rate as CPI Increases")
    plt.xlabel('CPI')
    plt.ylabel("Unemployment Rate")
    plt.show()

def GraphStore4(CPI4, UR4):
    plt.figure(figsize = (10,10))
    plt.style.use('seaborn')
    plt.scatter(CPI4,UR4,marker = ".", s=100, edgecolors = "black", c = "yellow")
    x = np.array(CPI4)
    y = np.array(UR4)
    m , b = np.polyfit(x,y,1)
    plt.plot(x, m*x + b)
    plt.title("Store 4 Change in Unemployment Rate as CPI Increases")
    plt.xlabel('CPI')
    plt.ylabel("Unemployment Rate")
    plt.show()

def GraphStore5(CPI5, UR5):
    plt.figure(figsize = (10,10))
    plt.style.use('seaborn')
    plt.scatter(CPI5,UR5,marker = ".", s=100, edgecolors = "black", c = "yellow")
    x = np.array(CPI5)
    y = np.array(UR5)
    m , b = np.polyfit(x,y,1)
    plt.plot(x, m*x + b)
    plt.title("Store 5 Change in Unemployment Rate as CPI Increases")
    plt.xlabel('CPI')
    plt.ylabel("Unemployment Rate")
    plt.show()


Begin(CPI1, CPI2, CPI3, CPI4, CPI5,UR1, UR2, UR3, UR4, UR5)





