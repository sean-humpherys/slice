# for plugin to be recognized by the SLICEngine, it must end in zz.py, such as 'pluginzz.py'
from pluginInterface import Interface
import re

#Module parses the file name to find the Truth or Deceptive Condition. Returns T (0) or D (1). 
#strFile = r'C:\Temp\Guilty_Text_Files\DACAMC_Guilty_Q01_S149.txt'   #returns  D and 1 in two variables
#Change the following strTruthfulID to the text in the Filename that identifies the truthful from deceptive conditions

strTruthfulId = 'Truth'
strDeceptiveId = 'Lie'

class plugin(Interface):

    """must have process and setTextObjectType functions"""

    def process(self, rawText, fileAttributes): 
        """ must return a dictionary object """

        #newRaw = re.sub(r'[\s+\.\?!,\"\%@#\^\(\)\n\\]',' ', rawText)
        #newnewRaw = re.sub(r'\'','*', newRaw)
        #tokens = newnewRaw.split(None)
        

# File attributes passed in from SLICEngine

    
        #self.numSentences = fileAttributes['numSentences'] #total number of sentences in file
        #self.numWords = fileAttributes['NumWords'] #total number of words in file
        #self.numChars = fileAttributes['numChars'] #total number of chars in file
        #self.numCharsMinusSpacesAndPunctuation = fileAttributes['numCharsMinusSpacesAndPunctuation'] #total number of chars from words only
        #self.avgSentenceLength = fileAttributes['avgSentenceLength'] #average sentence length
        #self.avgWordLength = fileAttributes['avgWordLength'] #average word length
        #self.numSyllables = fileAttributes['numSyllables'] #total number of syllables in file
        #self.avgSyllablesPerWord = fileAttributes['avgSyllablesPerWord'] #average syllables per word
        #self.numWordsWith3OrMoreSyllables = fileAttributes['numWordsWith3OrMoreSyllables'] #number of words with three or more syllables

        strFileName = fileAttributes['FILENAME']  #Global var of File Name being processed
        
        intCondition = strFileName.find(strTruthfulId) #returns integer of strTruthfulID, returns -1 if not found
        
 
    
# Fill pluginDict with plugin results for new linguistic cue        
        pluginDict = {}
        if intCondition >0:  #truthful
            pluginDict['Condition'] = "T"
            pluginDict['ConditionNum'] = 0
        else:
            pluginDict['Condition'] = "D"
            pluginDict['ConditionNum'] = 1      
       

        
#Return the pluginDict. The Dictionary keys will be the column headers.
        
        return pluginDict
        

    def setTextObjectType(self, x):
        """here you can choose how you want the textObject to be sent to the process function. It can
        be sent as either raw text or tokenized text. Use return raw, or return tokenized
        If you have a file with the line: 'I am a dog.', raw text will return that line as is
        and tokenized text will return a list: ['I', 'am', 'a', 'dog', '.']"""

        return "raw"
        #return "tokenized"

