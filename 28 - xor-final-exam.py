
c1 = 0b00100111010
c2 = 0b01001110110
c3 = 0b11010110101

print ("m1  = c3 ^ c2 ", bin(c3 ^ c2))
m1 = bin(c3 ^ c2)
m1 = 0b10011000011

print ("key = c1 ^ m1 ", bin(c1 ^ m1))
key = 0b10111111001
print ("m2  = c2 ^ key", bin(c2 ^ key))

m2 = 0b11110001111

print ("m3  = m1 ^ m2 ", bin(m1 ^ m2))

m3 = 0b01101001100

print ("c3  = m3 ^ key ", bin(m3 ^ key))

