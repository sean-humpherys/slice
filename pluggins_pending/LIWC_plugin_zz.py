# for plugin to be recognized by the SLICEngine, it must end in zz.py, such as 'pluginzz.py'

from pluginInterface import Interface
LIWC = open(r'c:\Python25\SLICE\LIWCFiles\LIWC2007_English080730.dic').readlines()

LIWClist = []
for i in range(len(LIWC)):
    LIWClist.append(LIWC[i].split())
LIWClist.remove(['%']) #remove the first percentage sign


LIWCcat = {} #create a dictionary of liwc categories e.g. {'22' : 0, ... }
LIWCnames = {} #holds the names of the Liwc categories as the key and the category number as the value
while LIWClist[0][0].startswith('%') == False:
    LIWCcat[LIWClist[0][0]]= 0
    LIWCnames[LIWClist[0][0]] = LIWClist[0][1] 
    LIWClist.remove(LIWClist[0])

LIWClist.remove(['%']) #remove the second percentage sign
#LIWClist now only contains words, categories are removed

#puts liwc words into a dictionary e.g. {'friend' : [12, 50, 43] , ... }
LIWCwords = {}
LIWCstems = {}
ListOfStems = []
for i in range(len(LIWClist)):
    aline = LIWClist[i]
    aline.reverse()
    revline = aline #revline is aline reversed, helps with pop()
    aword = revline.pop()
    if aword.endswith('*'):
        LIWCstems[aword] = revline
        ListOfStems.append(aword)
    else:
        LIWCwords[aword] = revline


        
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

        #reset the LIWCcat values to zero
        for key in LIWCcat.keys():
            LIWCcat[key] = 0
        
        #put words into a dictionary with their counts
        wordDict = {}
        FoundStem = False
        print textObject
        for word in textObject:
            if LIWCwords.has_key(word.lower()) == True:
                for i in LIWCwords[word.lower()]:
                    LIWCcat[i] += 1                    
            elif LIWCstems: #add stuff for stemmed keys
                while FoundStem == False:
                    for g in ListOfStems:#search through list of stems
                        if word.lower().find(g[:-1]) == 0:
                            FoundStem == True
                            for s in LIWCstems[g]:
                                LIWCcat[s] += 1
                    FoundStem = True



              


#Return the pluginDict. The Dictionary keys will be the column headers.
        pluginDict = {}

        for key in LIWCnames.keys():
            pluginDict[LIWCnames[key]] = float(LIWCcat[key])/self.words
        
        return pluginDict

    def setTextObjectType(self, x):
        """here you can choose how you want the textObject to be sent to the process function. It can
        be sent as either raw text or tokenized text. Use return raw, or return tokenized
        If you have a file with the line: 'I am a dog.', raw text will return that line as is
        and tokenized text will return a list: ['I', 'am', 'a', 'dog', '.']"""

        #return "raw"
        return "tokenized"
