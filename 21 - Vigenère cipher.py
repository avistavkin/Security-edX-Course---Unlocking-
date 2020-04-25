

def codewordadjust (plaintext, codeword):
    lenpl       = len (plaintext)
    lenco       = len (codeword)
    x           = lenpl / lenco
    y           = lenpl // lenco
    codeworda   = ""
    if y == 0:  # тут нужен будет обработчик если текст короче кодового слова
        i = 0
        for i in range (lenpl):
            codeworda += codeword [i]
    #    print ("y=", y)
    else:
        
        i = 0
        for i in range (y):
            codeworda += codeword 
        #print (codeworda) 
        z = lenpl - lenco*y
        #print (z) 
        if z != 0:
            i = 0
            for i in range (z):
                codeworda += codeword [i]
            #print (codeworda)  
    return codeworda

def encrypt (plaintext, codeworda):
   
    lenpl       = len (plaintext)
    i = 0
    Lplaintext = list(plaintext)
    Lcodeworda = list(codeworda)
    
    for i in range (lenpl):
        #print ("i=", i)
        diff = ord (Lcodeworda[i]) - ord ("A")
        #print ("diff=", diff)
        ordz = ord ("Z")
        #print ("ordx=", ordz)
        ordi = ord (Lplaintext[i])+ diff
        #print ("ordi=", ordi)
        orddiff = ordi-ordz
        #print ("orddiff=", orddiff)

        if (ord (Lplaintext[i])+ diff) > ord ("Z"):
            Lplaintext[i] = chr (ord ("A") + orddiff -1)
            #((ord (Lplaintext[i])+ diff) - ord ("Z"))
        
        else: Lplaintext [i] = chr (ord (Lplaintext[i])+ diff)

        #print (Lplaintext [i])

    
    return Lplaintext


#plaintext = input('plaintext...: ')
plaintext   = "ATTACKATDAWNATTACKATDAWN"
print ("plaintext= ",plaintext)
#codeword = input('codeword...: ')
codeword    = "LEMON"

codeworda   = codewordadjust (plaintext, codeword)
print ("codeworda= ",codeworda)

ciphertext  = encrypt (plaintext, codeworda)
print ("ciphertext=", ciphertext)
print ("".join(ciphertext))
#print (codeworda)