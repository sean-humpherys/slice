import os
import csv
import re
from abbreviations import Abbreviation


class SLICEngine:

    def __init__(self, docPath, output_file_name="results.txt"):
        self.docPath = docPath
        # os.getcwd())    #WHAT is this for?
        self.dirList = os.listdir(r'D:\Dropbox\Python26\SLICE')
        self.pluginList = []
        self.imp = ""
        self.fileAttributeDict = {}
        self.pluginAttributeDict = {}
        self.allAttributeDict = {}
        self.dictionaryList = []
        self.setDictionaryList = False
        # keeps track of the headerrow being written into CSV File"
        self.headerRowWritten = False
        self.OutputFileName = output_file_name

        # file attributes available to plugin
        self.lines = 0.0  # Number of lines
        self.blanklines = 0.0  # Number of Blank Lines
        self.numsentences = 0.0  # done
        self.words = 0.0  # Number of words
        self.characters = 0.0
        self.characters_minus_spaces = 0.0
        self.averageSentenceLength = 0.0
        self.averageWordLength = 0.0
        self.numWordsWith6OrMoreChars = 0.0
        self.numWordsWith7OrMoreChars = 0.0
        self.totalSyllables = 0.0
        self.averageSyllables = 0.0
        self.numWordsWithThreeOrMoreSyllables = 0.0

        for pluginFile in self.dirList:
            if pluginFile[-5:] == "zz.py":
                self.pluginList.append(pluginFile[:-3])


#________________________________________________________________________#
        # Essential for running Syllable Counter

        self.cmudict = r'cmudict.txt'
        self.sy_dict = {}
        self.SubSyl = ['cial', 'tia', 'cius', 'cious',
                       'giu', 'ion', 'iou', 'sia$', '.ely$', ]
        self.AddSyl = ['ia', 'riet', 'dien', 'iu', 'io', 'ii', '[aeiouym]bl$', '[aeiou]{3}', '^mc', 'ism$',
                       '([^aeiouy])\1l$', '[^l]lien', '^coa[dglx].', '[^gq]ua[^auieo]', 'dnt$', ]
#________________________________________________________________________#

    def runProgram(self):

        self.documentList = []
        self.docList = os.listdir(self.docPath)
        for document in self.docList:
            if document[-4:] == ".txt":  # only use txt files
                self.documentList.append(self.docPath + "\\" + document)

        for theFile in self.documentList:

            self.countWords(theFile)
            self.setNumSentences(theFile)
            self.setSyllables(theFile)
            self.setAverageSyllables()
            self.setFileAttributeDict()
            self.fileAttributeDict['FILENAME'] = theFile
            self.allAttributeDict.update(self.fileAttributeDict)
            self.setPlugins(theFile)
            self.resetINIT()
            # print self.fileAttributeDict

        return 0

    def resetINIT(self):
        """
        reset the variables
        """
        self.lines = 0.0  # Number of lines
        self.blanklines = 0.0  # Number of Blank Lines
        self.numsentences = 0.0  # done
        self.words = 0.0  # Number of words
        self.characters = 0.0
        self.characters_minus_spaces = 0.0
        self.averageSentenceLength = 0.0
        self.averageWordLength = 0.0
        self.totalSyllables = 0.0
        self.averageSyllables = 0.0
        self.numWordsWithThreeOrMoreSyllables = 0.0
        self.numWordsWith6OrMoreChars = 0.0
        self.numWordsWith7OrMoreChars = 0.0
        self.allAttributeDict = {}

    def setFileAttributeDict(self):

        self.fileAttributeDict['FILENAME'] = ''
        self.fileAttributeDict['NumLines'] = self.lines
        self.fileAttributeDict['NumBlankLines'] = self.blanklines
        self.fileAttributeDict['NumSents'] = self.numsentences
        self.fileAttributeDict['NumWords'] = self.words
        self.fileAttributeDict['NumChars'] = self.characters
        self.fileAttributeDict['NumWordChars'] = self.characters_minus_spaces
        self.fileAttributeDict['AvgSentLen'] = self.averageSentenceLength
        self.fileAttributeDict['AvgWordLen'] = self.averageWordLength
        self.fileAttributeDict['NumSyllables'] = self.totalSyllables
        self.fileAttributeDict['AvgSyllablesWord'] = self.averageSyllables
        self.fileAttributeDict['NumWordsThreeOrMoreSyllables'] = self.numWordsWithThreeOrMoreSyllables
        if self.setDictionaryList == False:  # don't set the list more than once
            self.dictionaryList = ['FILENAME', 'NumLines', 'NumBlankLines', 'NumSents',
                                   'NumWords', 'NumChars', 'AvgSentLen',
                                   'NumWordChars', 'AvgWordLen', 'NumSyllables', 'AvgSyllablesWord',
                                   'NumWordsThreeOrMoreSyllables']

    def setPlugins(self, filename):
        raw = open(filename, 'r').read()
        newRaw = re.sub(r'[\s+\.\?!,\"\%@#\^\(\)\n\\]', ' ', raw)
        newnewRaw = re.sub(r'\'', '*', newRaw)
        tokens = newnewRaw.split(None)
        def a(x, y): return self.imp.plugin().process(x, y)
        def objectType(o): return self.imp.plugin().setTextObjectType(o)
        for aPlugin in self.pluginList:
            self.imp = __import__(aPlugin)

            if objectType(1) == "raw":
                f = a(raw, self.fileAttributeDict)
            if objectType(1) == "tokenized":
                f = a(tokens, self.fileAttributeDict)

            for key in f.keys():
                if self.setDictionaryList == False:  # don't set the list more than once
                    self.dictionaryList.append(key)
                # self.fileAttributeDict.update(f)#combine lexical cues into one dictionary
                # combine lexical cues into one dictionary
                self.pluginAttributeDict.update(f)
        # update the all Attribute Dict with plugin values
        self.allAttributeDict.update(self.pluginAttributeDict)
        self.setDictionaryList = True  # set after the dictionarlist has been made
        # print self.dictionaryList
        self.__writeToCSV()

    # + "\\output"):
    def __writeToCSV(self, destination=os.getcwd() + "\\output"):
        if self.headerRowWritten == False:  # make sure the header row only gets written onece
            CSVDictFile = open(destination + "\\" +
                               self.OutputFileName, 'wb')  # changed by Sean
            CSVWriter = csv.writer(CSVDictFile)
            CSVWriter.writerow(self.dictionaryList)
            self.headerRowWritten = True
            CSVDictFile.close()
        CSVDictFile = open(destination + "\\" +
                           self.OutputFileName, 'ab')  # changed by Sean
        CSVDictWriter = csv.DictWriter(
            CSVDictFile, fieldnames=self.dictionaryList)
        CSVDictWriter.writerow(self.allAttributeDict)
        CSVDictFile.close()

    def setFullPathName(self, docname):
        """sets the self.docs variable"""
        filepath = self.docPath + "\\" + docname
        return filepath

    def countWords(self, filename):
        """counts the lines, blank lines, # of characters, and # words"""

        thetextfile = open(filename, 'r')
        # print "filename",thetextfile
        for line in thetextfile:
            self.lines += 1
            self.characters += (len(line)-1)  # doesn't count \n or blank lines
            # create a line with no spaces or punc
            newline = re.sub(r'[\s+\.\?!,\"\'\%@#\^\(\)\\]', '', line)
            # counts the number of characters minus spaces,tabs,newlines
            self.characters_minus_spaces += len(newline)
            # use for average word length
            if line.startswith('\n'):
                self.blanklines += 1

            tempwords = line.split(None)
            self.words += len(tempwords)
            for aWord in tempwords:
                if len(aWord) > 5:
                    self.numWordsWith6OrMoreChars += 1
                if len(aWord) > 6:
                    self.numWordsWith7OrMoreChars += 1
        self.characters += 1  # add 1 because there is no \n on the last line of the text
        # print "numcharacters",self.characters
        if self.words > 0:
            self.averageWordLength = self.characters_minus_spaces/self.words

    def setNumSentences(self, filename):
        """
        counts the number of sentences, sets the average sentence length, 
        """
        textfile = open(filename, 'r')
        self.readtextfile = textfile.read()
        self.text = self.readtextfile.replace('\n', ' ')
        pattern = re.compile(r"(\w+\"?\)?)([\.\?!])")
        # constructs an iterator that returns match objects
        prev = 0
        sentenceList = []
        abbr = Abbreviation()
        for m in pattern.finditer(self.text):
            if not(abbr.isabbrev(m.group(1))):
                # stick in a space before the period so the tokenizer won't
                # be confused about what's an abbreviation
                chunk = self.text[prev:m.end()-1] + m.group(2)
                sentenceList.append(chunk)
                prev = m.end()
        self.numsentences = len(sentenceList)
        if self.numsentences > 0:
            self.averageSentenceLength = self.words/self.numsentences
        else:
            self.averageSentenceLength = 0

    def setSy_Dict(self):  # sets the sy_dict
        openDict = open(self.cmudict, 'r')
        for line in openDict:
            if re.match(r'[a-zA-Z]', line):
                cdu = re.split(r'\s+', line, 1)
                sy_count = len(re.findall("\d+", cdu[1]))
                self.sy_dict[cdu[0]] = sy_count

    def setSyllables(self, filename):
        thetextfile = open(filename, 'r')
        num = 0
        for line in thetextfile:
            num += 1
            # print "     running subprocess %s of %s" % (num,self.lines)  #by Sean
            linelist = re.split(r'\s+', line)
            if not line:
                break
            for word in linelist:
                sy = self.get_sy_count(word)
                self.totalSyllables += sy
                if sy >= 3:
                    self.numWordsWithThreeOrMoreSyllables += 1
                if (sy == 0):
                    continue

    def get_sy_count(self, word):
        """Return the number of syllables in word, 0 if word not recognised """
        uword = re.sub('[^A-Z\']', '', word.upper())
        if (uword == ''):
            return 0
        if uword in self.sy_dict:
            return self.sy_dict[uword]  # memoize
        """
        if self.cmudict:
            cdu = re.split(r'\s+', os.popen('qgrep -e "^%s " %s ' % (uword, self.cmudict)).readline(), 1)            
            if (cdu[0] != uword):
                sy_count = 0
            else:
                sy_count = len(re.findall("\d+", cdu[1]))
            if sy_count == 0:
                sy_count = self.guess_sy_count(word)
        """
        if not uword:
            # print uword
            junk = 1  # by Sean cause I don't want anything to print and there must be something here or we get compile error
        else:
            sy_count = self.guess_sy_count(word)
        self.sy_dict[uword] = sy_count
        return sy_count

    def guess_sy_count(self, word):
        """If we can't lookup the word, then guess its syllables count. This is
        (heavily) based on Greg Fast's Perl module Lingua::EN::Syllables. But
        the bugs are mine."""
        mungedword = re.sub('e$', '', word.lower())
        splitword = re.split(r'[^aeiouy]+', mungedword)
        splitword = [x for x in splitword if (x != '')]  # hmm
        syllables = 0
        for i in self.SubSyl:
            if re.search(i, mungedword):
                syllables -= 1
        for i in self.AddSyl:
            if re.search(i, mungedword):
                syllables += 1
        if len(mungedword) == 1:
            syllables = + 1
        syllables += len(splitword)
        if syllables == 0:
            syllables = 1
        if len(word) == 1:
            syllables = 1
        return syllables

    def setAverageSyllables(self):
        try:  # exception code added by Sean
            self.averageSyllables = self.totalSyllables/self.words
        except ZeroDivisionError:
            self.averageSyllables = 0

    def setOutputFileName(self, strValue='SPLICE_Output.csv'):  # added by Sean
        self.OutputFileName = strValue
