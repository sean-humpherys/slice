# for plugin to be recognized by the SLICEngine, it must end in zz.py, such as 'pluginzz.py'

from pluginInterface import Interface
youList = open(r'you.dic').readlines()

class plugin(Interface):
    """must have process and setTextObjectType functions"""

    def process(self, textObject, fileAttributes):
        """ must return a dictionary object """

# File attributes passed in from SLICEngine

        self.fileName = fileAttributes['FILENAME'] #name of the file
        self.lines = fileAttributes['NumLines'] #total number of lines in file
        self.blankLines = fileAttributes['NumBlankLines'] #total number of blank lines in file
        self.numSentences = fileAttributes['NumSents'] #total number of sentences in file
        self.words = fileAttributes['NumWords'] #total number of words in file
        self.characters = fileAttributes['NumChars'] #total number of chars in file
        self.wordCharacters = fileAttributes['NumWordChars'] #total number of chars from words only
        self.averageSentenceLength = fileAttributes['NumWordChars'] #average sentence length
        self.averageWordLength = fileAttributes['AvgWordLen'] #average word length
        self.totalSyllables = fileAttributes['NumSyllables'] #total number of syllables in file
        self.averageSyllables = fileAttributes['AvgSyllablesWord'] #average syllables per word
        self.numWordsWithThreeOrMoreSyllables = fileAttributes['NumWordsThreeOrMoreSyllables'] #number of words with three or more syllables

# Fill pluginDict with plugin results for new linguistic cue
        i=0
        pluginDict = {}
        for word in textObject:
            if word in youList:
                i+=1
        pluginDict['Test'] = i
        #self.printThis('Im inside')
        print'Im inside directly'


#Return the pluginDict. The Dictionary keys will be the column headers.
        
        return pluginDict

    def setTextObjectType(self, x):
        """here you can choose how you want the textObject to be sent to the process function. It can
        be sent as either raw text or tokenized text. Use return raw, or return tokenized
        If you have a file with the line: 'I am a dog.', raw text will return that line as is
        and tokenized text will return a list: ['I', 'am', 'a', 'dog', '.']"""

        #return "raw"
        return "tokenized"
