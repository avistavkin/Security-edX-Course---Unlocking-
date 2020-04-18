alphabet = "abcdefghijklmnopqrstuvwxyz"
allength=len(alphabet)
print (allength)
Lalphabet=list (alphabet)
#print (Lalphabet[1])
plaintext = input("Enter plaintext:")
Key  = int(input("Enter key:"))

length=len(plaintext)
#print("plaintext length:", length)
Lplaintext = list(plaintext)

def encrypt(Lplaintext, Key):
    for k in range(length):
        for x in range (26):
            
            if Lplaintext[k] == Lalphabet [x]:
                    
                    if (x+Key) >= allength:
                        diff = x+Key - allength

                        Lplaintext[k] = Lalphabet [diff]
                        break
                    Lplaintext[k] = Lalphabet [x+Key]
                    break         
    return Lplaintext           

encrypt(Lplaintext, Key)
print ("".join(Lplaintext)) # собирает из листа (или массива) строку