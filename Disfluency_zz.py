# for plugin to be recognized by the SLICEngine, it must end in zz.py, such as 'pluginzz.py'
from pluginInterface import Interface
import re


class plugin(Interface):

    """must have process and setTextObjectType functions"""

    def process(self, rawText, fileAttributes):
        """ must return a dictionary object """

        newRaw = re.sub(r'[\s+\.\?!,\"\%@#\^\(\)\n\\]', ' ', rawText)
        newnewRaw = re.sub(r'\'', '*', newRaw)
        tokens = newnewRaw.split(None)

# File attributes passed in from SLICEngine

        # self.numSentences = fileAttributes['numSentences'] #total number of sentences in file
        # total number of words in file
        self.numWords = fileAttributes['NumWords']
        # self.numChars = fileAttributes['numChars'] #total number of chars in file
        # self.numCharsMinusSpacesAndPunctuation = fileAttributes['numCharsMinusSpacesAndPunctuation'] #total number of chars from words only
        # self.avgSentenceLength = fileAttributes['avgSentenceLength'] #average sentence length
        # self.avgWordLength = fileAttributes['avgWordLength'] #average word length
        # self.numSyllables = fileAttributes['numSyllables'] #total number of syllables in file
        # self.avgSyllablesPerWord = fileAttributes['avgSyllablesPerWord'] #average syllables per word
        # self.numWordsWith3OrMoreSyllables = fileAttributes['numWordsWith3OrMoreSyllables'] #number of words with three or more syllables

        # Declare variables
        intDisfluenciesAll = 0
        intUm = 0
        intUh = 0
        intEREHAHTTT = 0

        # populate values by finding disfluencies
        for word in tokens:
            # print word.lower()
            if word.lower() in ['um', 'umm']:
                intUm += 1
            if word.lower() in ['uh']:
                intUh += 1
            if word.lower() in ['er', 'eh', 'ah', 'ttt', 'tt', 'tttt']:
                intEREHAHTTT += 1

        # Find & count repeating phrases
        #txt = r'Uh, I hope I look nice and and pretty reliable.'
        #txt =r'People mainly um um maybe healthcare providers.'
        # txt = r'Well I I very I very very seldom miss a day or work.' #CIFA S222 Q5
        # (\b=word boundary \w+ is alphanumeric) then comes space or coma than duplicate word then word boundery. Returns repeating single-words phrases. i.e. "I I very seldom."
        patternOne = re.compile(r'(\b\w+)[,\s]+\1\b', re.IGNORECASE)
        # this findstwo-word phrases that repeate e.g. "I very I very seldom miss a day"
        patternTwo = re.compile(
            r'(\b\w+\b[,\s]\b\w+)[,\s]+\1\b', re.IGNORECASE)

        repeating2WordPhrases = re.findall(patternTwo, rawText)
        repeating1Word = re.findall(patternOne, rawText)

        # length of list tells us how many matches were found
        r1 = len(repeating1Word)
        r2 = len(repeating2WordPhrases)
        intCountRepeats = r1 + r2

# Fill pluginDict with plugin results for new linguistic cue
        pluginDict = {}
        try:  # take count and convert to ratio
            pluginDict['Disfluencies'] = self.formatAnswer(
                (intUm + intUh + intEREHAHTTT + intCountRepeats) / self.numWords)
            pluginDict['Um'] = self.formatAnswer(intUm / self.numWords)
            pluginDict['Uh'] = self.formatAnswer(intUh / self.numWords)
            pluginDict['UmUh'] = self.formatAnswer(
                (intUm + intUh) / self.numWords)
            pluginDict['ErEhAhTtt'] = self.formatAnswer(
                intEREHAHTTT / self.numWords)
            # raw count, this is not a function of how many words in a sentence.
            pluginDict['RepeatPhrasesCount'] = intCountRepeats
            pluginDict['RepeatPhrasesRatio'] = self.formatAnswer(
                intCountRepeats / self.numWords)

        except ZeroDivisionError:
            pluginDict['Disfluencies'] = 0
            pluginDict['Um'] = 0
            pluginDict['Uh'] = 0
            pluginDict['UmUh'] = 0
            pluginDict['ErEhAhTtt'] = 0
            pluginDict['RepeatPhrasesCount'] = 0
            pluginDict['RepeatPhrasesRatio'] = 0


# Return the pluginDict. The Dictionary keys will be the column headers.

        return pluginDict

    def setTextObjectType(self, x):
        """here you can choose how you want the textObject to be sent to the process function. It can
        be sent as either raw text or tokenized text. Use return raw, or return tokenized
        If you have a file with the line: 'I am a dog.', raw text will return that line as is
        and tokenized text will return a list: ['I', 'am', 'a', 'dog', '.']"""

        return "raw"
        # return "tokenized"

    # Format answer to a percentage with 3 decimals, added by SEan
    def formatAnswer(self, value):
        value = value * 100
        return '%.3f' % (value)
