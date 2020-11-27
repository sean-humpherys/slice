'''
import re
txt = r'Uh, I hope I look nice and and pretty reliable.'
txt =r'People mainly um um maybe healthcare providers.' 
txt = r'Well I I very I very very seldom miss a day or work.' #CIFA S222 Q5
patternOne = re.compile(r'(\b\w+)[,\s]+\1\b', re.IGNORECASE)  #(\b=word boundary \w+ is alphanumeric) then comes space or coma than duplicate word then word boundery. Returns repeating single-words phrases. i.e. "I I very seldom." 
patternTwo = re.compile(r'(\b\w+\b[,\s]\b\w+)[,\s]+\1\b', re.IGNORECASE) # this findstwo-word phrases that repeate e.g. "I very I very seldom miss a day"
patternTwo = re.compile(r'(\b\w+\b[,\s]\b\w+)[,\s]+\1\b', re.IGNORECASE)
repeating2WordPhrases = re.findall(patternTwo, txt)
repeating1Word = re.findall(patternOne, txt)
r1 = len(repeating1Word) #length of list tells us how many matches were found
r2 = len(repeating2WordPhrases)
print r1 + r2

strFileName = r'C:\Temp\DACA_Text_Files\DACA_Interviewee_First_Response\Innocent_Q01'
print strFileName.find('Innofcent')
                       
p = re.compile('Innogcent', re.IGNORECASE)
r = re.search(p, strFileName)
if r:
    print "Subject " + r.group(1)
    pluginDict['Condition'] = "T"
    pluginDict['ConditionNum'] = 0
else:
    print "Subject guilty"
'''

word =r'Um, I would definitely have to say working at an ice cream parlor. Um, the duties were a bit monotonous after a while, I worked there for about six months and I had to make waffle cones every day and I must have burned my fingers every single time but I did it and it was terrible and the people there were horrendous and I was really young compared to everybody else so it was just a terrible experience. '
#populate Nonhedging modal verbs
if word.lower() in ['must', 'mustn*t', 'shall', 'can', 'can*t', 'cannot', 'needn*t','will', 'won*t',]: # The astrict is becuase SpliceEngine removes the apostrophy and replaces with *
    intNonhedgingModal +=1
intNonhedgingModal += rawText.lower().count('have to')
intNonhedgingModal += rawText.lower().count('have got to')
intNonhedgingModal += rawText.lower().count('need to')

print intNonhedgingModal
def formatAnswer(value):
    value = value * 100
    return '%.3f' % (value)

