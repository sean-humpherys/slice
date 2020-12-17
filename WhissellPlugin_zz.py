# for plugin to be recognized by the SLICEngine, it must end in zz.py, such as 'pluginzz.py'
import random
from pluginInterface import Interface
from whissellapi import WhissellDictionary


class plugin(Interface):
    # must have process and setTextObjectType functions

    def process(self, textObject, fileAttributes):
        # must return a dictionary object

        # File attributes passed in from SLICEngine
        # not sure I need this code is I do not need these attribute values
        self.fileName = fileAttributes['FILENAME']  # name of the file
        # total number of lines in file
        self.lines = fileAttributes['NumLines']
        # total number of blank lines in file
        self.blankLines = fileAttributes['NumBlankLines']
        # total number of sentences in file
        self.numSentences = fileAttributes['NumSents']
        # total number of words in file
        self.words = fileAttributes['NumWords']
        # total number of chars in file
        self.characters = fileAttributes['NumChars']
        # total number of chars from words only
        self.wordCharacters = fileAttributes['NumWordChars']
        # average sentence length
        self.averageSentenceLength = fileAttributes['NumWordChars']
        # average word length
        self.averageWordLength = fileAttributes['AvgWordLen']
        # total number of syllables in file
        self.totalSyllables = fileAttributes['NumSyllables']
        # average syllables per word
        self.averageSyllables = fileAttributes['AvgSyllablesWord']
        # number of words with three or more syllables
        self.numWordsWithThreeOrMoreSyllables = fileAttributes['NumWordsThreeOrMoreSyllables']

        wd = WhissellDictionary()
        # Whissell defaults to 2 is no words found. 2 means a rating "in-between"
        avg_pleasantness = wd.pleasantness_average(textObject)
        avg_activation = wd.activation_average(textObject)
        avg_imagery = wd.imagery_average(textObject)


# Fill pluginDict with plugin results for new linguistic cue
        pluginDict = {}
        pluginDict['WhissellPleasantness'] = avg_pleasantness
        pluginDict['WhissellActivation'] = avg_activation
        pluginDict['WhissellImagery'] = avg_imagery

# Return the pluginDict. The Dictionary keys will be the column headers.

        return pluginDict

    def setTextObjectType(self, x):
        """here you can choose how you want the textObject to be sent to the process function. It can
        be sent as either raw text or tokenized text. Use return raw, or return tokenized
        If you have a file with the line: 'I am a dog.', raw text will return that line as is
        and tokenized text will return a list: ['I', 'am', 'a', 'dog', '.']"""

        # return "raw"
        return "tokenized"
