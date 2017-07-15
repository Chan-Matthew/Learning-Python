#Learn how to convert from hexadecimal and binary to decimal basically everything

print bin(35)                            #to binary
print hex(0b100011)         #to hexadecimal

print "---------------------------------------"

outer = ['Li', 'Na','K']
inner = ['F','Cl','Br']

for metal in outer:
    for gas in inner:
        print metal + gas

numbers = range(1,13)
for x in numbers:
    for y in numbers:
        print "\t",x*y,
    print

for i in range(1,6):
    for j in range(1,i+1):
        print j,
    print
    
print "---------------------------------------"
