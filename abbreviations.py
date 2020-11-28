from pathlib import Path


class Abbreviation:
    """ Creates a list of abbreviations that are used to help the sentence splitter identify sentences and ignore stuff like 'Dr.'
    """

    def __init__(self):
        path = Path(r"abbreviationsLower.txt")
        with open(path, mode='r') as f:
            abbrev_str = f.read()
            self.abbreviations = abbrev_str.split()

    def is_abbreviation(self, word=""):
        """
        Returns True if the word is in a list of predefined abbreviations

        Precondition:  punctuation, like periods, have been removed from the testable abbreviation

        Arguments: 
            word: string

        Return: 
            boolean.  True if the word is in a list of predefined abbreviations
        """
        return True if word.lower() in self.abbreviations else False
