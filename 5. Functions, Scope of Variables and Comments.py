#def name (parameter):
    #block

def word(word):
    print word
word("hello")

def sum2(num1, num2):
    print num1+num2
sum2(2,2)

def sumList(alist):
    total = 0
    for i in alist:
        total+=i
    print total
spam = [1,1,1,6,3,8,12,16]
sumList(spam)

def sumdiff(num1,num2):
    sums = num1+num2
    diff = num1-num2
    return sums,diff
a,b = sumdiff(10,7)
c = sumdiff(10,7)                           #gives you a tuple. Similar to lists but immutable
print a
print b
print c

def hamplusone(ham):
    ham = ham+1
    return ham
ham = 4
print hamplusone(ham)               #prints out 5
print ham                                           #prints out 4

def addspam(spam):
    spam = spam.append("hello")
    return spam
spam = [1]
addspam(spam)
print spam
