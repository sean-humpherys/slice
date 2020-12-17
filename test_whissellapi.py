from statistics import mean
from whissellapi import WhissellDictionary

wd = WhissellDictionary()


# Test various ratings from the Whissell Dictionary
assert isinstance(wd.pleasantness("window"), float) == True


def tests(word, answer):
    print(f"Testing {word}. Returned value:", wd.pleasantness(word),
          wd.activation(word), wd.imagery(word))
    assert wd.pleasantness(word) == answer[0]
    assert wd.activation(word) == answer[1]
    assert wd.imagery(word) == answer[2]
    assert wd.get_tuple(word) == answer
    print("............. test passed")


word = "ain't"
answer = (1.1429, 1.5000, 1.0)  # (pleasantess, activation, imagery)
tests(word, answer)

word = "abilities"
answer = (2.5000, 2.1111, 2.2)  # (pleasantess, activation, imagery)
tests(word, answer)

word = "window"
answer = (2.4000, 1.5556, 3.0)  # (pleasantess, activation, imagery)
tests(word, answer)


# Test None
assert wd.pleasantness(None) == None
assert wd.activation(None) == None
assert wd.imagery(None) == None

# Test missing word
assert wd.pleasantness("bogusword") == None
assert wd.activation("bogusword") == None
assert wd.imagery("bogusword") == None
assert wd.get_tuple("bogusword") == ()

# Test missing word with non_exist_value
assert wd.pleasantness("bogusword", 0) == 0
assert wd.activation("bogusword", 0) == 0
assert wd.imagery("bogusword", 0) == 0

# Test convert_apostrophe()
assert wd.convert_apostrophe("ain't") == "ain’t"
assert wd.convert_apostrophe("windows") == "windows"

# Test variations in appostrophes
# actor's  # char 37
# bunny’s  # char 8217
# doesn’t  # char 8217

word = "actor's"
answer = (2.1000, 2.3077, 2.0)  # (pleasantess, activation, imagery)
tests(word, answer)

word = "bunny’s"
answer = (2.6250, 1.6667, 2.6)  # (pleasantess, activation, imagery)
tests(word, answer)

word = "doesn’t"
answer = (1.5000, 1.8000, 1.4)  # (pleasantess, activation, imagery)
tests(word, answer)

# Test UK spellings
word = "aluminium"
answer = (1.5000, 1.4286, 3.0)  # (pleasantess, activation, imagery)
tests(word, answer)

word = "behaviour"
answer = (2.0000, 2.4545, 2.2)  # (pleasantess, activation, imagery)
tests(word, answer)

word = "plough"
answer = (1.5000, 2.2500, 3.0)  # (pleasantess, activation, imagery)
tests(word, answer)


# Test a list/tuple of words
words = []
answers = []
assert wd.pleasantness_list(words) == answers

words = ["actor's", "plough", "behaviour", "bogusword"]
answers = [2.1000, 1.5000, 2.0000, None]
assert wd.pleasantness_list(words) == answers

words = ["actor's", "plough", "behaviour", "bogusword"]
answers = [2.3077,  2.2500,  2.4545, None]
assert wd.activation_list(words) == answers

words = ["actor's", "plough", "behaviour", "bogusword"]
answers = [2.0, 3.0,  2.2, None]
assert wd.imagery_list(words) == answers

# remove None from a list
ratings = wd.imagery_list(words)
ratings_without_none = list(filter(lambda x: x is not None, ratings))
print(ratings_without_none)

# Test average ratings from a list
words = ["actor's", "plough", "behaviour", "bogusword"]
assert wd.pleasantness_average(words) == 1.8667
assert wd.activation_average(words) == 2.3374
assert wd.imagery_average(words) == 2.4

# Test average ratings from a list
words = ["bogusword"]

print(wd.pleasantness_average(words))


print("ALL TESTS PASS")
