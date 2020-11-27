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




        #Declare variables
        intLike = 0
        intWell = 0
        intOkay = 0
        intYeah = 0
        intOh = 0
        intYouKnow = 0
        intIMean = 0
        intOther = 0

        #populate values by finding interjections 
        for word in tokens:  #tokens is the list of words without punctuation
            if word.lower() in ['like']:
                intLike +=1
            if word.lower() in ['well']:
                intWell +=1
            if word.lower() in ['okay', 'ok']:
                intOkay +=1
            if word.lower() in ['yeah']:
                intYeah +=1
            if word.lower() in ['oh', 'ooh']:
                intOh +=1
            if word.lower() in ['ew', 'ha', 'huh', 'hm', 'hmm', 'huh', 'jeez', 'mhm', 'uh-huh', 'uh-oh', 'whoa', 'whew', 'phew', 'mm', 'mmm', 'wow', 'alright', 'gosh', 'ah-hum', 'mm-hm', 'mm-hmm']:
                intOther +=1
                
        intYouKnow = rawText.lower().count('you know')  #rawText is a single string of raw text, run only once on rawText, do not run on words in tokens code
        intIMean = rawText.lower().count('i mean')
        #consider 'Let's see' as an interjection hesitations.
        
# Fill pluginDict with plugin results for new linguistic cue 'you know, I mean, like, well, okay, yeah, and oh'
        pluginDict = {}
        try:
            pluginDict['Interjections'] = self.formatAnswer((intLike + intWell + intOkay + intYeah + intOh + intYouKnow + intIMean + intOther)  / self.numWords ) #convert raw counts to ratios
            pluginDict['Like'] = self.formatAnswer(intLike  / self.numWords)
            pluginDict['Well'] = self.formatAnswer(intWell  / self.numWords)
            pluginDict['Okay'] = self.formatAnswer(intOkay  / self.numWords)
            pluginDict['Yeah'] = self.formatAnswer(intYeah  / self.numWords)
            pluginDict['Oh'] = self.formatAnswer(intOh  / self.numWords)
            pluginDict['YouKnow'] = self.formatAnswer(intYouKnow  / self.numWords)
            pluginDict['IMean'] = self.formatAnswer(intIMean  / self.numWords)
            pluginDict['InterjOthers'] = self.formatAnswer(intOther  / self.numWords)
        except ZeroDivisionError:
            pluginDict['Interjections'] = 0
            pluginDict['Like'] = 0
            pluginDict['Well'] = 0
            pluginDict['Okay'] = 0
            pluginDict['Yeah'] = 0
            pluginDict['Oh'] = 0
            pluginDict['YouKnow'] = 0
            pluginDict['IMean'] = 0
            pluginDict['InterjOthers'] = 0
        
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
