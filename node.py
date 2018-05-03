import nltk

from nltk.corpus import wordnet as wn

noWords = ["192", "209", "1848", "unless", "houseless", "whose", "those", "unfrequently", "you", "hant", "themselves", "adeliza", "until", "itself", "parti", "into", "eau", "cannot", "them", "sladden", "thuls", "sowla", "larkar", "toldenarba", "akathooma", "neerib", "lel", "unto", "nuth", "these", "myself", "her", "against", "whom", "should", "where", "when", "moomoos", "than", "would", "unpanting", "this", "which", "they", "their", "what", "tholdenblarna", "star-girt", "him", "upon", "with", "jyshak", "that", "wherein", "shepperalk", "his", "man-horse", "from", "the", "and", "was", "out", "for", "are", "ave", "ago", "all", "apt", "ask", "had"]

class Word:
    
    def __init__(self, theWord, theColor):
        self.word = theWord
        self.colors = []
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

class Color:
    
    def __init__(self, theWord, theSentance):
        self.color = theWord
        self.synsetColor = wn.synsets(self.color)[0]
        self.sentance = theSentance
        self.wordNodes = []
        self.processWords()

    def processWords(self):
        for aWord in self.sentance:
            new = True
            aWord = aWord.lower()
            # If word does not exist yet for this color
            if(len(aWord) > 2 and aWord not in noWords):
                for eachNode in self.wordNodes:
                    if(eachNode.word == aWord):
                        new = False
                if new:
                    self.wordNodes.append(Word(aWord, self.synsetColor))
