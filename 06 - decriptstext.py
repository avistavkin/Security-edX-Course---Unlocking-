import numpy as np


alphabet = "abcdefghijklmnopqrstuvwxyz"
allength=len(alphabet)
Lalphabet=list (alphabet)

pplaintext = ["hm al, mo tmh hm al, huvh gn hul jzlnhgmt:",\
"qulhulo 'hgn tmaxlo gt hul cgty hm nzrrlo", \
"hul nxgtsn vty voomqn mr mzhovslmzn rmohztl,", \
"mo hm hvel vocn vsvgtnh v nlv mr homzaxln",\
"vty ak mppmngts lty hulc?",\
"hm ygl: hm nxllp;",\
"tm cmol; vty, ak v nxllp hm nvk ql lty",\
"hul ulvoh-vwul vty hul humznvty tvhzovx numwen",\
"huvh rxlnu gn ulgo hm, 'hgn v wmtnzccvhgmt",\
"yldmzhxk hm al qgnu'y. hm ygl, hm nxllp;",\
"hm nxllp: plowuvtwl hm yolvc: vk, hulol'n hul oza;",\
"rmo gt huvh nxllp mr ylvhu quvh yolvcn cvk wmcl",\
"qult ql uvdl nuzrrxly mrr hugn cmohvx wmgx,",\
"cznh sgdl zn pvznl"]

print ("pplaintext")
print (pplaintext)
#plaintextlength

#hhcount = allength*[10*[0]]
hhcount = np.zeros([allength, 13], dtype = int) 
#hcount = [0] * 10
lettercount = 0

def calchintext (plaintext, i):
    hcount = [0] * 13
    lettercount = 0
    #print ("lettercount", lettercount)
    plaintextlength = len (plaintext)
    #print ("plaintextlength", plaintextlength)

    #print ("plaintext", plaintext)
    Lplaintext = list (plaintext)
    #print ("Lalphabet[i]", Lalphabet[i])
    #print ("Lplaintext", Lplaintext)
    for j in range(plaintextlength):
        if Lplaintext [j] == ' ' or Lplaintext [j] == ',' or Lplaintext [j] == ':' or Lplaintext [j] == '?':
           lettercount = 0
           #print ("пробел найден")
           continue  
        if Lplaintext [j] == Lalphabet[i]: 
            #print ("hcount=", hcount[i][lettercount])
            hcount[lettercount]+=1 
            lettercount+=1
            #print ("i=", j)
            #print ("hcount+1=", hcount[i][lettercount])
            continue
        else: 
            #print ("lettercount=",lettercount)
            lettercount+=1
            #print ("lettercount+1=",lettercount)
    return hcount

a=0
for a in range (14): #запусткаем цикл по строкам
    i=0
    temphhcount = [0] * 13
    #print ("PPLAINTTEXT", pplaintext[a])
    for i in range (allength): #запускаем цикл по буквам алфавита
        
        #hhcount [i]  = 
        temphhcount = calchintext (pplaintext[a], i) #вот эта адова строка
        print ("For letter: ", Lalphabet [i], " lettercount is:", hhcount[i])
        j=0
        #print ("temphhcount = ", temphhcount)
        for j in range (13):
            #value = hhcount[a][j] + temphhcount [j]
            #position = int(10 * a + j)
            #numpy.put(hhcount, [position], [value])
            hhcount[i][j] += temphhcount [j]
            

    #print (hcount)


print(np.matrix(hhcount))