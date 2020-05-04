import math

passlenth = 10
numberofchars = 26+26+10
numberofcombination = passlenth ** numberofchars
print (numberofcombination)
timetocalculate = numberofcombination * 0.01
print (int(timetocalculate))
print (type(timetocalculate))
print ("time in days", int(timetocalculate / 86400))

numberofcombinationsfortimeattack = passlenth * numberofchars
print ("numberofcombinationsfortimeattack", numberofcombinationsfortimeattack)
timefortimeattack = numberofcombinationsfortimeattack * 0.01
print ("timefortimeattack", timefortimeattack)
xor = 26 ** 20
print ("xor=", int(xor))

hasharbitrary = 1.17 * (2 ** 12)
print ("hasharbitrary", math.ceil(hasharbitrary))