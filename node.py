from __future__ import print_function
import nltk
from nltk.corpus import wordnet as wn

noWords = ["192", "209", "1848", "unless", "houseless", "whose", "those", "unfrequently", "you", "hant", "themselves", "adeliza", "until", "itself", "parti", "into", "eau", "cannot", "them", "sladden", "thuls", "sowla", "larkar", "toldenarba", "akathooma", "neerib", "lel", "unto", "nuth", "these", "myself", "her", "against", "whom", "should", "where", "when", "moomoos", "than", "would", "unpanting", "this", "which", "they", "their", "what", "tholdenblarna", "star-girt", "him", "upon", "with", "jyshak", "that", "wherein", "shepperalk", "his", "man-horse", "from", "the", "and", "was", "out", "for", "are", "ave", "ago", "all", "apt", "ask", "had"]

class Word:
    
    def __init__(self, theWord, theColor, theLocationFromColor):
        self.word = theWord
        self.locFromColor = theLocationFromColor
        self.colors = []
        self.repeat = 1
        self.colors.append(theColor)
        # All related to color
        # wup_similarity, path_similarity
        self.relatedness = []
        self.synsetWord = "" if not wn.synsets(self.word) else wn.synsets(self.word)[0]
        self.related()

    def related(self):
        # Adding wup_similarity
        if self.colors:
            wup = self.colors[len(self.colors) - 1].wup_similarity(self.synsetWord)
            if(type(wup) != type(None)):
                self.relatedness.append(wup)
            path = self.colors[len(self.colors) - 1].path_similarity(self.synsetWord)
            if(type(path) != type(None)):
                self.relatedness.append(path)

    def add(self, newLocation):
        # If the word has already existed for this color. We will find the average location of the two.
        self.repeat += 1
        self.locFromColor = (self.locFromColor + newLocation) / self.repeat

class Color:
    
    def __init__(self, theWord, sentance):
        self.color = theWord
        self.synsetColor = wn.synsets(self.color)[0]
        self.location = sentance.index(self.color)
        self.wordNodes = []
        self.processWords(sentance)
        self.repeat = 1

    def processWords(self, sentance):
        for aWord in sentance:
            new = True
            locationFromColor = abs(sentance.index(aWord) - self.location)
            if(locationFromColor <= 5 and aWord != self.color):
                aWord = aWord.lower()
                # If word does not exist yet for this color
                if(len(aWord) > 2 and aWord not in noWords):
                    for eachNode in self.wordNodes:
                        if(eachNode.word == aWord):
                            new = False
                            eachNode.add(locationFromColor)
                    if new:
                        self.wordNodes.append(Word(aWord, self.synsetColor, locationFromColor))

    def add(self, newLocation, newSentance):
        # If the color has already existed. We will find the average location of the two.
        self.repeat += 1
        self.location = (self.location + newLocation) / self.repeat
        self.add(newSentance)

    def printWords(self):
        for aWord in self.wordNodes:
            print(aWord.word, end = ' ')
        print('\n')
