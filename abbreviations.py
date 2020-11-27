# The abbrevfile is a list of abbreviations that are used to help the
# sentence splitter identify sentences and ignore stuff like "Dr."
# Precondition: punctuation, like periods, have been removed

class Abbreviation:
    def __init__(self):
        abbrevfile = r"abbreviationsLower.txt"
        g = open(abbrevfile, 'r')
        abbrevstr = g.read()

        self.L = abbrevstr.split()

    def isabbrev(self, s):
        """
        The abbrev method compares words to the abbrevfile
        """
        abbrevs = self.L
        if s.lower() in abbrevs:
            return True
        else:
            return False
