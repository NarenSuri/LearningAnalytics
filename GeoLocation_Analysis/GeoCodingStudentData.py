# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 15:02:15 2016

@author: Naren Suri
"""
"""
This code is created to GeoCode the states and countrys the students came from.
The analysis done on this page is dependent on the 
"""
# loading the data with pandas
import pandas as panda
import re
import geocoder
import numpy as np
import time
import sys

# load the excel sheet
path ="C:/Users/nsuri/Desktop/LearningAnalyticsDS/Data/source/"
FileName = "DataAnalyticsLearningProject_AnonymizedToShare.xlsx"
#FileName = "DataAnalyticsLearningProject_AnonymizedToShare_AnonymizedAndGeoCoded.xlsx"
excelsheet = panda.ExcelFile(path+FileName)
print excelsheet.sheet_names
print excelsheet.sheet_names[0]
loadedDataDf = excelsheet.parse("Sheet1")
#print loadedDataDf.head()
# The data has been loaded in to the dataFrame
#add the geocoding column
loadedDataDf['Adress For GeoCoding']=None
loadedDataDf['Latitide']=None
loadedDataDf['Longitude']=None
loadedDataDf['city']=None
loadedDataDf['country']=None
loadedDataDf['state']=None
loadedDataDf['country_lati']=None
loadedDataDf['country_longi']=None
loadedDataDf['state_lati']=None
loadedDataDf['state_longi']=None
loadedDataDf['state_long']=None

print type(loadedDataDf['Adress For GeoCoding'])

def saveObtainedGeoCodes():
    extStrtPos = re.search(".xlsx",FileName).start()
    #print extStrtPos
    # write the datafrmae to the new file to share with
    outfileName = FileName[:extStrtPos]+"_AnonymizedAndGeoCoded"+FileName[extStrtPos:]
    writer = panda.ExcelWriter(path+outfileName)
    loadedDataDf.to_excel(writer,'Sheet1')
    writer.save()
    print "created the new file with the geo-codes appended"
    
def setallIndexes(): 

    global city
    city  = loadedDataDf.columns.get_loc('city')
    global country
    country  = loadedDataDf.columns.get_loc('country')
    global country_lati
    country_lati  = loadedDataDf.columns.get_loc('country_lati')
    global country_longi
    country_longi  = loadedDataDf.columns.get_loc('country_longi')
    global state
    state  = loadedDataDf.columns.get_loc('state') 
    global state_lati
    state_lati  = loadedDataDf.columns.get_loc('state_lati')
    global state_longi
    state_longi  = loadedDataDf.columns.get_loc('state_longi')
    global Latitide
    Latitide = loadedDataDf.columns.get_loc('Latitide')
    global Longitude
    Longitude = loadedDataDf.columns.get_loc('Longitude')    
    global state_long
    state_long = loadedDataDf.columns.get_loc('state_long')
    global Adress_For_GeoCoding
    Adress_For_GeoCoding = loadedDataDf.columns.get_loc('Adress For GeoCoding')
    #print Adress_For_GeoCoding 
    
    
    global Visa_Permit_Type_Code
    Visa_Permit_Type_Code = loadedDataDf.columns.get_loc('Visa Permit Type Code')+1
    global Home_Address_Line1 
    Home_Address_Line1 = loadedDataDf.columns.get_loc('Home Address Line1')+1
    global Home_Address_Line2
    Home_Address_Line2=loadedDataDf.columns.get_loc('Home Address Line2')+ 1
    global Home_Address_Line3
    Home_Address_Line3=loadedDataDf.columns.get_loc('Home Address Line3')+ 1
    global Home_Address_City
    Home_Address_City=loadedDataDf.columns.get_loc('Home Address City')+ 1
    global Home_Address_County
    Home_Address_County=loadedDataDf.columns.get_loc('Home Address County')+ 1
    global Home_Address_IN_County_Code
    Home_Address_IN_County_Code=loadedDataDf.columns.get_loc('Home Address - IN County Code')+ 1
    global Home_Address_State_Code
    Home_Address_State_Code=loadedDataDf.columns.get_loc('Home Address State Code')+ 1
    global Home_Address_State_Name
    Home_Address_State_Name=loadedDataDf.columns.get_loc('Home Address State Name')+ 1
    global Home_Address_Zip_Code
    Home_Address_Zip_Code=loadedDataDf.columns.get_loc('Home Address Zip Code')+ 1
    global Home_Address_Country_Name
    Home_Address_Country_Name=loadedDataDf.columns.get_loc('Home Address Country Name')+ 1
    global Home_Address_Country_Code
    Home_Address_Country_Code=loadedDataDf.columns.get_loc('Home Address Country Code')+ 1
    global Mailing_Address_Line1 
    Mailing_Address_Line1=  loadedDataDf.columns.get_loc('Mailing Address Line1')+1	
    global Mailing_Address_Line2
    Mailing_Address_Line2= loadedDataDf.columns.get_loc('Mailing Address Line2')+1	
    global Mailing_Address_Line3
    Mailing_Address_Line3= loadedDataDf.columns.get_loc('Mailing Address Line3')+1	
    global Mailing_Address_Line4
    Mailing_Address_Line4= loadedDataDf.columns.get_loc('Mailing Address Line4')+1	
    global Mailing_Address_City
    Mailing_Address_City= loadedDataDf.columns.get_loc('Mailing Address City')+1
    global Mailing_Address_County	
    Mailing_Address_County	= loadedDataDf.columns.get_loc('Mailing Address County')+1	
    global Mailing_Address_IN_County_Code	
    Mailing_Address_IN_County_Code= loadedDataDf.columns.get_loc('Mailing Address - IN County Code')+1
    global Mailing_Address_State_Code
    Mailing_Address_State_Code= loadedDataDf.columns.get_loc('Mailing Address State Code')+1
    global Mailing_Address_State_Name
    Mailing_Address_State_Name= loadedDataDf.columns.get_loc('Mailing Address State Name')+1
    global Mailing_Address_Country_Code
    Mailing_Address_Country_Code= loadedDataDf.columns.get_loc('Mailing Address Country Code')+1
    global Mailing_Address_Country_Name
    Mailing_Address_Country_Name= loadedDataDf.columns.get_loc('Mailing Address Country Name')+1

# Set all columns indexes to save computing time
setallIndexes()

def OnelastTimeTryFillingMissedGeocodes(loadedDataDf):
    global OnelastTimeTryFillingMissedGeocodes
    OnelastTimeTryFillingMissedGeocodes=1
    print "entering in OnelastTimeTryFillingMissedGeocodes "
    index = loadedDataDf.index[loadedDataDf['Latitide'].isnull()]
    #print [index]
    for rowI in index:
        #print rowI,loadedDataDf.ix[rowI,Adress_For_GeoCoding]
        geocoding(rowI,Adress_For_GeoCoding,"")
        #loadedDataDf.ix[rowI,Latitide] = 1.01201
    OnelastTimeTryFillingMissedGeocodes=0
    print "tried filling mised codes for second time.."

    
def adressExtraction(text,mode):
     address=""
     if mode==0:
         if (str(text[Visa_Permit_Type_Code]) == "F-1" or str(text[Visa_Permit_Type_Code]) == "F-2"):    
             address= str(text[Home_Address_Line2])+","+str(text[Home_Address_Line3])+","+str(text[Home_Address_City])+","+str(text[Home_Address_County])+","+str(text[Home_Address_IN_County_Code])+","+str(text[Home_Address_State_Code])+","+str(text[Home_Address_State_Name])+","+str(text[Home_Address_Zip_Code])+","+str(text[Home_Address_Country_Name])+","+str(text[Home_Address_Country_Code])
         else:
             address= str(text[Mailing_Address_Line1])+","+str(text[Mailing_Address_Line2])+","+str(text[Mailing_Address_Line3])+","+str(text[Mailing_Address_Line4])+","+str(text[Mailing_Address_City])+","+str(text[Mailing_Address_County])+","+str(text[Mailing_Address_IN_County_Code])+","+str(text[Mailing_Address_State_Code])+","+str(text[Mailing_Address_State_Name])+","+str(text[Mailing_Address_Country_Code])+","+str(text[Mailing_Address_Country_Name])
     elif mode==1:
         if (str(text[Visa_Permit_Type_Code]) == "F-1" or str(text[Visa_Permit_Type_Code]) == "F-2"):    
             address= str(text[Home_Address_State_Name])+","+str(text[Home_Address_Zip_Code])+","+str(text[Home_Address_Country_Name])+","+str(text[Home_Address_Country_Code])
         else:
             address= str(text[Mailing_Address_State_Code])+","+str(text[Mailing_Address_State_Name])+","+str(text[Mailing_Address_Country_Code])+","+str(text[Mailing_Address_Country_Name])
    #################################################################################
     elif mode==2: ## Except visa is empty, all others are categorized according to their countries
         if (str(text[Visa_Permit_Type_Code]) == ""):    
             address= str(text[Home_Address_Line2])+","+str(text[Home_Address_Line3])+","+str(text[Home_Address_City])+","+str(text[Home_Address_County])+","+str(text[Home_Address_IN_County_Code])+","+str(text[Home_Address_State_Code])+","+str(text[Home_Address_State_Name])+","+str(text[Home_Address_Zip_Code])+","+str(text[Home_Address_Country_Name])+","+str(text[Home_Address_Country_Code])
         else:
             address= str(text[Mailing_Address_Line1])+","+str(text[Mailing_Address_Line2])+","+str(text[Mailing_Address_Line3])+","+str(text[Mailing_Address_Line4])+","+str(text[Mailing_Address_City])+","+str(text[Mailing_Address_County])+","+str(text[Mailing_Address_IN_County_Code])+","+str(text[Mailing_Address_State_Code])+","+str(text[Mailing_Address_State_Name])+","+str(text[Mailing_Address_Country_Code])+","+str(text[Mailing_Address_Country_Name])
     
     elif mode==3:
         if (str(text[Visa_Permit_Type_Code]) == ""):    
             address= str(text[Home_Address_State_Name])+","+str(text[Home_Address_Zip_Code])+","+str(text[Home_Address_Country_Name])+","+str(text[Home_Address_Country_Code])
         else:
             address= str(text[Mailing_Address_State_Code])+","+str(text[Mailing_Address_State_Name])+","+str(text[Mailing_Address_Country_Code])+","+str(text[Mailing_Address_Country_Name])
          
     else:
         print "There is a problem in Visa Selection mode"
     return address

#do google geocoding here
def geocoding(rowindex,Adress_For_GeoCoding,text):
    if text=="":
        text = loadedDataDf.ix[rowindex,Adress_For_GeoCoding]
    g = geocoder.google(loadedDataDf.ix[rowindex,Adress_For_GeoCoding])
    if not OnelastTimeTryFillingMissedGeocodes==1:
        if g.lat == None:
       
        #print 'checking nan'
            g = geocoder.google(adressExtraction(text,1))
        #print g.lat
            
    loadedDataDf.ix[rowindex,Latitide] = g.lat
    loadedDataDf.ix[rowindex,Longitude] = g.lng
    loadedDataDf.ix[rowindex,city] =g.city

    #country
    loadedDataDf.ix[rowindex,country] =g.country_long # country
    loadedDataDf.ix[rowindex,state] =g.state
    loadedDataDf.ix[rowindex,state_long] =g.state_long
    print rowindex
    #print state
    if loadedDataDf.ix[rowindex,state] is not None:        
        c = geocoder.google(loadedDataDf.ix[rowindex,country])
        loadedDataDf.ix[rowindex,country_lati] = c.lat
        loadedDataDf.ix[rowindex,country_longi] = c.lng
    
    if not ((loadedDataDf.ix[rowindex,state] is None)  or (loadedDataDf.ix[rowindex,country] is None)):
        s = geocoder.google(loadedDataDf.ix[rowindex,state]+","+loadedDataDf.ix[rowindex,country])
        loadedDataDf.ix[rowindex,state_lati] = s.lat
        loadedDataDf.ix[rowindex,state_longi] = s.lng
    
    

#Process each column for address extraction to send to geoCoder
def addressExtOnVisa(col):
    rowindex=0
    #call the generator that can fetch each row one by one
    for row in loadedDataDf.itertuples():
        #print row[loadedDataDf.columns.get_loc('Home Address Line1') + 1]
        #adressExtractionval=adressExtraction(row)
        #loadedDataDf.loc[rowindex][Adress_For_GeoCoding] = adressExtraction(row)
        loadedDataDf.ix[rowindex,Adress_For_GeoCoding] = re.sub(" ", ",", adressExtraction(row,0))
        time.sleep(1)
        geocoding(rowindex,Adress_For_GeoCoding,row)
        rowindex = rowindex+1
    OnelastTimeTryFillingMissedGeocodes(loadedDataDf)
    print loadedDataDf.isnull().sum()
        
        
# now lets handle the columns which we want to handle to update the columns with
    #loadedDataDf['Adress For GeoCoding'] =  loadedDataDf[col].map(adressExtraction)

#print (loadedDataDf.columns=='Home Address Line1').nonzero()
# check the visa column to choose between the different addresses in the data
loadedDataDf['Adress For GeoCoding']
addressExtOnVisa("Visa Permit Type Code")
saveObtainedGeoCodes()
#print loadedDataDf['Adress For GeoCoding']

#loadedDataDf['Home Address Line1']+","+loadedDataDf['Home Address Line2']+","+loadedDataDf['Home Address Line3']+","+loadedDataDf['Home Address City']+","+loadedDataDf['Home Address County']+","+loadedDataDf['Home Address - IN County Code']+","+loadedDataDf['Home Address State Code']+","+loadedDataDf['Home Address State Name']+","+loadedDataDf['Home Address Zip Code']+","+loadedDataDf['Home Address Country Name']+","+loadedDataDf['Home Address Country Code']+","
sys.modules[__name__].__dict__.clear()

