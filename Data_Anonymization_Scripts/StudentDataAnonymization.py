# -*- coding: utf-8 -*-
"""
Created on Thu Oct 06 13:49:50 2016

@author: nsuri
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# loading the data with pandas
import pandas as panda
import hashlib as cryptoService
import re as regex

# load the excel sheet
path = "C:/Users/nsuri/Desktop/"
FileName = "DiscussionsTopicsDataSourceForAnalysis.xlsx"
excelsheet = panda.ExcelFile(path+FileName)
print excelsheet.sheet_names
print excelsheet.sheet_names[0]
loadedDataDf = excelsheet.parse("DiscussionsTopicsDataSourceForA")
#print loadedDataDf.head()
# The data has been loaded in to the dataFrame

# create a lambda fucntion to proces the text
# implementing the md5 hash algorithm to secure the details
anonymizedData = lambda text: cryptoService.md5(str(text)).hexdigest()
def anonymizeData(col):
# now lets handle the columns which we want to handle to update the columns with
    loadedDataDf[col+' Crypted'] =  loadedDataDf[col].map(anonymizedData)
# list of columns To anonymize
colstoAnonymize = ['topic_id','user_id','name','created_at']
for col in colstoAnonymize:
    anonymizeData(col)
    
# Now delete all the columns with raw secret data
for delcol in colstoAnonymize:
    del loadedDataDf[delcol]
print "Sucessfully deleted all the columns those contins the private data"

extStrtPos = regex.search(".xlsx",FileName).start()
print extStrtPos
# write the datafrmae to the new file to share with
outfileName = FileName[:extStrtPos]+"_AnonymizedToShare"+FileName[extStrtPos:]
writer = panda.ExcelWriter(path+outfileName)
loadedDataDf.to_excel(writer,'Sheet1')
writer.save()
print "created the new file, youmay share it with Analyst/developer now"

'''
University ID	00000000000
Student Career Code	GRAD
	
	
Institution Code	IUBLA
	
Institution Description	Bloomington
Term Code	4168
Term Short Description	Fall 2016
	
Term Begin Date	8/22/2016
Term End Date	12/16/2016
Term Category Code	R
Term Category Short Description	Regular
	
Academic Year Code	2017
Withdraw Code	NWD
Withdraw Short Description	 
Withdraw Description	 
Withdraw Reason Code	 
Withdraw Reason Short Description	 
Withdraw Reason Description	 
Withdraw Date	 
Student Career Number	0
Primary Program Code	DSCI5
Primary Program Short Description	Grad Dsci
Primary Program Description	Data Science Graduate
Academic Load Indicator	N
Academic Load Short Description	No Units
Academic Load Description	No Unit Load
Projected Academic Level Code	GR
Projected Academic Level Short Description	Graduate
Projected Academic Level Description	Graduate
Academic Level Code - Start Term	GR
Academic Level Short Description - Start Term	Graduate
Academic Level Description - Start Term	Graduate
Academic Level Code - End Term	GR
Academic Level Short Description - End Term	Graduate
Academic Level Description - End Term	Graduate
Eligible To Enroll Indicator	Y
Tuition Calculation Timestamp	9/1/2016
Tuition Calc Required Indicator	N
Academic Standing Action Code	 
Academic Standing Status Code	 
Academic Standing Program Code	 
Academic Standing Short Description	 
Academic Standing Description	 
Last Date Attended	 
Study Agreement Code	 
Study Agreement Short Description	 
Study Agreement Description	 
Official Residency Code	NR
Official Residency Description	Nonresident Student
Student Academic Group Code	INFO
Academic Group Description	Sch of Informatics & Computing
Units Taken For GPA	0
Units Passed For GPA	0
Grade Points	0
Units Transferred	0
Total Term Units	0
Cumulative Grade Points	0
Current (Term) GPA	0
Units Taken For Progress	0
Cumulative GPA	0
Units Taken Not For GPA	0
Units Passed Not For GPA	0
Units In Progress For GPA	0
Units In Progress Not For GPA	0
Test Credit	0
Units Audited	6
Other Credit	0
Financial Aid Progress Units Taken	0
Cumulative Units Taken For GPA	0
Cumulative Units In Progress For GPA	0
Cumulative Units In Progress Not For GPA	0
Total Cumulative Units	0
IU Cumulative Units In Progress Not For GPA	0
IU Total Cumulative Units In Progress	0
IU Cumulative GPA	0
IU Term GPA	0
IU Grade Points	0
IU Cumulative Units Audited	6
IU Total Cumulative Units Earned	0
IU Cumulative Grade Points	0
IU Cumulative Units In Progress For GPA	0
IU Cumulative Units Passed For GPA	0
IU Cumulative Units Passed Not For GPA	0
IU Total Cumulative Units Passed	0
IU Cumulative Units Completed For GPA	0
IU Cumulative Units Completed Not For GPA	0
IU Total Cumulative Units Completed	0
IU Total Cumulative Test Credit	0
IU Cumulative External Transfer Units	0
IU Units Audited	6
IU Units In Progress For GPA	0
IU Units In Progress Not For GPA	0
IU Units Passed For GPA	0
IU Units Passed Not For GPA	0
IU Total Units Passed	0
IU Units Completed For GPA	0
IU Units Completed Not For GPA	0
IU Total Units Completed	0
IU Total Units Earned	0
IU Total Test Credit	0
IU External Transfer Units	0
Derived Enrollment Status	A
Career Sort Number	2
Derived Career Name	Graduate
Expanded Level Sort	2
Derived Expanded Level Name	Masters
Level Sort Number	2
Derived Level Name	Masters
IU Total Units Included in GPA (Term)	0
IU Total Units Included in GPA (Cumulative)	0
Primary Plan 1 Code	DATASCIMS1
Primary Plan 1 Description	Data Science MS
Primary Plan 1 Organization Code	BL-DSCI
Primary Plan 1 Organization Description	Data Science
ICHE CIP Primary Plan 1 Code	303001
ICHE CIP Primary Plan 1 Descriptioin	COMPUTATIONAL SCIENCE
IPEDS CIP Primary Plan 1 Code	303001
IPEDS CIP Primary Plan 1 Description	COMPUTATIONAL SCIENCE
IU CIP 2000 Primary Plan 1 Code	303001
IU CIP 2000 Primary Plan 1 Description	COMPUTATIONAL SCIENCE
Primary Plan 2 Code	 
Primary Plan 2 Description	 
Primary Plan 2 Organization Code	 
Primary Plan 2 Organization Description	 
ICHE CIP Primary Plan 2 Code	 
ICHE CIP Primary Plan 2 Description	 
IPEDS CIP Primary Plan 2 Code	 
IPEDS CIP Primary Plan 2 Description	 
IU CIP 2000 Primary Plan 2 Code	 
IU CIP 2000 Primary Plan 2 Description	 
Primary Plan 3 Code	 
Primary Plan 3 Description	 
Primary Plan 3 Organization Code	 
Primary Plan 3 Organization Description	 
ICHE CIP Primary Plan 3 Code	 
ICHE CIP Primary Plan 3 Description	 
IPEDS CIP Primary Plan 3 Code	 
IPEDS CIP Primary Plan 3 Description	 
IU CIP 2000 Primary Plan 3 Code	 
IU CIP 2000 Primary Plan 3 Description	 
Derived Total Term Units	0
Derived Total Term Units, including audit	6
Derived Current Term Indicator	Y
Official Tuition Residency Code	NR
Official Tuition Residency Description	Nonresident Student
Official Tuition Residency Exception Code	 
Admit Term Code	 
Admit Type Code	 
Admission County Code	 
Admission County Name	 
Admission State Code	 
Admission Zip Code	 
Student Term Create Date	8/15/2016
Derived Summer 1 Indicator	 
Derived Summer 1 Units	 
Derived Summer Session 1 audit hours for term.	 
Derived Summer 1 Description	 
Derived Summer 1 Load Ind	 
Derived Summer 2 Indicator	 
Derived Summer 2 Units	 
Derived Summer Session 2 audit hours for term.	 
Derived Summer 2 Description	 
Derived Summer 2 Load Ind	 
Current Admit Type	 
Current Admit Term	 
Use Row for Headcount	N
Projected Academic Level Override Indicator	N
Override All Academic Level	N
Override Maximum Units	N
Override Student Tuition Group	 
Tuition Residency Number	0
Override Initial Enrollment Fee	N
Override Initial Add Fee	N
STU_FEE_EXCL_EXST_IND	N
Last Term Attended	4168
Last Date Attended	12/16/2016
SATI Critical Reading Score	 
SATI Math Score	 
SATI Writing Score	 
ACT English Score	 
ACT Math Score	 
ACT Writing Score	 
ACT Composite Score	 
ACT Reading Score	 
ACT Science Score	 
ACT Combined English-Writing Score	 
ROW_USE_FOR_HDCT_SMMR_1_IND	 
ROW_USE_FOR_HDCT_SMMR_2_IND	 
ROW_USE_HDCT_UNDUPL_IND	N
ROW_USE_HDCT_UNDUPL_SMMR_1_IND	 
ROW_USE_HDCT_UNDUPL_SMMR_2_IND	 
HEALTH_IND	N
SOM_IND	N
Plan Distance Ed Indicator	N
High School Org ID	 
High School CEEB code	 
High School Name	 
High School Grad Date	 
High School Class Rank	 
High School Class Size	 
High School Rank Percentile	 
High School Cum GPA Cnvrted to 4-pt Scale	 
DIST_ED_TERM_UNT_NBR	 
High School Cum GPA Type	 
DIST_ED_SMMR_1_UNT_NBR	 
High School Cum GPA	 
DIST_ED_SMMR_2_UNT_NBR	 
PRSN_ADMT_CNTRY_CD	 
High School City	 
Min Term Units	0
High School County	 
High School State Code	 
High School Zip/Postal Code	 
High School Country Code	 
Primary Full Name	ABCD
Primary Prefix	 
Primary Suffix	 
Primary Last Name	AB
Primary First Name	CD
Primary Middle Name	 
Preferred Last Name	AB
Preferred Full Name	CD
Preferred Prefix	 
Preferred Suffix	 
Preferred First Name	AB
Preferred Middle Name	 
Gender Code	F
Gender Short Description	Female
Gender Description	Female
Marital Status Code	U
Marital Status Short Description	Unknown
Marital Status Description	Unknown
Date of Birth	10/18/1991
Birth Place Name	Aurangabad
Birth Country Code	IND
Birth State Code	MAHARA
Date of Death	 
FERPA Indicator	N
Primary Ethnic Code	4
Primary Ethnic Short Description	Asian
Primary Ethnic Description	Asian
Preferred Email Address	a@iu.edu
Primary Ethnic Detail Code	ASIAN
Primary Ethnic Detail Short Description	Asian
Primary Ethnic Detail Description	Asian
Campus-ID (SIDN)	 
Military Status Code	 
Military Status Short Description	 
Military Status Description	 
US Citizenship Status Code	4
US Citizenship Country Code	USA
US Citizenship Country Description	United States
2nd Ctitzenship Country Code	IND
2nd Citizenship Country Description	India
Campus Address Email ID	a@iu.edu
Disability Indicator	N
Other Email Address	a@iu.edu
GDS Campus Email Address	a@iu.edu
Network ID	ABCDEFG
FERPA Complete Restriction Indicator	N
FERPA Date of Birth Restriction Indicator	N
FERPA Campus Email Restriction Indicator	N
FERPA Marital Status Restriction Indicator	N
FERPA Other Email Restriction Indicator	N
FERPA Preferred Name Restriction Indicator	N
FERPA Primary Name Restriction Indicator	N
Visa Permit Type Code	L1
Derived Ethnic Code	6
Derived Ethnic Description	NR-Alien
Mailing Address Country Code	USA
Mailing Address Country Name	United States
Mailing Address City	Bloomington
Mailing Address County	Monroe
Mailing Address - IN County Code	53
Mailing Address State Code	IN
Mailing Address State Name	Indiana
Mailing Address Zip Code	47403
Mailing Phone Country Code	 
Mailing Address Phone Nbr	 
Mailing Phone Extension	 
Mailing Phone Preference Indicator	 
FERPA Mail Address Restriction Indicator	N
FERPA Mail Phone Restriction Indicator	N
Mailing Address House Type Code	 
Home Address Country Code	USA
Home Address Country Name	United States
Home Address City	Bloomington
Home Address County	Monroe
Home Address - IN County Code	53
Home Address State Code	IN
Home Address State Name	Indiana
Home Address Zip Code	47403
Home Phone Country Code	 
Home Phone Extension	 
Home Phone Preference Indicator	N
FERPA Home Address Restriction Indicator	N
FERPA Home Phone Restriction Indicator	N
Home Address House Type Code	 
Local Address Country Code	 
Local Address Country Name	 
Local Address Line 1	 
Local Address Line 2	 
Local Address Line 3	 
Local Address Line 4	 
Local Address City	 
Local Address County	 
Local Address - IN County Code	 
Local Address State Code	 
Local Address State Name	 
Local Address Zip Code	 
Local Phone Country Code	 
Local Address Phone Nbr	 
Local Phone Extension	 
Local Phone Preference Indicator	 
FERPA Local Address Restriction Indicator	N
FERPA Local Phone Restriction Indicator	N
Local Address House Type Code	 
FERPA Cell Phone Restriction Indicator	N
Academic Honors Diploma Indicator	 
Core 40 Indicator	 
Historical 21st Century Scholar indicator	 
21st Century Award Recipient Indicator	N
IR_FRST_GEN_IND	N
Former ACP Student Indicator	N
Reporting ICHE CIP  Plan 1 Code	303001
Reporting ICHE_CIP Plan 1 Desc	COMPUTATIONAL SCIENCE
Reporting IPEDS CIP  Plan 1 Code	303001
Reporting IPEDS_CIP Plan 1 Desc	COMPUTATIONAL SCIENCE
Reporting IU CIP Plan 1 Code	303001
Reporting IU CIP Plan 1 Desc	COMPUTATIONAL SCIENCE
Reporting ICHE CIP  Plan 2 Code	 
Reporting ICHE_CIP Plan 2 Desc	 
Reporting IPEDS CIP  Plan 2 Code	 
Reporting IU CIP Plan 2 Desc	 
Reporting ICHE CIP  Plan 3 Code	 
Reporting IPEDS_CIP Plan 2 Desc	 
Reporting ICHE_CIP Plan 3 Desc	 
Reporting IPEDS CIP  Plan 3 Code	 
Reporting IU CIP Plan 2 Code	 
Reporting IPEDS_CIP Plan 3 Desc	 
Reporting IU CIP Plan 3 Code	 
Reporting IU CIP Plan 3 Desc	 
PRSN_ETHNIC_DTL_WHT_IND	N
PRSN_ETHNIC_DTL_BLK_IND	N
PRSN_ETHNIC_DTL_HISP_IND	N
PRSN_ETHNIC_DTL_ASN_IND	Y
PRSN_ETHNIC_DTL_AMIN_IND	N
PRSN_ETHNIC_DTL_PCFC_ISLDR_IND	N
PRSN_ETHNIC_DTL_NONE_IND	N
PRSN_ETHNIC_VLDTD_IND	Y
PRSN_ETHNIC_HISP_IND	N
PRSN_DRVD_IPEDS_ETHNIC_CD	6
PRSN_DRVD_IPEDS_ETHNIC_DESC	NR-Alien
Online Plan Indicator 1	N
Online Plan Indicator 2	 
Online Plan Indicator 3	 
Distance Eduction Indicator(Student)	N
Distance Education Indicator-SS1 (Student)	N
Distance Education Indicator-SS2 (Student)	N
Derived Enroll Status Report Indicator	A
Student General Education Core Source Code	NR
Student General Education Core Institution	 
Bloomington Groups	 
Bloomington Groups Description	 
21st Century Participation	 
Bloomington Hudson Holland Scholars	 
Bloomington FASE Mentor	 
ACAD_PRM_SUB_PLAN_1_CD	 
ACAD_PRM_SUB_PLAN_1_DESC	 
ACAD_PRM_SUB_PLAN_2_CD	 
ACAD_PRM_SUB_PLAN_2_DESC	 
ACAD_PRM_SUB_PLAN_3_CD	 
ACAD_PRM_SUB_PLAN_3_DESC	 
STU_ACP_STDNT_IND	N
SAT Read/Writing Section Score	 
SAT Math Section Score	 
SAT Read/Writing Section Score - Agency	 
SAT Math Section Score - Agency	 
Derived SATI or Converted ACT Max Composite Score	 
Derived SATI or Converted ACT Max Composite Indicator	 
Derived SATI Composite Score - Math + Critical Reading	 
Derived ACT Composite Score - SAT Format	 
Derived SATI or Converted ACT Max Composite Score - Agency	 
Derived SATI or Converted ACT Max Composite Indicator - Agency	 
Derived SATI Composite Score - Math + Critical Reading - Agency	 
Derived ACT Composite Score - SAT Format - Agency	 
Derived 2017 SAT Composite	 
Derived 2017 SAT Source	 
Derived 2017 SAT Calc Composite	 
Derived 2017 ACT to SAT	 
Derived 2017 SAT Composite - Agency only	 
Derived 2017 SAT Source - Agency only	 
Derived 2017 SAT Calc Composite  - Agency only	 
Derived 2017 ACT to SAT  - Agency only	 
Derived Reporting SAT Composite	 
Derived Reporting SAT Source	 
Derived Reporting SAT Calc Composite	 
Derived Reporting ACT Composite Score - SAT Format	 
Derived Reporting SAT Composite - Agency only	 
Derived Reporting SAT Source - Agency only	 
Derived Reporting SAT Calc Composite - Agency only	 
Derived Reporting ACT Composite Score - SAT Format - Agency	 
'''
    