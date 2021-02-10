# 1st Problem

def remdup(l):
    if len(l) == 0:
        return []
    else:
        return removeLastOccur(l)

def removeLastOccur(l):
    AnswerList = []
    l.reverse()
    for i in l:
        if i not in AnswerList:
            AnswerList.append(i)
    AnswerList.reverse()
    return (AnswerList)


# 2nd Problem

def splitsum(l):
    AnswerList = []
    pos = 0
    neg = 0
    for i in l:
        if i > 0:
            pos = pos + (i*i)
        elif i < 0:
            neg = neg + (i*i*i)
    AnswerList.append(pos)
    AnswerList.append(neg)
    return AnswerList


# 3rd Problem

def matrixflip(m,d):
    l = m[:]
    if d == 'h':
        for i in l:
            i.reverse()
    elif d == 'v':
        l.reverse()
    else:
        return m
    return(l)