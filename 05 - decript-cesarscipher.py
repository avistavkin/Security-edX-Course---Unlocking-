alphabet = "abcdefghijklmnopqrstuvwxyz"
allength=len(alphabet)
Lalphabet=list (alphabet)


#length=len(brute_force)
#print("plaintext length:", length)
#Lbrute_force = list(brute_force)

def encrypt(ciphertext, i):
    Lbrute_force = list(ciphertext)
    print ("Key=", i)
    length=len(ciphertext)
    for k in range(length): 
        for x in range (26):
            if Lbrute_force[k] == Lalphabet [x]:
                    
                    if (x+i) >= allength:
                        diff = x+i - allength
                        Lbrute_force[k] = Lalphabet [diff]
                        break
                    Lbrute_force[k] = Lalphabet [x+i]
                    break         
    return Lbrute_force           

for i in range (26):
    Lbrute_force = encrypt("kyvtrmrcipnzccrkkrtbwifdkyvefikynvjkrkeffe", i)
    print ("".join(Lbrute_force)) # собирает из листа (или массива) строку
    print ("\n")

"""
brute_force("kyvtrmrcipnzccrkkrtbwifdkyvefikynvjkrkeffe")

def brute_force(ciphertext):

    pass #print all (plaintext, k) possibilities and copy the right one to the Edx platform
    
brute_force("kyvtrmrcipnzccrkkrtbwifdkyvefikynvjkrkeffe")

"""