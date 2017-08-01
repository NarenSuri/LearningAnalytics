# -*- coding: utf-8 -*-
"""
Created on Thu Feb 02 13:31:36 2017

@author: nsuri
"""
########################################################################
#### Goal :
# Extract students by semester and see the transition of flow.
########################################################################
# loading the data with pandas


# loading the data with pandas
from AllFunctionsForDsAnalytics import AllFunctionsForDsAnalytics
import sys
import pandas as panda



#################################################################################################################################################################################################################################################################    

def createBinsForEachConsequtiveTerms(BinsToProcessNow,EnrolledClassData):
    print "Creating Bin for    " + str(BinsToProcessNow[0]) +"  -   "+str(BinsToProcessNow[1]) 
    BinOneAllData = EnrolledClassData.loc[EnrolledClassData['ACAD_TERM_CD']== BinsToProcessNow[0]]
    BinTwoAllData = EnrolledClassData.loc[EnrolledClassData['ACAD_TERM_CD']== BinsToProcessNow[1]]
    
    BinOne= BinOneAllData.ix[:,['PRSN_UNIV_ID Crypted','Course_Code']]
    BinTwo= BinTwoAllData.ix[:,['PRSN_UNIV_ID Crypted','Course_Code']]
    
    return(BinOne,BinTwo)    


def BinsOuterJoin(BinOne,BinTwo):       
       Bin1_Bin2_Outer12 = BinOne.merge(BinTwo, left_on='PRSN_UNIV_ID Crypted', right_on='PRSN_UNIV_ID Crypted', how='outer')
       Bin1_Bin2_Outer12 = Bin1_Bin2_Outer12.ix[(Bin1_Bin2_Outer12['PRSN_UNIV_ID Crypted'].notnull())&(Bin1_Bin2_Outer12['Course_Code_x'].notnull() )&( Bin1_Bin2_Outer12['Course_Code_y'].notnull() )]
       return(Bin1_Bin2_Outer12)
       
def JoinAllResultsAndSave(ResultSet,FileName1):
    print "About to save the results to the File"
    outfileName = path+FileName1
    #outfileName2 = path+FileName2
    ResultSet.to_csv(outfileName+'.csv', sep=',', encoding='utf-8')

####################################################################################################################################################################
DsFunctionsLib = AllFunctionsForDsAnalytics()
############################################################################################################################################################################################

# load the excel sheet
path ="C:/Users/nsuri/Desktop/LearningAnalyticsDS/Data/source/"
FileName = "DS_CRS_4140_AnonymizedToShare.xlsx"
#FileName = "DataAnalyticsLearningProject_AnonymizedToShare_AnonymizedAndGeoCoded.xlsx"
excelsheet = panda.ExcelFile(path+FileName)
print excelsheet.sheet_names
print excelsheet.sheet_names[0]
loadedDataDf = excelsheet.parse("Sheet1")

# select only the Enrolled classes by discarding the Dropped and WithDrawn Classes
# we may work on finding the pattern among dropped and withdrawn classes later ; but for now the analysis is focused only on Enrolled classes
EnrolledClassDataAll = loadedDataDf.ix[(loadedDataDf['PRSN_UNIV_ID Crypted'].notnull())&(loadedDataDf['ACAD_PRM_PGM_CD'].notnull() )&( loadedDataDf['ACAD_PRM_PLAN_1_CD'].notnull() )&( loadedDataDf['ACAD_GRP_CD'].notnull())&(loadedDataDf['ACAD_ORG_CD'].notnull())&(loadedDataDf['ACAD_TERM_CD'].notnull())&(loadedDataDf['CRS_SUBJ_CD'].notnull())&(loadedDataDf['CRS_CATLG_NBR'].notnull())&(loadedDataDf['CLS_NBR'].notnull())&(loadedDataDf['CLS_INSTR_NM'].notnull())&(loadedDataDf['CRS_CMPNT_CD'].notnull())&(loadedDataDf['STU_ENRL_STAT_CD']=='E')&(loadedDataDf['STU_DRVD_CLS_ENRL_STAT_IND']=='E')&(loadedDataDf['STU_DRV_ENRL_STAT_IND']=='E')&(loadedDataDf['CRS_CMPNT_CD']!='DIS')]
loadedDataDf = loadedDataDf[0:0]
# Got Enrolled Data with enrollment type of only enrolled

###############################################################
# now we have all the data that we need; But we should do an outer join on the data by semester and course
# so create a new column for each course name - as the name / number we have now is not suffinicient to maintain the unique nature in the data
# ACAD_TERM_CD CRS_SUBJ_CD	CRS_CATLG_NBR

## Process each record and put them in to the relevent semester bins
# some courses are topic courses, and these courses doesnt have any unique course number so please add such classes here and automatically class number will be added to such classes to uniquely define them
ClassNumbersToBeTakenCareOf = ['590','604','649','659']
# join the columns CRS_SUBJ_CD	CRS_CATLG_NBR
EnrolledClassDataAll ['Course_Code'] = EnrolledClassDataAll['ACAD_TERM_CD'].map(str)+"-"+ EnrolledClassDataAll['CRS_SUBJ_CD'].map(str)+EnrolledClassDataAll['CRS_CATLG_NBR'].map(str) + EnrolledClassDataAll.apply(lambda row: DsFunctionsLib.isAddClassNumber(str(row['CRS_CATLG_NBR']),str(row['CLS_NBR']),ClassNumbersToBeTakenCareOf),axis=1)
EnrolledClassDataAll ['Program_Started_In_Semester'] = None
EnrolledClassDataAll ['FinishedAtleast4Semesters'] = None
# Now lets create bins #SemOne #SemTwo #SemThree #SemFour

# Aggregate and create bins
# you should add here if you have more semesters in the data

# intensionally asked to give instead of using a set on the semester column of the data - also the order matters so human decision is better than automation here. Also i wanted to make sure that developer knows whats going in the script here.
#**** Order is important, so be careful  with the order you give here. 
CustomSortOrder = ['Spring 2014','Summer 2014','Fall 2014','Spring 2015','Summer 2015','Fall 2015','Spring 2016','Summer 2016','Fall 2016','Spring 2017','Summer 2017','Fall 2017']


# Create a dictionary and lets create the semister order for each student, beacuse not all stundents have fall as their first semester

PerStudentSemisterOrder = DsFunctionsLib.SemisterOrderOfaStudent(CustomSortOrder,EnrolledClassDataAll)
PerStudentSemisterOrder = DsFunctionsLib.SortPerStudentSemisterOrder(PerStudentSemisterOrder,CustomSortOrder)
########################################################### Now lets divide the data based on the semesters the students started their education#####################
# the students who started their education in the spring , fall and summer are to be seperated out
# take the complete data and make it into 3 pieces
#Crating 3 datasets
####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@############################
OnlyStudentsWith4SemestersModeSet=1
EnrolledClassDataAll = DsFunctionsLib.divideDataSetToThree(EnrolledClassDataAll,PerStudentSemisterOrder,OnlyStudentsWith4SemestersModeSet)
if OnlyStudentsWith4SemestersModeSet==1:
    EnrolledClassDataAll = EnrolledClassDataAll.loc[EnrolledClassDataAll['FinishedAtleast4Semesters']==1]
#########@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@############################
SemestersList=['Spring','Fall','Summer']
TypeOfProgram=['DSCI9','DSCI5']
EnrolledClassData = None
BinOne = None
BinTwo = None
Bin1_Bin2_Outer12 = None

ResultSet = panda.DataFrame(columns=['PRSN_UNIV_ID Crypted', 'Course_Code_x','Course_Code_y'])
for OnlineOrResendential in TypeOfProgram:
    if OnlineOrResendential == 'DSCI9':
        programTypeIs = 'Online'
    elif OnlineOrResendential == 'DSCI5':
        programTypeIs = 'Resedential'
    else:
        programTypeIs = 'UnKnown'

    if EnrolledClassData is not None:
        EnrolledClassData = EnrolledClassData[0:0]
         
    EnrolledClassData = EnrolledClassDataAll.loc[(EnrolledClassDataAll['ACAD_PRM_PGM_CD']== OnlineOrResendential)]
        ########################################################## With Semesters Info #################################################################################
    for i in range(len(CustomSortOrder)-1):  
        BinsToProcessNow =(CustomSortOrder[i],CustomSortOrder[i+1]) 
        BinOne,BinTwo = createBinsForEachConsequtiveTerms(BinsToProcessNow,EnrolledClassData)
        Bin1_Bin2_Outer12 = BinsOuterJoin(BinOne,BinTwo)
        ResultSet = ResultSet.append(Bin1_Bin2_Outer12,ignore_index=True)
        
        if BinOne is not None:
            BinOne = BinOne[0:0]
            BinTwo = BinTwo[0:0]
            Bin1_Bin2_Outer12 = Bin1_Bin2_Outer12[0:0]
            

    JoinAllResultsAndSave(ResultSet,programTypeIs+"-EvolutionOfCoursesDS")
        
sys.modules[__name__].__dict__.clear()