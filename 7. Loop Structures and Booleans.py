##while line:                                               Sentinel loop
##    linesREad = linesRead  1
##    line = infile.readline()
##infile.close()

#Babylonian method
posNum = 1234
sq = float(posNum)
while(abs(sq - posNum/sq) > 0.001):
    sq= (sq+posNum/sq)/2
    print sq

from random import randint
def guessingGame():
    number = randint(1,10)
    guess = None
    try:
        while guess != number:
            
            guess = input("What number am I thinking of: (q to quit) ")
    except:
        pass
      
print "----------------------------"
print False and True            #prints first false statement 
print 0 and ""
print False*3
print "" and 0
print [3,"0"] or 0
print 0 or "1D04" or []     #prints 1st true statement for Or
print "Cat" and "dog"       #prints 2nd true statement if first is also true for And 
print True and "hello"
print 1 or Kitten
