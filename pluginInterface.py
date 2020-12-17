class Interface:
    def __init__(self):
        if self.__class__ == Interface:
            # I'm an abstract base class, don't instantiate me.
            raise TypeError

    def process(self, tokenList, fileAttributes):
        raise TypeError

    def setTextObjectType(self):
        raise TypeError
