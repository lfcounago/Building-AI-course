import math
import numpy as np

text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''

def distance(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi)**2
    return np.sqrt(sum)

def main(text):
    # tasks your code should perform:

    # 1. split the text into words, and get a list of unique words that appear in it
    # a short one-liner to separate the text into sentences (with words lower-cased to make words equal 
    # despite casing) can be done with 
    # docs = [line.lower().split() for line in text.split('\n')]
    docs = [line.lower().split() for line in text.split('\n')]
    docdictionary = {}
    linedictionaries = []
    # 2. go over each unique word and calculate its term frequency, and its document frequency
    for line in docs:
        linedictionary = {}
        for word in line:
            if word in linedictionary.keys():
                linedictionary[word] += 1
            else:
                linedictionary[word] = 1
            if word in docdictionary.keys():
                docdictionary[word] += 1
            else:
                docdictionary[word] = 1
        linedictionaries.append(linedictionary)
    # 3. after you have your term frequencies and document frequencies, go over each line in the text and 
    # calculate its TF-IDF representation, which will be a vector
    tfidf_vector = []
    lineindex = 0
    for line in docs:
        line_vector = []
        for word in line:
            line_vector.append(linedictionaries[lineindex][word] * math.log(1/docdictionary[word]))
        tfidf_vector.append(line_vector)
        lineindex += 1
    # 4. after you have calculated the TF-IDF representations for each line in the text, you need to
    # calculate the distances between each line to find which are the closest.
    #N = len(tfidf_vector)
    outerrow = []
    outerrowindex = 0
    for row in tfidf_vector:
        innerrowindex = 0
        innerrow = []
        for secondrow in tfidf_vector:
            if innerrowindex == outerrowindex:
                innerrow.append(np.inf)
            else:
                innerrow.append(distance(row, secondrow))
            innerrowindex += 1
        outerrow.append(innerrow)
        outerrowindex += 1
    dist = np.stack(outerrow)        
    print(np.unravel_index(np.argmin(dist), dist.shape))

main(text)