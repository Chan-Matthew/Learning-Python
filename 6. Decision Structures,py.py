#not 1st, then and then or

print True or not True and False


year = 200

if (year%4 == 0) and ((year%100 !=0) or (year%400==0)):
    print True
else:
    print False

#try:
    #black
#except:
    #print something

s = [["hello","goodbye","ciao"],["pen"," apple","applepen"],["purple","yellow","blue"]]
code  = "defghijklmnopqrstuvwxyzabc"

import string

def doTrans(s,frm, to):
    table = string.maketrans(frm,to)
    result = string.translate(s,table)
    return result

def encodeMessage (S, code):
    result = []
    for row in S:
        newRow = []
        for word in row:
            newRow.append(doTrans(word, string.ascii_lowercase, code))
        result.append(newRow)
    return result

def decodeMessage (S, code):
    result = []
    for row in S:
        newRow = []
        for word in row:
            newRow.append(doTrans(word,code ,string.ascii_lowercase))
        result.append(newRow)
    return result

result = encodeMessage(s, code)
print result
decoded = decodeMessage(result,code)
print decoded
