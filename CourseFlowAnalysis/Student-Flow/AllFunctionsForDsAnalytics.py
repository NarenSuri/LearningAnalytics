    # -*- coding: utf-8 -*-
"""
Created on Thu Feb 02 20:17:11 2017
    
@author: nsuri
"""
import pandas as panda


class AllFunctionsForDsAnalytics:
    
    def SemisterOrderOfaStudent(self,CustomSortOrder,EnrolledClassData):
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
    
    def SortPerStudentSemisterOrder(self,PerStudentSemisterOrder,CustomSortOrder):
        for key,Currentvalues in PerStudentSemisterOrder.iteritems():
            SortedListOfCurrentStudnet =CustomSortOrder
            disjuntValues =  list(set(SortedListOfCurrentStudnet).difference(set(Currentvalues)))
            #print disjuntValues
            FinalVals = [val for val in SortedListOfCurrentStudnet if val not in disjuntValues] #SortedListOfCurrentStudnet.remove(disjuntValues)
            #disjuntValues.remove(SortedListOfCurrentStudnet)
            PerStudentSemisterOrder[key] = FinalVals
        return(PerStudentSemisterOrder)
    
    def insertIntoCoursesTakenInSequence(self,row,Index,CoursesTakenInSequence,columns,EnrolledClassData):
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
    
    def StudentsCourseSemisterBins(self,EnrolledClassData,PerStudentSemisterOrder,mode):
        SemOne = panda.DataFrame(columns=['PRSN_UNIV_ID Crypted', 'Course_Code'])
        SemTwo = panda.DataFrame(columns=['PRSN_UNIV_ID Crypted', 'Course_Code'])
        SemThree = panda.DataFrame(columns=['PRSN_UNIV_ID Crypted', 'Course_Code'])
        SemFour = panda.DataFrame(columns=['PRSN_UNIV_ID Crypted', 'Course_Code'])   
        Dfcolumns=['PRSN_UNIV_ID Crypted', 'Gender','Semester1','Semester2','Semester3','Semester4','Semester5','Semester6','Semester7','Semester8','Semester9','Semester10','Semester11','Semester12','Semester13','Semester14','Semester15'] 
        CoursesTakenInSequence = panda.DataFrame(columns=Dfcolumns)
    
        if mode==0:        
            for row in EnrolledClassData.itertuples():
                Index = (PerStudentSemisterOrder[row[EnrolledClassData.columns.get_loc('PRSN_UNIV_ID Crypted')+1]].index(row[EnrolledClassData.columns.get_loc('ACAD_TERM_CD')+1]) )+1
                self.insertIntoCoursesTakenInSequence(row,Index,CoursesTakenInSequence,Dfcolumns,EnrolledClassData)               
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
                self.insertIntoCoursesTakenInSequence(row,Index,CoursesTakenInSequence,Dfcolumns,EnrolledClassData)              
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
            print ("Please check the mode of semester level binning")
            
        return(SemOne,SemTwo,SemThree,SemFour,CoursesTakenInSequence)
                
    def SequenceOfCoursesTaken(self,SemOne,SemTwo,SemThree,SemFour):
       
        Sem1_Sem2_Outer12 = SemOne.merge(SemTwo, left_on='PRSN_UNIV_ID Crypted', right_on='PRSN_UNIV_ID Crypted', how='outer')
        Sem1_Sem2_Outer = Sem1_Sem2_Outer12.ix[(Sem1_Sem2_Outer12['PRSN_UNIV_ID Crypted'].notnull())&(Sem1_Sem2_Outer12['Course_Code_x'].notnull() )&( Sem1_Sem2_Outer12['Course_Code_y'].notnull() )]
       
        Sem2_Sem3_Outer23 = SemTwo.merge(SemThree, left_on='PRSN_UNIV_ID Crypted', right_on='PRSN_UNIV_ID Crypted', how='outer')
        Sem2_Sem3_Outer = Sem2_Sem3_Outer23.ix[(Sem2_Sem3_Outer23['PRSN_UNIV_ID Crypted'].notnull())&(Sem2_Sem3_Outer23['Course_Code_x'].notnull() )&( Sem2_Sem3_Outer23['Course_Code_y'].notnull() )]
       
        Sem3_Sem4_Outer34 = SemThree.merge(SemFour, left_on='PRSN_UNIV_ID Crypted', right_on='PRSN_UNIV_ID Crypted', how='outer')
        Sem3_Sem4_Outer = Sem3_Sem4_Outer34.ix[(Sem3_Sem4_Outer34['PRSN_UNIV_ID Crypted'].notnull())&(Sem3_Sem4_Outer34['Course_Code_x'].notnull() )&( Sem3_Sem4_Outer34['Course_Code_y'].notnull() )]
       
        return(Sem1_Sem2_Outer,Sem2_Sem3_Outer,Sem3_Sem4_Outer)
    
    def JoinAllResultsAndSave(self,Sem1_Sem2_Outer,Sem2_Sem3_Outer,Sem3_Sem4_Outer,path,CoursesTakenInSequence,FileName1,FileName2):
        print ("About to save the results to the File")
        outfileName = path+FileName1
        #outfileName2 = path+FileName2
        FinalResult = panda.concat([Sem1_Sem2_Outer, Sem2_Sem3_Outer,Sem3_Sem4_Outer], ignore_index=True)
        FinalResult.to_csv(outfileName+'.csv', sep=',', encoding='utf-8')     
        
        FinalResultToUse = panda.concat([Sem1_Sem2_Outer.ix[:,1:3], Sem2_Sem3_Outer.ix[:,1:3],Sem3_Sem4_Outer.ix[:,1:3]], ignore_index=True)
        FinalResultToUse.to_csv(outfileName+'_ToUse.csv', sep=',', encoding='utf-8')   
        #CoursesTakenInSequence.to_csv(outfileName2+'_ToUse.csv', sep=',', encoding='utf-8') 
    
    # used for chedking if that particular class number is to be taken care    
    def isAddClassNumber(self,courseCatalogue,classnumber,ClassNumbersToBeTakenCareOf):
        #print courseCatalogue
        if courseCatalogue in ClassNumbersToBeTakenCareOf:
            return("-"+classnumber)
        else:
            return("")
    
    
    def divideDataSetToThree(self,EnrolledClassDataAll,PerStudentSemisterOrder,OnlyStudentsWith4SemestersModeSet):
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
        
        
    def createBinsForEachConsequtiveTerms(BinsToProcessNow,EnrolledClassData):
        print ("Creating Bin for    " + str(BinsToProcessNow[0]) +"  -   "+str(BinsToProcessNow[1]) )
        BinOneAllData = EnrolledClassData.loc[EnrolledClassData['ACAD_TERM_CD']== BinsToProcessNow[0]]
        BinTwoAllData = EnrolledClassData.loc[EnrolledClassData['ACAD_TERM_CD']== BinsToProcessNow[1]]
    
        BinOne= BinOneAllData.ix[:,['PRSN_UNIV_ID Crypted','Course_Code']]
        BinTwo= BinTwoAllData.ix[:,['PRSN_UNIV_ID Crypted','Course_Code']]
    
        return(BinOne,BinTwo)    


    def BinsOuterJoin(BinOne,BinTwo):       
       Bin1_Bin2_Outer12 = BinOne.merge(BinTwo, left_on='PRSN_UNIV_ID Crypted', right_on='PRSN_UNIV_ID Crypted', how='outer')
       Bin1_Bin2_Outer12 = Bin1_Bin2_Outer12.ix[(Bin1_Bin2_Outer12['PRSN_UNIV_ID Crypted'].notnull())&(Bin1_Bin2_Outer12['Course_Code_x'].notnull() )&( Bin1_Bin2_Outer12['Course_Code_y'].notnull() )]
       return(Bin1_Bin2_Outer12)
       
       def JoinAllResultsAndSave(ResultSet,FileName1,path):
           print ("About to save the results to the File")
           outfileName = path+FileName1
           #outfileName2 = path+FileName2
           ResultSet.to_csv(outfileName+'.csv', sep=',', encoding='utf-8')
    
    #################################################################################################################################################################################################################################################################    
