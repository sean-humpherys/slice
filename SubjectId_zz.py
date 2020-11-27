# for plugin to be recognized by the SLICEngine, it must end in zz.py, such as 'pluginzz.py'
from pluginInterface import Interface
import re

#Module parses the file name to find the subjectID. Returns just the ID. 
#strFile = r'C:\Temp\Guilty_Text_Files\DACAMC_Guilty_Q01_S149.txt'   #returns  149
#File name must include S followed by one or more numbers


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

        strFileName = fileAttributes['FILENAME']
        

        p = re.compile(r'S(\d{1,3})', re.IGNORECASE)
        r = re.search(p, strFileName)
 
    
# Fill pluginDict with plugin results for new linguistic cue        
        pluginDict = {}
        if r:
            print "Subject " + r.group(1)
            pluginDict['SubjectId'] = r.group(1)
      
       

        
#Return the pluginDict. The Dictionary keys will be the column headers.
        
        return pluginDict
        

    def setTextObjectType(self, x):
        """here you can choose how you want the textObject to be sent to the process function. It can
        be sent as either raw text or tokenized text. Use return raw, or return tokenized
        If you have a file with the line: 'I am a dog.', raw text will return that line as is
        and tokenized text will return a list: ['I', 'am', 'a', 'dog', '.']"""

        return "raw"
        #return "tokenized"

