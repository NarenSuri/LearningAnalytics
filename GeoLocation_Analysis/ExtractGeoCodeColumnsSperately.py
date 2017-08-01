# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 18:47:30 2016

@author: nsuri
"""

# Extract particular columns from the finally created geo-coded excel file

# loading the data with pandas
import pandas as panda
import re
import geocoder
import time
import numpy as np
import sys

# load the excel sheet
path ="C:/Users/nsuri/Desktop/LearningAnalyticsDS/Data/workspace/"
FileName = "DataAnalyticsLearningProject_AnonymizedToShare_AnonymizedAndGeoCoded.xlsx"
excelsheet = panda.ExcelFile(path+FileName)
print excelsheet.sheet_names
print excelsheet.sheet_names[0]
loadedDataDf = excelsheet.parse("Sheet1")
print loadedDataDf.head()
# The data has been loaded in to the dataFrame

global loadedDataDf
global prunedDf


def setallIndexes(): 
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
    global state_long
    state_long = loadedDataDf.columns.get_loc('state_long')+1

   
def saveDataPruned(prunedDf):
    extStrtPos = re.search(".xlsx",FileName).start()
    #print extStrtPos
    # write the datafrmae to the new file to share with
    outfileName = FileName[:extStrtPos]+"_GeoCoded"+FileName[extStrtPos:]
    outfileName ="StudentData_GeoCodedFinal"+FileName[extStrtPos:]
    writer = panda.ExcelWriter(path+outfileName)
    prunedDf[['University ID Crypted','Term Code','Term Short Description','Term Category Code','Academic Year Code','Withdraw Short Description','Last Date Attended','Official Residency Code','Admit Term Code','Admit Type Code','Student Term Create Date','Current Admit Type','Current Admit Term','Last Date Attended.1','Gender Code','Visa Permit Type Code','Adress For GeoCoding','Latitide','Longitude','city','country','state','country_lati','country_longi','state_lati','state_longi','state_long']].to_excel(writer,'Sheet1') 
    writer.save()
    print "created the new file with the geo-codes appended"
    
# Set all columns indexes to save computing time
setallIndexes()

def RemoveAllNansInDF(loadedDataDf):
    #prunedDf = loadedDataDf.ix[ : ,Latitide:Longitude].dropna()
    prunedDf = loadedDataDf[loadedDataDf['Latitide'].notnull() & loadedDataDf['Longitude'].notnull() & loadedDataDf['country'].notnull()]
   #prunedDf = loadedDataDf.dropna(axis=1)
    #print prunedDf
    print type(prunedDf)
    print "Filtered all null values"
    return prunedDf
    
prunedDf = RemoveAllNansInDF(loadedDataDf)
#print loadedDataDf.ix[:,Latitide:Longitude].isnull().sum()
saveDataPruned(prunedDf)
print " Done with exporting and purging data"
    
sys.modules[__name__].__dict__.clear()
