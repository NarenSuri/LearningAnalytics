# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 15:56:22 2017

@author: nsuri
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 17:22:28 2016

@author: nsuri
"""
import sys
sys.modules[__name__].__dict__.clear()
# loading the data with pandas
import pandas as panda
import sys


def SemisterOrderOfaStudent(CustomSortOrder,EnrolledClassData):
    PerStudentSemisterOrder={}
    for row in EnrolledClassData.itertuples():
        if(PerStudentSemisterOrder.has_key(row[EnrolledClassData.columns.get_loc('PRSN_UNIV_ID Crypted')+1])):
            if(row[EnrolledClassData.columns.get_loc('ACAD_TERM_CD')+1] in PerStudentSemisterOrder[row[EnrolledClassData.columns.get_loc('PRSN_UNIV_ID Crypted')+1]]):
                pass
            else:
                PerStudentSemisterOrder[row[EnrolledClassData.columns.get_loc('PRSN_UNIV_ID Crypted')+1]].append(row[EnrolledClassData.columns.get_loc('ACAD_TERM_CD')+1])
        else:
            PerStudentSemisterOrder[row[EnrolledClassData.columns.get_loc('PRSN_UNIV_ID Crypted')+1]]=[row[EnrolledClassData.columns.get_loc('ACAD_TERM_CD')+1]]
    return(PerStudentSemisterOrder)

def SortPerStudentSemisterOrder(PerStudentSemisterOrder,CustomSortOrder):
    for key,Currentvalues in PerStudentSemisterOrder.iteritems():
        SortedListOfCurrentStudnet =CustomSortOrder
        disjuntValues =  list(set(SortedListOfCurrentStudnet).difference(set(Currentvalues)))
        #print disjuntValues
        FinalVals = [val for val in SortedListOfCurrentStudnet if val not in disjuntValues] #SortedListOfCurrentStudnet.remove(disjuntValues)
        #disjuntValues.remove(SortedListOfCurrentStudnet)
        PerStudentSemisterOrder[key] = FinalVals
    return(PerStudentSemisterOrder)

def insertIntoCoursesTakenInSequence(row,Index,CoursesTakenInSequence,columns,EnrolledClassData):
     # check if the dataframe already has that paricular student in it
     #print row[EnrolledClassData.columns.get_loc('PRSN_UNIV_ID Crypted')+1]
     #print CoursesTakenInSequence['PRSN_UNIV_ID Crypted']
     if any( CoursesTakenInSequence['PRSN_UNIV_ID Crypted'] == row[EnrolledClassData.columns.get_loc('PRSN_UNIV_ID Crypted')+1]):         
         rowindex = CoursesTakenInSequence.loc[row[EnrolledClassData.columns.get_loc('PRSN_UNIV_ID Crypted')+1]==CoursesTakenInSequence['PRSN_UNIV_ID Crypted']].index.tolist()         
         CoursesTakenInSequence.ix[rowindex[0],columns[Index]] = row[EnrolledClassData.columns.get_loc('Course_Code')+1]
     else:         
         CoursesTakenInSequence.loc[CoursesTakenInSequence.shape[0]+1] = [row[EnrolledClassData.columns.get_loc('PRSN_UNIV_ID Crypted')+1]]+[0] * 16
         rowindex = CoursesTakenInSequence.loc[row[EnrolledClassData.columns.get_loc('PRSN_UNIV_ID Crypted')+1]==CoursesTakenInSequence['PRSN_UNIV_ID Crypted']].index.tolist()         
         CoursesTakenInSequence.ix[rowindex[0],columns[Index]] = row[EnrolledClassData.columns.get_loc('Course_Code')+1]

def StudentsCourseSemisterBins(EnrolledClassData,PerStudentSemisterOrder,mode):
    SemOne = panda.DataFrame(columns=['PRSN_UNIV_ID Crypted', 'Course_Code'])
    SemTwo = panda.DataFrame(columns=['PRSN_UNIV_ID Crypted', 'Course_Code'])
    SemThree = panda.DataFrame(columns=['PRSN_UNIV_ID Crypted', 'Course_Code'])
    SemFour = panda.DataFrame(columns=['PRSN_UNIV_ID Crypted', 'Course_Code'])   
    Dfcolumns=['PRSN_UNIV_ID Crypted', 'Gender','Semester1','Semester2','Semester3','Semester4','Semester5','Semester6','Semester7','Semester8','Semester9','Semester10','Semester11','Semester12','Semester13','Semester14','Semester15'] 
    CoursesTakenInSequence = panda.DataFrame(columns=Dfcolumns)

    if mode==0:        
        for row in EnrolledClassData.itertuples():
            Index = (PerStudentSemisterOrder[row[EnrolledClassData.columns.get_loc('PRSN_UNIV_ID Crypted')+1]].index(row[EnrolledClassData.columns.get_loc('ACAD_TERM_CD')+1]) )+1
            insertIntoCoursesTakenInSequence(row,Index,CoursesTakenInSequence,Dfcolumns,EnrolledClassData)               
            binIndex =  (Index % 4)        
            if(binIndex == 1):
                SemOne.loc[SemOne.shape[0]+1] = [row[EnrolledClassData.columns.get_loc('PRSN_UNIV_ID Crypted')+1] , 'Sem1-' + row[EnrolledClassData.columns.get_loc('Course_Code')+1]] 
            elif(binIndex == 2):
                SemTwo.loc[SemTwo.shape[0]+1] = [row[EnrolledClassData.columns.get_loc('PRSN_UNIV_ID Crypted')+1] , 'Sem2-'+ row[EnrolledClassData.columns.get_loc('Course_Code')+1]]
            elif(binIndex == 3):
                SemThree.loc[SemThree.shape[0]+1] = [row[EnrolledClassData.columns.get_loc('PRSN_UNIV_ID Crypted')+1] , 'Sem3-' + row[EnrolledClassData.columns.get_loc('Course_Code')+1]]
            else:
                SemFour.loc[SemFour.shape[0]+1] = [row[EnrolledClassData.columns.get_loc('PRSN_UNIV_ID Crypted')+1] , 'Sem4-' +row[EnrolledClassData.columns.get_loc('Course_Code')+1]]
    elif mode==1:        
        for row in EnrolledClassData.itertuples():
            Index = (PerStudentSemisterOrder[row[EnrolledClassData.columns.get_loc('PRSN_UNIV_ID Crypted')+1]].index(row[EnrolledClassData.columns.get_loc('ACAD_TERM_CD')+1]) )+1
            insertIntoCoursesTakenInSequence(row,Index,CoursesTakenInSequence,Dfcolumns,EnrolledClassData)              
            binIndex =  (Index % 4)        
            if(binIndex == 1):
                SemOne.loc[SemOne.shape[0]+1] = [row[EnrolledClassData.columns.get_loc('PRSN_UNIV_ID Crypted')+1] , row[EnrolledClassData.columns.get_loc('Course_Code')+1]] 
            elif(binIndex == 2):
                SemTwo.loc[SemTwo.shape[0]+1] = [row[EnrolledClassData.columns.get_loc('PRSN_UNIV_ID Crypted')+1] ,  row[EnrolledClassData.columns.get_loc('Course_Code')+1]]
            elif(binIndex == 3):
                SemThree.loc[SemThree.shape[0]+1] = [row[EnrolledClassData.columns.get_loc('PRSN_UNIV_ID Crypted')+1] , row[EnrolledClassData.columns.get_loc('Course_Code')+1]]
            else:
                SemFour.loc[SemFour.shape[0]+1] = [row[EnrolledClassData.columns.get_loc('PRSN_UNIV_ID Crypted')+1] , row[EnrolledClassData.columns.get_loc('Course_Code')+1]]
    else:
        print "Please check the mode of semester level binning"
        
    return(SemOne,SemTwo,SemThree,SemFour,CoursesTakenInSequence)
            
def SequenceOfCoursesTaken(SemOne,SemTwo,SemThree,SemFour):
   
    Sem1_Sem2_Outer12 = SemOne.merge(SemTwo, left_on='PRSN_UNIV_ID Crypted', right_on='PRSN_UNIV_ID Crypted', how='outer')
    Sem1_Sem2_Outer = Sem1_Sem2_Outer12.ix[(Sem1_Sem2_Outer12['PRSN_UNIV_ID Crypted'].notnull())&(Sem1_Sem2_Outer12['Course_Code_x'].notnull() )&( Sem1_Sem2_Outer12['Course_Code_y'].notnull() )]
   
    Sem2_Sem3_Outer23 = SemTwo.merge(SemThree, left_on='PRSN_UNIV_ID Crypted', right_on='PRSN_UNIV_ID Crypted', how='outer')
    Sem2_Sem3_Outer = Sem2_Sem3_Outer23.ix[(Sem2_Sem3_Outer23['PRSN_UNIV_ID Crypted'].notnull())&(Sem2_Sem3_Outer23['Course_Code_x'].notnull() )&( Sem2_Sem3_Outer23['Course_Code_y'].notnull() )]
   
    Sem3_Sem4_Outer34 = SemThree.merge(SemFour, left_on='PRSN_UNIV_ID Crypted', right_on='PRSN_UNIV_ID Crypted', how='outer')
    Sem3_Sem4_Outer = Sem3_Sem4_Outer34.ix[(Sem3_Sem4_Outer34['PRSN_UNIV_ID Crypted'].notnull())&(Sem3_Sem4_Outer34['Course_Code_x'].notnull() )&( Sem3_Sem4_Outer34['Course_Code_y'].notnull() )]
   
    return(Sem1_Sem2_Outer,Sem2_Sem3_Outer,Sem3_Sem4_Outer)

def JoinAllResultsAndSave(Sem1_Sem2_Outer,Sem2_Sem3_Outer,Sem3_Sem4_Outer,path,CoursesTakenInSequence,FileName1,FileName2):
    print "About to save the results to the File"
    outfileName = path+FileName1
    #outfileName2 = path+FileName2
    FinalResult = panda.concat([Sem1_Sem2_Outer, Sem2_Sem3_Outer,Sem3_Sem4_Outer], ignore_index=True)
    FinalResult.to_csv(outfileName+'.csv', sep=',', encoding='utf-8')     
    
    FinalResultToUse = panda.concat([Sem1_Sem2_Outer.ix[:,1:3], Sem2_Sem3_Outer.ix[:,1:3],Sem3_Sem4_Outer.ix[:,1:3]], ignore_index=True)
    FinalResultToUse.to_csv(outfileName+'_ToUse.csv', sep=',', encoding='utf-8')   
    #CoursesTakenInSequence.to_csv(outfileName2+'_ToUse.csv', sep=',', encoding='utf-8') 

# used for chedking if that particular class number is to be taken care    
def isAddClassNumber(courseCatalogue,classnumber,ClassNumbersToBeTakenCareOf):
    #print courseCatalogue
    if courseCatalogue in ClassNumbersToBeTakenCareOf:
        return("-"+classnumber)
    else:
        return("")


def divideDataSetToThree(EnrolledClassDataAll,PerStudentSemisterOrder,OnlyStudentsWith4SemestersModeSet):
    # creating a column in the EnrolledClassDataAll that specifies the new column with the studnet info on when the student started his education? like in spring, summer or Fall
    for row in EnrolledClassDataAll.itertuples():
        SemStarted = (PerStudentSemisterOrder[row[EnrolledClassDataAll.columns.get_loc('PRSN_UNIV_ID Crypted')+1]][0])
        if row[EnrolledClassDataAll.columns.get_loc('Program_Started_In_Semester')+1] is None:            
            if('Spring'.lower() in SemStarted.lower()):
                # update the row to Spring
                EnrolledClassDataAll.loc[EnrolledClassDataAll['PRSN_UNIV_ID Crypted']==row[EnrolledClassDataAll.columns.get_loc('PRSN_UNIV_ID Crypted')+1],'Program_Started_In_Semester']='Spring'
            elif('Summer'.lower() in SemStarted.lower()):
                EnrolledClassDataAll.loc[EnrolledClassDataAll['PRSN_UNIV_ID Crypted']==row[EnrolledClassDataAll.columns.get_loc('PRSN_UNIV_ID Crypted')+1],'Program_Started_In_Semester']='Summer'
            elif('Fall'.lower() in SemStarted.lower()):
                EnrolledClassDataAll.loc[EnrolledClassDataAll['PRSN_UNIV_ID Crypted']==row[EnrolledClassDataAll.columns.get_loc('PRSN_UNIV_ID Crypted')+1],'Program_Started_In_Semester']='Fall'
            else:
                EnrolledClassDataAll.loc[EnrolledClassDataAll['PRSN_UNIV_ID Crypted']==row[EnrolledClassDataAll.columns.get_loc('PRSN_UNIV_ID Crypted')+1],'Program_Started_In_Semester']='NA'
                
            if OnlyStudentsWith4SemestersModeSet == 1:
                if len(PerStudentSemisterOrder[row[EnrolledClassDataAll.columns.get_loc('PRSN_UNIV_ID Crypted')+1]])>=4:
                   EnrolledClassDataAll.loc[EnrolledClassDataAll['PRSN_UNIV_ID Crypted']==row[EnrolledClassDataAll.columns.get_loc('PRSN_UNIV_ID Crypted')+1],'FinishedAtleast4Semesters']=1
                else:
                   EnrolledClassDataAll.loc[EnrolledClassDataAll['PRSN_UNIV_ID Crypted']==row[EnrolledClassDataAll.columns.get_loc('PRSN_UNIV_ID Crypted')+1],'FinishedAtleast4Semesters']=0  
                
    return(EnrolledClassDataAll)

#################################################################################################################################################################################################################################################################    

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
EnrolledClassDataAll ['Course_Code'] = EnrolledClassDataAll['CRS_SUBJ_CD'].map(str)+EnrolledClassDataAll['CRS_CATLG_NBR'].map(str) + EnrolledClassDataAll.apply(lambda row: isAddClassNumber(str(row['CRS_CATLG_NBR']),str(row['CLS_NBR']),ClassNumbersToBeTakenCareOf),axis=1)
EnrolledClassDataAll ['Program_Started_In_Semester'] = None
EnrolledClassDataAll ['FinishedAtleast4Semesters'] = None
# Now lets create bins #SemOne #SemTwo #SemThree #SemFour

# Aggregate and create bins
# you should add here if you have more semesters in the data

# intensionally asked to give instead of using a set on the semester column of the data - also the order matters so human decision is better than automation here. Also i wanted to make sure that developer knows whats going in the script here.
#**** Order is important, so be careful  with the order you give here. 
CustomSortOrder = ['Spring 2014','Summer 2014','Fall 2014','Spring 2015','Summer 2015','Fall 2015','Spring 2016','Summer 2016','Fall 2016','Spring 2017','Summer 2017','Fall 2017']


# Create a dictionary and lets create the semister order for each student, beacuse not all stundents have fall as their first semester

PerStudentSemisterOrder = SemisterOrderOfaStudent(CustomSortOrder,EnrolledClassDataAll)
PerStudentSemisterOrder = SortPerStudentSemisterOrder(PerStudentSemisterOrder,CustomSortOrder)
########################################################### Now lets divide the data based on the semesters the students started their education#####################
# the students who started their education in the spring , fall and summer are to be seperated out
# take the complete data and make it into 3 pieces
#Crating 3 datasets
####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@############################
OnlyStudentsWith4SemestersModeSet=1
EnrolledClassDataAll = divideDataSetToThree(EnrolledClassDataAll,PerStudentSemisterOrder,OnlyStudentsWith4SemestersModeSet)
if OnlyStudentsWith4SemestersModeSet==1:
    EnrolledClassDataAll = EnrolledClassDataAll.loc[EnrolledClassDataAll['FinishedAtleast4Semesters']==1]
#########@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@############################
SemestersList=['Spring','Fall','Summer']
TypeOfProgram=['DSCI9','DSCI5']
EnrolledClassData = None
SemOne = None
SemTwo = None
SemFour = None
SemThree = None
CoursesTakenInSequence = None
Sem1_Sem2_Outer = None
Sem2_Sem3_Outer = None
Sem3_Sem4_Outer = None
Sem1_Sem2_Outer12 = None
Sem2_Sem3_Outer23 = None
Sem3_Sem4_Outer34 = None

for Term in SemestersList:
    for OnlineOrResendential in TypeOfProgram:
        if OnlineOrResendential == 'DSCI9':
            programTypeIs = 'Online'
        elif OnlineOrResendential == 'DSCI5':
            programTypeIs = 'Resedential'
        else:
            programTypeIs = 'UnKnown'

        if EnrolledClassData is not None:
            EnrolledClassData = EnrolledClassData[0:0]
         
        EnrolledClassData = EnrolledClassDataAll.loc[(EnrolledClassDataAll['Program_Started_In_Semester']== Term) & (EnrolledClassDataAll['ACAD_PRM_PGM_CD']== OnlineOrResendential)]
        ########################################################## With Semesters Info #################################################################################
        ## Now create the 4 semister bins
        if SemOne is not None:
            SemOne = SemOne[0:0]
            SemTwo = SemTwo[0:0]
            SemThree = SemThree[0:0]
            SemFour = SemFour[0:0]
            CoursesTakenInSequence = CoursesTakenInSequence[0:0]
            Sem1_Sem2_Outer = Sem1_Sem2_Outer[0:0]
            Sem2_Sem3_Outer = Sem2_Sem3_Outer[0:0]
            Sem3_Sem4_Outer = Sem3_Sem4_Outer[0:0]
            

          
        SemOne,SemTwo,SemThree,SemFour,CoursesTakenInSequence = StudentsCourseSemisterBins(EnrolledClassData,PerStudentSemisterOrder,mode=0)
        # Now lets do the outer merge by semisters           
        Sem1_Sem2_Outer,Sem2_Sem3_Outer,Sem3_Sem4_Outer = SequenceOfCoursesTaken(SemOne,SemTwo,SemThree,SemFour)
        # Now we need to aggregate by number of times a course taken in a particular semister taken
        JoinAllResultsAndSave(Sem1_Sem2_Outer,Sem2_Sem3_Outer,Sem3_Sem4_Outer,path,CoursesTakenInSequence,FileName1=programTypeIs+"_"+Term+"_FlowOfCoursesEnrollment_WithSemestes",FileName2=programTypeIs+"_"+Term+"_CoursesTakenInSequence")
        ########################################################## With Out Semesters Info #################################################################################
        ## Now create the 4 semister bins
        if SemOne is not None:
            SemOne = SemOne[0:0]
            SemTwo = SemTwo[0:0]
            SemThree = SemThree[0:0]
            SemFour = SemFour[0:0]
            CoursesTakenInSequence = CoursesTakenInSequence[0:0]
            Sem1_Sem2_Outer = Sem1_Sem2_Outer[0:0]
            Sem2_Sem3_Outer = Sem2_Sem3_Outer[0:0]
            Sem3_Sem4_Outer = Sem3_Sem4_Outer[0:0]


        
        SemOne,SemTwo,SemThree,SemFour,CoursesTakenInSequence = StudentsCourseSemisterBins(EnrolledClassData,PerStudentSemisterOrder,mode=1)
        # Now lets do the outer merge by semisters
        Sem1_Sem2_Outer,Sem2_Sem3_Outer,Sem3_Sem4_Outer = SequenceOfCoursesTaken(SemOne,SemTwo,SemThree,SemFour)
        # Now we need to aggregate by number of times a course taken in a particular semister taken
        JoinAllResultsAndSave(Sem1_Sem2_Outer,Sem2_Sem3_Outer,Sem3_Sem4_Outer,path,CoursesTakenInSequence,FileName1=programTypeIs+"_"+Term+"_FlowOfCoursesEnrollment_WithOutSemesterDisctinction",FileName2=programTypeIs+"_"+Term+"_CoursesTakenInSequence")
sys.modules[__name__].__dict__.clear()