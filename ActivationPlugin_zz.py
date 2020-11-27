# for plugin to be recognized by the SLICEngine, it must end in zz.py, such as 'pluginzz.py'
from pluginInterface import Interface
import re

class plugin(Interface):
    """must have process and setTextObjectType functions"""
    whissell = open(r'dictionaryofaffect.txt').readlines()

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

        activation = 0.0

        numWhisselWords = 0 # keeps track of num words found in Whissel Dictionary
          
        #self.numSentences = fileAttributes['numSentences'] #total number of sentences in file
        self.numWords = fileAttributes['NumWords'] #total number of words in file
        #self.numChars = fileAttributes['numChars'] #total number of chars in file
        #self.numCharsMinusSpacesAndPunctuation = fileAttributes['numCharsMinusSpacesAndPunctuation'] #total number of chars from words only
        #self.avgSentenceLength = fileAttributes['avgSentenceLength'] #average sentence length
        #self.avgWordLength = fileAttributes['avgWordLength'] #average word length
        #self.numSyllables = fileAttributes['numSyllables'] #total number of syllables in file
        #self.avgSyllablesPerWord = fileAttributes['avgSyllablesPerWord'] #average syllables per word
        #self.numWordsWith3OrMoreSyllables = fileAttributes['numWordsWith3OrMoreSyllables'] #number of words with three or more syllables



        # puts whissel into a dictionary
        


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
                activation += float(plugin.whissDict[word][1]) * float(wordDict[word])
             
        
        
# Fill pluginDict with plugin results for new linguistic cue

        pluginDict = {}
        #Changed by Sean, divided by numWords instead of numWhissleWords
        if self.numWords != 0:
            pluginDict['ActivationPlugin'] = activation/self.numWords

        else:
            pluginDict['ActivationPlugin'] = 0
            

#Return the pluginDict. The Dictionary keys will be the column headers.
        
        return pluginDict

    def setTextObjectType(self, x):
        """here you can choose how you want the textObject to be sent to the process function. It can
        be sent as either raw text or tokenized text. Use return raw, or return tokenized
        If you have a file with the line: 'I am a dog.', raw text will return that line as is
        and tokenized text will return a list: ['I', 'am', 'a', 'dog', '.']"""

        return "raw"
        #return "tokenized"

