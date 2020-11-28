# Simple tests of abbreviations module
from abbreviations import Abbreviation


abbr = Abbreviation()
# should be true values
assert abbr.is_abbreviation("Dr") == True
assert abbr.is_abbreviation("a") == True
assert abbr.is_abbreviation("I") == True


# should be false values
assert abbr.is_abbreviation("in") == False
assert abbr.is_abbreviation("doctor") == False
assert abbr.is_abbreviation("mister") == False
assert abbr.is_abbreviation("Dr.") == False
assert abbr.is_abbreviation("") == False

print("Test Passed")

"""Design notes
The abbreviationsLower.txt file includes each letter in the alphabet. One unintented consequence is the letter "a" is a letter AND an article
This abbreviation list will identify the article "a" as an abbreviation rather than as an article
"i" is in the abbreviation list. An unintented consequence is the personal pronoun "I" will be identified as an abbreviation and not be counted in pronouns
The consequences depend on how the abbreviation list is used.
On school of though is don't treat abbreviations differently. Using a neural network can handle abbreviations, stemming, and the like (Rachel Thomas, FastAI NLP).
"""
