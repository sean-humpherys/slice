# for plugin to be recognized by the SLICEngine, it must end in zz.py, such as 'pluginzz.py'
from pluginInterface import Interface
import re

class plugin(Interface):
    """must have process and setTextObjectType functions"""
    whissell = open(r'c:\Python26\SPLICE\dictionaryofaffect.txt').readlines()

    whissDict = {}
    for i in range (len(whissell)):
        aline = whissell[i].split()
        whissDict[aline[0]] =(aline[1],aline[2],aline[3])
    
    def process(self, rawText, fileAttributes):
        """ must return a dictionary object """

        newRaw = re.sub(r'[\s+\.\?!,\"\%@#\^\(\)\n\\]',' ', rawText)
        newnewRaw = re.sub(r'\'','*', newRaw)
        tokens = newnewRaw.split(None)

# File attributes passed in from SLICEngine

        imagery = 0.0

        numWhisselWords = 0 # keeps track of num words found in Whissel Dictionary
          
        #self.numSentences = fileAttributes['numSentences'] #total number of sentences in file
        self.numWords = fileAttributes['numWords'] #total number of words in file
        #self.numChars = fileAttributes['numChars'] #total number of chars in file
        #self.numCharsMinusSpacesAndPunctuation = fileAttributes['numCharsMinusSpacesAndPunctuation'] #total number of chars from words only
        #self.avgSentenceLength = fileAttributes['avgSentenceLength'] #average sentence length
        #self.avgWordLength = fileAttributes['avgWordLength'] #average word length
        #self.numSyllables = fileAttributes['numSyllables'] #total number of syllables in file
        #self.avgSyllablesPerWord = fileAttributes['avgSyllablesPerWord'] #average syllables per word
        #self.numWordsWith3OrMoreSyllables = fileAttributes['numWordsWith3OrMoreSyllables'] #number of words with three or more syllables


        # puts words into a dictionary with their counts
        wordDict = {}
        for word in tokens:
            if wordDict.has_key(word) == True:
                wordDict[word] +=1
                
            else:
                wordDict[word] = 1
                           
         # calculate Activation
        for word in wordDict:
            if plugin.whissDict.has_key(word) == True:
                numWhisselWords += wordDict[word]
                imagery += float(plugin.whissDict[word][2]) * float(wordDict[word])
             
        
        
# Fill pluginDict with plugin results for new linguistic cue

        pluginDict = {}

        if numWhisselWords != 0:
            pluginDict['ImageryPlugin'] = imagery/numWhisselWords

        else:
            pluginDict['ImageryPlugin'] = 0
            

#Return the pluginDict. The Dictionary keys will be the column headers.
        
        return pluginDict

