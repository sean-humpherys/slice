""" Runs SLICE on the desired files
    Specify the input directory of files to run SLICE on
    Specify the single, text output file

"""
import SLICEngine


strDirectory = r'D:\AarenEmails\test'
strFileN = r'Results.txt'
s = SLICEngine.SLICEngine(strDirectory)
s.setOutputFileName(strFileN)
s.runProgram()
print("...Finished.................")


'''
#p=r'C:\Temp\DACA_Text_Files\DACA_Interviewee_First_Response\Guilty_Q01'
p=r'C:\Temp\Test_SPLICE'
strFileN = r'test_okay.csv'
s=SLICEngine.SLICEngine(p)
s.setOutputFileName(strFileN) 
s.runProgram()
print "end................"



for y in xrange(1,25): #Run 24 questions from DACA through SPLICE
    intQuestionNum = y
    strDirectory = r'C:\Temp\DACA_Text_Files\DACA_Interviewee_First_Response\Guilty_Q%02d' % (intQuestionNum)  #%02d forces two digits with leading zero if needed
    strFileN = r'DACAMC_1stResponse_Splice_Q%02d.csv' % (intQuestionNum)
    s=SLICEngine.SLICEngine(strDirectory)
    s.setOutputFileName(strFileN) 
    s.runProgram()
    print "end................."


import SLICEngine
for y in xrange(1,13): #Run 12 questions from CIFA through SPLICE
    intQuestionNum = y
    strDirectory = r'C:\Temp\CIFA_1stResponse\Q%02d' % (intQuestionNum)  #%02d forces two digits with leading zero if needed
    strFileN = r'CIFA_1stResponse_Splice_Q%02d.csv' % (intQuestionNum)
    s=SLICEngine.SLICEngine(strDirectory)
    s.setOutputFileName(strFileN) 
    s.runProgram()
    print "end................."

'''
