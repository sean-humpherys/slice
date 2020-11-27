# for plugin to be recognized by the SLICEngine, it must end in zz.py, such as 'pluginzz.py'
from pluginInterface import Interface
#import re
#Counts the number of question marks in the response. must use raw text

class plugin(Interface):

    """must have process and setTextObjectType functions"""

    def process(self, rawText, fileAttributes): 
        """ must return a dictionary object """


        #newRaw = re.sub(r'[\s+\.\?!,\"\%@#\^\(\)\n\\]',' ', rawText)
        #newnewRaw = re.sub(r'\'','*', newRaw)
        #tokens = newnewRaw.split(None)

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
        intQuestions = 0     
        intQuestions = rawText.lower().count('?')  #rawText is a single string of raw text, run only once on rawText, do not run on words in tokens code
        
# Fill pluginDict with plugin results for new linguistic cue 'you know, I mean, like, well, okay, yeah, and oh'
        pluginDict = {}
        try:
            pluginDict['QuestionCount'] = intQuestions
            pluginDict['QuestionRatio'] = self.formatAnswer(intQuestions  / self.numWords)

        except ZeroDivisionError:
            pluginDict['QuestionCount'] = 0
            pluginDict['QuestionRatio'] = 0
        
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
