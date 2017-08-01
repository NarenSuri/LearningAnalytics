# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 23:11:15 2016

@author: nsuri
"""

# loading the data with pandas
import pandas as panda
import re
import geocoder
import numpy as np
import math

# load the excel sheet
path ="C:/Users/nsuri/Desktop/LearningAnalyticsDS/Data/workspace/"
FileName = "StudentData_GeoCodedFinal.xlsx"
excelsheet = panda.ExcelFile(path+FileName)
print excelsheet.sheet_names
print excelsheet.sheet_names[0]
loadedDataDf = excelsheet.parse("Sheet1")
#print loadedDataDf.head()
# The data has been loaded in to the dataFrame



def setallIndexes(): 
    global GroupByCountry
    global outfileName
    # add lati longi
    global Latitide
    Latitide = loadedDataDf.columns.get_loc('Latitide')+1
    global Longitude
    Longitude = loadedDataDf.columns.get_loc('Longitude')+1
    global country
    country = loadedDataDf.columns.get_loc('country')+1
    global city
    city = loadedDataDf.columns.get_loc('city')+1
    global state
    state = loadedDataDf.columns.get_loc('state')+1
    global country_lati
    country_lati = loadedDataDf.columns.get_loc('country_lati')+1
    global country_longi
    country_longi = loadedDataDf.columns.get_loc('country_longi')+1
    global state_lati
    state_lati = loadedDataDf.columns.get_loc('state_lati')+1
    global state_longi
    state_longi = loadedDataDf.columns.get_loc('state_longi')+1
    global Visa_Permit_Type_Code
    Visa_Permit_Type_Code = loadedDataDf.columns.get_loc('Visa Permit Type Code')+1
    print Visa_Permit_Type_Code

def transLogOfxbylogxPlus1X10(x):
    counts= len(x)
    return float(math.log10(float(counts)/float(math.log10(counts+1))))*10
def transLogOfxbylogxPlus1X(x):
    counts= len(x)
    return float(math.log10(float(counts)/float(math.log10(counts+1))))
def transLogX(x):
    counts= len(x)
    return float(math.log10(counts+1))   
# Group by country
def groupByCountry():
    column = 'GroupByCountry'
    #loadedDataDf[column]=0
    #GroupByCountry = panda.DataFrame(loadedDataDf.groupby('country').size().rename('counts'))
    #GroupByCountry = panda.DataFrame(loadedDataDf.groupby('country').size())
    

    #GroupByCountry = loadedDataDf.groupby(["country","country_lati","country_longi"]).agg({"country":{ 'count': np.count_nonzero}},{"trasnformation":{ trasnformation}})    
    GroupByCountry = loadedDataDf.groupby(["country","country_lati","country_longi"]).agg(['count',transLogOfxbylogxPlus1X,transLogOfxbylogxPlus1X10,transLogX])
    
    GroupByCountry.columns = GroupByCountry.columns.droplevel(0)
    
    print GroupByCountry.ix[:,0:4]
    #print loadedDataDf.groupby(['country']).aggregate(np.count_nonzero)
    saveCsv(column,GroupByCountry.ix[:,0:4])
    #saveExcel(column,GroupByCountry.ix[:,0:4])
# Group by country
def groupByStates():
    column = 'GroupByStates'
    GroupByState = loadedDataDf.groupby(["state_long","state","state_lati","state_longi"]).agg(['count',transLogOfxbylogxPlus1X,transLogOfxbylogxPlus1X10,transLogX])
    
    GroupByState.columns = GroupByState.columns.droplevel(0)
    
    print GroupByState.ix[:,0:5]
    #print loadedDataDf.groupby(['country']).aggregate(np.count_nonzero)
    saveCsv(column,GroupByState.ix[:,0:5])
    #saveExcel(column,GroupByState.ix[:,0:4])

# Group by Visas and states
def GroupByVisasAndStates():
    column = 'GroupByVisasAndStates'
    x = loadedDataDf.ix[:,Visa_Permit_Type_Code-1]==' '
    loadedDataDf.ix[:,Visa_Permit_Type_Code-1][x]='Citizen'
    GroupByStateAndVisa = loadedDataDf.groupby(["Visa Permit Type Code","state_long","state","state_lati","state_longi"]).agg(['count',transLogOfxbylogxPlus1X,transLogOfxbylogxPlus1X10,transLogX])
    
    GroupByStateAndVisa.columns = GroupByStateAndVisa.columns.droplevel(0)
    
    print GroupByStateAndVisa.ix[:,0:5]
    #print loadedDataDf.groupby(['country']).aggregate(np.count_nonzero)
    saveCsv(column,GroupByStateAndVisa.ix[:,0:5])
    #saveExcel(column,GroupByState.ix[:,0:4])
    
# Group by Visas and country
def GroupByVisasAndCountry():
    column = 'GroupByVisasAndCountry'
    x = loadedDataDf.ix[:,country-1]==' '
    loadedDataDf.ix[:,country-1][x]='DontKnow'
    GroupByVisasAndCountry = loadedDataDf.groupby(["Visa Permit Type Code","country","country_lati","country_longi"]).agg(['count',transLogOfxbylogxPlus1X,transLogOfxbylogxPlus1X10,transLogX])
    
    GroupByVisasAndCountry.columns = GroupByVisasAndCountry.columns.droplevel(0)
    
    print GroupByVisasAndCountry.ix[:,0:4]
    #print loadedDataDf.groupby(['country']).aggregate(np.count_nonzero)
    saveCsv(column,GroupByVisasAndCountry.ix[:,0:4])
    #saveExcel(column,GroupByState.ix[:,0:4])

def EachCountryByVisaType():
    visas = sorted(set(loadedDataDf.ix[:,Visa_Permit_Type_Code-1]))
    global loadedDataDf
    loadedDataDf = loadedDataDf.rename(columns={'Visa Permit Type Code': 'Visa_Permit_Type_Code'})

    for visa in visas:
            column = 'CountryByVisaType_'
            if type(visa) is type(123):
                subData = loadedDataDf.query("Visa_Permit_Type_Code==%d" %(visa,))
            else:
                subData = loadedDataDf.query("Visa_Permit_Type_Code=='"+str(visa)+"'")
            GroupByVisasAndCountry = subData.groupby(["Visa_Permit_Type_Code","country","country_lati","country_longi"]).agg(['count',transLogOfxbylogxPlus1X,transLogOfxbylogxPlus1X10,transLogX])
            GroupByVisasAndCountry.columns = GroupByVisasAndCountry.columns.droplevel(0)
            print GroupByVisasAndCountry.ix[:,0:4]
            #print loadedDataDf.groupby(['country']).aggregate(np.count_nonzero)
            column = column+str(visa)
            saveCsv(column,GroupByVisasAndCountry.ix[:,0:4])
            #saveExcel(column,GroupByState.ix[:,0:4])    
def EachStateByVisaType():
    visas = sorted(set(loadedDataDf.ix[:,Visa_Permit_Type_Code-1]))
    global loadedDataDf
    #loadedDataDf = loadedDataDf.rename(columns={'Visa Permit Type Code': 'Visa_Permit_Type_Code'})

    for visa in visas:
            column = 'StateByVisaType_'
            if type(visa) is type(123):
                subData = loadedDataDf.query("Visa_Permit_Type_Code==%d" %(visa,))
            else:
                subData = loadedDataDf.query("Visa_Permit_Type_Code=='"+str(visa)+"'")
            GroupByVisasAndCountry = subData.groupby(["Visa_Permit_Type_Code","state_long","state_lati","state_longi"]).agg(['count',transLogOfxbylogxPlus1X,transLogOfxbylogxPlus1X10,transLogX])
            GroupByVisasAndCountry.columns = GroupByVisasAndCountry.columns.droplevel(0)
            print GroupByVisasAndCountry.ix[:,0:4]
            #print loadedDataDf.groupby(['country']).aggregate(np.count_nonzero)
            column = column+str(visa)
            saveCsv(column,GroupByVisasAndCountry.ix[:,0:4])
            #saveExcel(column,GroupByState.ix[:,0:4])
            
def saveExcel(column,groupedDataFrame):
    extStrtPos = re.search(".xlsx",FileName).start()
    #print extStrtPos
    # write the datafrmae to the new file to share with
    #outfileName = FileName[:extStrtPos]+"_GeoCoded"+FileName[extStrtPos:]
    outfileName ="temp_GeoCoded_"+column+FileName[extStrtPos:]
    writer = panda.ExcelWriter(path+outfileName)
    groupedDataFrame.to_excel(writer,'Sheet1') 
    writer.save()
    print "created the new file with the groupings"    
    
def saveCsv(column,groupedDataFrame):
    print "saving the file"
    #print extStrtPos
    # write the datafrmae to the new file to share with
    outfileName = path+column
    groupedDataFrame.to_csv(outfileName+'.csv', sep=',', encoding='utf-8')   

#do google geocoding here
def assignCountryGeoCodes(loadedTempDf):
    rowindex =0
    column='GroupByCountryResults'
    for row in loadedTempDf.itertuples():  
        #print row[country]
        g = geocoder.google(row[0])           
        loadedTempDf.ix[rowindex,country_lati] = g.lat
        loadedTempDf.ix[rowindex,country_longi] = g.lng
    saveCsv(column,loadedTempDf)
        
def openCreatedTempFile():
    extStrtPos = re.search(".xlsx",FileName).start()
    excelsheet = panda.ExcelFile(path+"temp_GeoCodedCountry"+FileName[extStrtPos:])
    print excelsheet.sheet_names
    print excelsheet.sheet_names[0]
    loadedTempDf = excelsheet.parse("Sheet1")
    print loadedDataDf.head()
    assignCountryGeoCodes(loadedTempDf)
    
setallIndexes()
groupByCountry()
groupByStates()
GroupByVisasAndStates()
GroupByVisasAndCountry()
EachCountryByVisaType()
EachStateByVisaType()