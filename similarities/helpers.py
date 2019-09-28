from nltk.tokenize import sent_tokenize

def lines(a, b):
    """Return lines in both a and b"""
    aList = a.split('\n')
    bList = b.split('\n')
    simList = []

    for line in aList:
        if line in bList:
            simList.append(line)

    return simList


def sentences(a, b):
    """Return sentences in both a and b"""
    aList = sent_tokenize(a)
    bList = sent_tokenize(b)
    simList = []
    for sent in aList:
        if sent in bList and sent not in simList:
            simList.append(sent)
    # TODO
    return simList


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    def subList (s, n):
        sList = []
        for i in range(len(s) - (n - 1)):
            j = i + n
            sList.append(s[i:j])
        return sList

    aList = subList(a, n)
    bList = subList(b, n)

    simList = []
    for sub in aList:
        if sub in bList and sub not in simList:
            simList.append(sub)

    # TODO
    return simList
