# Michelle Bergin
# 
# =========================
# This project is my attempt at creating a neural network.
# 
# Below is my choice of colors for this project
#
# I will organize my related words by:
# 
# * hypernym
# * hyponym
# * troponym
# * holonym
# * meronym
# * accidence?
# * inflexionism ^?
# * polysemous
# 
# How I determine these... not sure.

import os, node

colors = ["green", "blue", "violet", "crimson", "alabaster", "orange", "aqua", "amaranth", "purple", "pink", "red", "amber", "bronze", "brown", "gold", "rose", "silver", "yellow", "amethyst", "white", "brass", "fuchsia", "ruby", "aquamarine", "lime", "gray", "auburn", "azure", "batorange", "beige", "black", "blond", "blood", "sapphire", "lavender", "lilac", "maroon", "turquoise", "rose", "burgundy", "cadet", "cerulean", "charcoal", "chartreuse", "copper", "coral", "cyan", "ebony", "ultramarine", "firebrick", "garnet", "ivory", "indigo", "jade", "khaki", "magenta", "mahogany", "mauve", "olive", "opal", "periwinkle", "scarlet", "sienna", "tan", "teal", "topaz", "umber", "vermillion"]

# Each node will be a specific color. If a color is found in a text that matches one above, a node will be created for it. From then on if that same color is called again changes will be made to the original node already created. So there will be only one node per color.

nodes = []

def main():

    # All book text needs to go into a folder in this directory called books.
    folder = "books"

    # Walking the folder to pull out all the files therein
    files = openFolder(folder)

    # Parsing out colors from the files
    findColors(files, folder)
    
    for node in nodes:
        print(node.color)
        node.printWords()

def openFolder(folder):
    files = []
    for root, dirs, fileNames in os.walk(folder):
        files = fileNames
    return files

def findColors(files, folder):
    for eachFile in files:
        location = ""
        location = folder + "/" + eachFile

        fh = open(location, "r")

        # Reading and stripping annoying shit from my text files
        fh = fh.read()
        fh = fh.replace('\n', ' ')
        fh = fh.replace('\r', ' ')
        fh = fh.replace('\\', ' ')
        fh = fh.replace('!', '. ')
        fh = fh.replace('?', '. ')
        fh = fh.replace('(', '')
        fh = fh.replace(')', '')
        fh = fh.replace('[', '')
        fh = fh.replace(']', '')
        fh = fh.replace('{', '')
        fh = fh.replace('}', '')
        fh = fh.replace('-', ' ')
        fh = fh.replace(':', '')
        fh = fh.replace('"', '')

        # Pulling out sentances from the text
        sentances = fh.split('. ')
 
        for sentance in sentances:
            
            # Getting rid of unnecessary shit again
            sentance = sentance.replace('.', '')
            sentance = sentance.replace(';', '')
            sentance = sentance.replace(',', '')
            sentance = sentance.replace('\'', '')

            sentance = sentance.split(' ')
            
            for word in sentance:
                new = True
                # If the word in the sentance is one of the colors above:
                if word in colors:
                    # If the color is already a node
                    for eachNode in nodes:
                        # If the node already exists for the color:
                        if(eachNode.color == word):
#                            nodes.append(node.Color(word, sentance))
                            new = False
                    if new:
                        nodes.append(node.Color(word, sentance))
                            
    
if __name__ == '__main__':
    main()
