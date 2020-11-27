# count lines, sentences, and words of a text file
lines, blanklines, sentences, words = 0, 0, 0, 0
filename = r'C:\Temp\DACA_Text_Files\DACA_Interviewee_First_Response\Guilty_Q10\DACAMC_Guilty_Q10_S29.txt'
textf = open(filename, 'r')
for line in textf:
    print line, # test
    lines += 1
    if line.startswith('\n'):
        blanklines += 1
    else:
    # assume that each sentence ends with . or ! or ?
        sentences += line.count('.') + line.count('!') + line.count('?')
        tempwords = line.split(None)
        print tempwords # test
        # word total count
        words += len(tempwords)
textf.close()       
print "Words : ", words
