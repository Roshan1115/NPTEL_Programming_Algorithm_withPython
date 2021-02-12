# 1st Problem

def rainaverage(l):
    dict1={}
    final=[]
    for tup in l:
        if tup[0] in dict1:
                dict1[tup[0]].append(tup[1])
        else:
                dict1[tup[0]]=[tup[1]]

    for c in dict1:
        ar=sum(dict1[c])/len(dict1[c])
        ar = float(ar)
        final.append(tuple([c,ar]))
        final.sort()
    return final


# 2nd Problem

result =[]
def flatten(l):
    for i in l:
        if listtype(i):
            flatten(i)
        else:
            result.append(i)
    return(result)

def listtype(l):
    return(type(l) == type([]))