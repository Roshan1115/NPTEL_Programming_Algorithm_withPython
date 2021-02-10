# 1st problem

def PrimeCheck(num):    # cheking for prime number
    if (num == 0 or num == 1):
        return False
    elif num == 2:
        return True
    for i in range(2, num):
        if (num%i == 0):
            return False
        elif i == num-1:
            return True

def primepartition(m):    # Checking for partitionability
    Prime_upto_number = []
    for i in range(2, m-1):
        if(PrimeCheck(i) == True):
            Prime_upto_number.append(i)
    for p in Prime_upto_number:
        q = m - p
        if(q in Prime_upto_number):
            return True
    if m <= 2:      # number less than 2cannot be partitioned into prime numbers
        return False
    else:
        return False


# 2nd Problem

def matched(s):
    counter = 0
    i = 0
    while(counter >= 0 and i < len(s)):
        if(s[i] == "("):
            counter = counter + 1
        if(s[i] == ")"):
            counter = counter - 1
        i = i + 1
    if(counter == 0):
        return True
    else:
        return False


# 3rd Problem

def rotateOne(l):
    first_element = l[0]
    for i in range(0, len(l)):
        if(i == len(l)-1):
            l[i] = first_element
        else:
            l[i] = l[i + 1]

def rotatelist(LIS,k):
    l = LIS[:]
    if(k <= 0):
        return(LIS)
    for i in range(1, k+1):
        rotateOne(l)
    return(l)

print(rotatelist([1,2,3,4,5],3))