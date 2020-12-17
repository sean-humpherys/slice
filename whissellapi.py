from pathlib import Path
from statistics import mean, StatisticsError

# The only difference between US and UK dictionaries is the spelling of some words. Ratings are the same.
us_dictionary_location = r'dictionaries/whissell_dictionary_us_english.txt'
uk_dictionary_location = r'dictionaries/whissell_dictionary_uk_english.txt'


class WhissellDictionary():
    """ Provides access to the Whissell Dictionary of Affect in Language (US and UK 2009 versions). 
        Methods return ratings on pleasantness, activation, and imagery for a given word. 
        Activation is 'how active the word feels' (1=passive, 2=in between, 3=active).
        Imagery is 'how easily the word calls an image to mind' (1=hard to imagine, 2=in between, 3=easy to imagine).
        Pleasantness is 'how pleasant the word feels' (1=unpleasant, 2=in between, 3=pleasant).
        Loads US and UK versions into one, unique dictionary. According to the Whissell dictionaries'
        content, the US and UK only differ in spelling of some words (e.g., plough, plow, aluminium, aluminum). 
        The ratings are the same. 
    """

    def __init__(self):
        """Loads the US and UK versions of the Whissell dictionary
        into a combine dictionary of unique words and ratings."""

        us_dict = self.load_dictionary()
        uk_dict = self.load_dictionary(uk_dictionary_location)
        self.whiss_dict = {**uk_dict, **us_dict}

    def load_dictionary(self, whissell_file_loc=us_dictionary_location):
        """ Open's the US version of the Dictionary of Affect by Whissell. 
        Words and ratings start after the header ends on line 39.
        Order of a line in the dictionary is: word, pleasantness, activation, imagery.
        Delimeter is a series of white spaces.

        Arguments:
            whissell_file_loc : location of the Whissell dictionary. Defaults to  /dictionaries/

        Returns:
            dictionary of tuples. Each word is a key. Ratings are in a tuple in order (pleasantness, activation, imagery)
        """
        dictionary_starts_at_line = 39
        path = Path(whissell_file_loc)
        temp_dict = {}
        with open(path, mode='r') as f:
            whole_file = f.readlines()
            for i in range(dictionary_starts_at_line, len(whole_file)):
                ratings = whole_file[i].split()
                temp_dict[ratings[0]] = (
                    float(ratings[1]),
                    float(ratings[2]),
                    float(ratings[3]),
                )
        return temp_dict

    def convert_apostrophe(self, target_word):
        """ Converts normal apostrophe (char 37) to char 8217 to match the apostrophe character
        used in the Whissell dictionary, e.g. you’ve, ain’t. The benefit is the Whissell dictionary
        from Dr. Whissell remains unmodified and easily replacable with future dictionary versions.

        target_word: str  The word that may have an apostrophe.

        Returns the word replacing an apostrophe with char 8217."""
        # Whissell dict. uses asspostrophe characters inconsistently
        # In Visual Code, the strange character 'ain�t' in the Whissel dictionary
        # looks like char 65533 but it is sometimes char 8217 or char 37
        apostrophe = "\'"  # char 37
        whissell_apostrophe = "’"  # char 8217
        if isinstance(target_word, str):
            return target_word.replace(apostrophe, whissell_apostrophe)
        else:
            return None

    def get_tuple(self, word):
        """ Returns three ratings for a word as a tuple in order (pleasantness, activation, imagery)
        Returns empty tuple if word not found."""
        # Whissell dict. uses asspostrophe characters inconsistently
        word_altered = self.convert_apostrophe(word)
        ratings = self.whiss_dict.get(word)
        ratings_word_altered = self.whiss_dict.get(word_altered)
        if ratings == None and ratings_word_altered == None:
            return ()  # word not found
        else:
            if ratings == None:
                return ratings_word_altered
            else:
                return ratings

    def activation(self, word, not_exist_value=None):
        """ Returns activation rating (float) from the Whissell dictionary"""
        # Whissell dict. uses asspostrophe characters inconsistently
        word_altered = self.convert_apostrophe(word)
        ratings = self.whiss_dict.get(word)
        ratings_word_altered = self.whiss_dict.get(word_altered)
        if ratings == None and ratings_word_altered == None:
            return not_exist_value  # word not found
        else:
            if ratings == None:
                return ratings_word_altered[1]
            else:
                return ratings[1]

    def imagery(self, word, not_exist_value=None):
        """ Returns imagery rating (float) from the Whissell dictionary"""
        # Whissell dict. uses asspostrophe characters inconsistently
        word_altered = self.convert_apostrophe(word)
        ratings = self.whiss_dict.get(word)
        ratings_word_altered = self.whiss_dict.get(word_altered)
        if ratings == None and ratings_word_altered == None:
            return not_exist_value  # word not found
        else:
            if ratings == None:
                return ratings_word_altered[2]
            else:
                return ratings[2]

    def pleasantness(self, word, not_exist_value=None):
        """ Returns pleasantness rating (float) from the Whissell dictionary"""
        # Whissell dict. uses asspostrophe characters inconsistently
        word_altered = self.convert_apostrophe(word)
        ratings = self.whiss_dict.get(word)
        ratings_word_altered = self.whiss_dict.get(word_altered)
        if ratings == None and ratings_word_altered == None:
            return not_exist_value  # word not found
        else:
            if ratings == None:
                return ratings_word_altered[0]
            else:
                return ratings[0]

    def pleasantness_list(self, words, not_exist_value=None):
        """ Returns a list of pleasantness ratings given a list/tuple of words."""
        answer_list = []
        for word in words:
            answer_list.append(self.pleasantness(word, not_exist_value))
        return answer_list

    def activation_list(self, words, not_exist_value=None):
        """ Returns a list of activation ratings given a list/tuple of words."""
        answer_list = []
        for word in words:
            answer_list.append(self.activation(word, not_exist_value))
        return answer_list

    def imagery_list(self, words, not_exist_value=None):
        """ Returns a list of imagery ratings given a list/tuple of words."""
        answer_list = []
        for word in words:
            answer_list.append(self.imagery(word, not_exist_value))
        return answer_list

    def pleasantness_average(self, words, round_to=4, avg_of_none=2.0):
        """ Returns an average of pleasantness (float) for the words passed in a list.
        Arguments: 
            rount_to is the decimals desired after rounding.
            avg_of_none is the Whissell rating if words is an empty list or words are not in dictionary. 
            2 is suggest since that signifies 'in-between' by Whissell. 
            Alternative could be avg_of_none=None, if user desires to be notified of missing values.
        """
        ratings = self.pleasantness_list(words)
        ratings = list(filter(lambda x: x is not None, ratings))
        try:
            average = round(mean(ratings), round_to)
        except StatisticsError:
            average = avg_of_none
        return average

    def activation_average(self, words, round_to=4, avg_of_none=2.0):
        """ Returns an average of activation (float) for the words passed in a list"""
        ratings = self.activation_list(words)
        ratings = list(filter(lambda x: x is not None, ratings))
        return round(mean(ratings), round_to)

    def imagery_average(self, words, round_to=4, avg_of_none=2.0):
        """ Returns an average of imagery (float) for the words passed in a list"""
        ratings = self.imagery_list(words)
        ratings = list(filter(lambda x: x is not None, ratings))
        return round(mean(ratings), round_to)
