# for plugin to be recognized by the SLICEngine, it must end in zz.py, such as 'pluginzz.py'
from pluginInterface import Interface
import re

class plugin(Interface):

    """must have process and setTextObjectType functions"""
   
    def process(self, rawText, fileAttributes): 
        """ must return a dictionary object """

        newRaw = re.sub(r'[\s+\.\?!,\"\%@#\^\(\)\n\\]',' ', rawText)
        newnewRaw = re.sub(r'\'','*', newRaw)
        tokens = newnewRaw.split(None)
        

# File attributes passed in from SLICEngine

    
        #self.numSentences = fileAttributes['numSentences'] #total number of sentences in file
        self.numWords = fileAttributes['NumWords'] #total number of words in file
        #self.numChars = fileAttributes['numChars'] #total number of chars in file
        #self.numCharsMinusSpacesAndPunctuation = fileAttributes['numCharsMinusSpacesAndPunctuation'] #total number of chars from words only
        #self.avgSentenceLength = fileAttributes['avgSentenceLength'] #average sentence length
        #self.avgWordLength = fileAttributes['avgWordLength'] #average word length
        #self.numSyllables = fileAttributes['numSyllables'] #total number of syllables in file
        #self.avgSyllablesPerWord = fileAttributes['avgSyllablesPerWord'] #average syllables per word
        #self.numWordsWith3OrMoreSyllables = fileAttributes['numWordsWith3OrMoreSyllables'] #number of words with three or more syllables

        #read in hedging adverbs
        lAdverbs = open(r'dictionary_hedging_adverbs.txt').readlines()
        lAdverbs = [words.rstrip('\n') for words in lAdverbs] #remove the end of line character \n from each line

        
        #read in hedging adjectives
        lAdj = open(r'dictionary_hedging_adj.txt').readlines()
        lAdj = [words.rstrip('\n') for words in lAdj] #remove the end of line character \n from each line

        
        #read in hedging conjunctions
        lConj = open(r'dictionary_hedging_conjunctions.txt').readlines()
        lConj = [words.rstrip('\n') for words in lConj] #remove the end of line character \n from each line

        
        #read in hedging verbs
        lVerb = open(r'dictionary_hedging_verbs.txt').readlines()
        lVerb = [words.rstrip('\n') for words in lVerb] #remove the end of line character \n from each line


        #Declare variables
        intHedgingModal = 0
        intNonhedgingModal = 0
        intHedgingAdverbs = 0
        intHedgingAdj = 0
        intHedgingConj = 0
        intHedgingVerbs = 0

        #populate Nonhedging modal verbs, rawText is not tokenized and in one long string, run this line only once, "have got to" is counted in the slang "got to"
        intNonhedgingModal += (rawText.lower().count('have to') + rawText.lower().count('had to') + rawText.lower().count('got to') + rawText.lower().count('need to'))

        
        #populate values by finding modal verbs, repeat for each word in the token list
        for word in tokens:
            if word.lower() in ['may', 'might', 'ought', 'should', 'would', 'wouldn*t', 'could', 'couldn*t']:
                intHedgingModal +=1
                
        #populate additional Nonhedging modal verbs
            if word.lower() in ['must', 'mustn*t', 'shall', 'can', 'can*t', 'cannot', 'will', 'won*t']: # The astrict is becuase SpliceEngine removes the apostrophy and replaces with *
                intNonhedgingModal +=1

        #populate hedging adverbs
            if word.lower() in lAdverbs:
                intHedgingAdverbs +=1    

        #populate hedging Adjectives
            if word.lower() in lAdj:
                intHedgingAdj +=1


        #populate hedging Conjunctions
            if word.lower() in lConj:
                intHedgingConj +=1
                
        #populate hedging Verb
            if word.lower() in lVerb:
                intHedgingVerbs +=1
       
           
# Fill pluginDict with plugin results for new linguistic cue        
        pluginDict = {}
        try:
            pluginDict['NonhedgeModal'] = self.formatAnswer(intNonhedgingModal / self.numWords)  #convert raw count to ratio
            pluginDict['HedgeModal'] = self.formatAnswer(intHedgingModal  / self.numWords  )     
            pluginDict['HedgeAdv'] = self.formatAnswer(intHedgingAdverbs  / self.numWords)
            pluginDict['HedgeAdj'] = self.formatAnswer(intHedgingAdj  / self.numWords)
            pluginDict['HedgeConj'] = self.formatAnswer(intHedgingConj  / self.numWords)
            pluginDict['HedgeVerb'] = self.formatAnswer(intHedgingVerbs  / self.numWords)
            pluginDict['HedgeAll'] = self.formatAnswer((intHedgingModal + intHedgingAdverbs + intHedgingAdj + intHedgingConj + intHedgingVerbs ) / self.numWords)
        except ZeroDivisionError:
            pluginDict['NonhedgeModal'] = 0
            pluginDict['HedgeModal'] = 0
            pluginDict['HedgeAdv'] = 0
            pluginDict['HedgeAdj'] = 0
            pluginDict['HedgeConj'] = 0
            pluginDict['HedgeVerb'] = 0
            pluginDict['HedgeAll'] = 0
            
        
#Return the pluginDict. The Dictionary keys will be the column headers.
        
        return pluginDict

    def setTextObjectType(self, x):
        """here you can choose how you want the textObject to be sent to the process function. It can
        be sent as either raw text or tokenized text. Use return raw, or return tokenized
        If you have a file with the line: 'I am a dog.', raw text will return that line as is
        and tokenized text will return a list: ['I', 'am', 'a', 'dog', '.']"""

        return "raw"
        #return "tokenized"
    
    def formatAnswer(self, value):  #Format answer to a percentage with 3 decimals
        value = value * 100
        return '%.3f' % (value)
