# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 18:09:07 2016

@author: nsuri
"""

# loading the data with pandas
import pandas as panda


# load the excel sheet
path ="C:/Users/nsuri/Desktop/LearningAnalyticsDS/Data/source/"
FileName = "FlowOfCoursesEnrollmentWithSemestes.xlsx"

excelsheet = panda.ExcelFile(path+FileName)
print excelsheet.sheet_names
print excelsheet.sheet_names[0]
loadedDataDf = excelsheet.parse("FlowOfCoursesEnrollmentWithSeme")

# we may work on finding the pattern among dropped and withdrawn classes later ; but for now the analysis is focused only on Enrolled classes
EnrolledClassData = loadedDataDf.ix[(loadedDataDf['PRSN_UNIV_ID Crypted'].notnull())&(loadedDataDf['ACAD_PRM_PGM_CD'].notnull() )&( loadedDataDf['ACAD_PRM_PLAN_1_CD'].notnull() )&( loadedDataDf['ACAD_GRP_CD'].notnull())&(loadedDataDf['ACAD_ORG_CD'].notnull())&(loadedDataDf['ACAD_TERM_CD'].notnull())&(loadedDataDf['CRS_SUBJ_CD'].notnull())&(loadedDataDf['CRS_CATLG_NBR'].notnull())&(loadedDataDf['CLS_NBR'].notnull())&(loadedDataDf['CLS_INSTR_NM'].notnull())&(loadedDataDf['CRS_CMPNT_CD'].notnull())&(loadedDataDf['STU_ENRL_STAT_CD']=='E')&(loadedDataDf['STU_DRVD_CLS_ENRL_STAT_IND']=='E')&(loadedDataDf['STU_DRV_ENRL_STAT_IND']=='E')&(loadedDataDf['CRS_CMPNT_CD']!='DIS')]

# Enrolled Data with enrollment type of only enrolled
