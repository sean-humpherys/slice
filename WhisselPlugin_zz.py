# for plugin to be recognized by the SLICEngine, it must end in zz.py, such as 'pluginzz.py'
import random
from pluginInterface import Interface
from path import Path


def open_dictionary(whissell_file_loc=r'dictionaries/Whissell_dictionary_English.txt'):
    """Open's the Dictionary of Affect by Whissell. Words and ratings start after the header ends on line 39. 
    Order of a line in the dictionary is : word, pleasantness rating, activation, imagery. 
    Delimeter is a series of white spaces. 
    """
    path = Path(whissell_file_loc)
    words_start_at = 39
    with open(path, mode='r') as f:
        whole_file = f.readlines()
        whiss_dict = {}
        for i in range(words_start_at, len(whole_file)):
            ratings = whole_file[i].split()
            whiss_dict[ratings[0]] = (ratings[1], ratings[2], ratings[3])
    return whiss_dict


class plugin(Interface):
    """must have process and setTextObjectType functions"""
    whissell = open(r'dictionaryofaffect.txt').readlines(
    )  # edited by sean 3/20/2019 to remove the hardcoded path to dictionaryofaffect.txt

    whissDict = {}
    for i in range(len(whissell)):
        aline = whissell[i].split()
        whissDict[aline[0]] = (aline[1], aline[2], aline[3])

    def process(self, textObject, fileAttributes):
        """must return a dictionary object"""

# File attributes passed in from SLICEngine

        positive = 0.0
        negative = 0.0
        activation = 0.0

        numWhisselWords = 0  # keeps track of num words found in Whissel Dictionary

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

        # puts whissel into a dictionary

        # puts words into a dictionary with their counts
        wordDict = {}
        # print textObject
        for word in textObject:
            if wordDict.has_key(word) == True:
                wordDict[word] += 1

            else:
                wordDict[word] = 1
        # print wordDict

         # calculate positivity
        for word in wordDict:
            if plugin.whissDict.has_key(word) == True:
                numWhisselWords += wordDict[word]
                positive += float(plugin.whissDict[word]
                                  [0]) * float(wordDict[word])
                negative += float(plugin.whissDict[word]
                                  [1]) * float(wordDict[word])
                activation += float(plugin.whissDict[word]
                                    [2]) * float(wordDict[word])


# Fill pluginDict with plugin results for new linguistic cue

        pluginDict = {}

        if numWhisselWords != 0:
            pluginDict['Whissellpos'] = positive/numWhisselWords
            pluginDict['Whissellneg'] = negative/numWhisselWords
            pluginDict['Whissellact'] = activation/numWhisselWords

        else:
            pluginDict['Whissellpos'] = 0
            pluginDict['Whissellneg'] = 0
            pluginDict['Whissellact'] = 0


# Return the pluginDict. The Dictionary keys will be the column headers.

        return pluginDict

    def setTextObjectType(self, x):
        """here you can choose how you want the textObject to be sent to the process function. It can
        be sent as either raw text or tokenized text. Use return raw, or return tokenized
        If you have a file with the line: 'I am a dog.', raw text will return that line as is
        and tokenized text will return a list: ['I', 'am', 'a', 'dog', '.']"""

        # return "raw"
        return "tokenized"
