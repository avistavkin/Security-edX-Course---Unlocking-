"""
import hashlib

"""
def weak_md5(s):
    return hashlib.md5(s).digest()[:5]
"""

def find_collisions():
"""

import hashlib
import itertools

st = "test"
hsh = weak_md5(st.encode())
print ("st:", st)
print ("hsha:", hsh)

#    hsh = []
#    st = []
for i in range(1,37): 
        print (i)
        l = list(itertools.product('abcdefghijklmnopqrstuvwxyz0123456789',repeat = i))
#        print (l)
        
        for s in l:
            s = ''.join(s)
            h = weak_md5(s.encode())
#            print ("hshb:", h)
           
#            if str(h) == str(hsh): #по идее проверяет вхождение подстроки в строку
            if h in hsh:
                s0 = st[hsh.index(h)]
                print ("s:", s)
                print ("s0:", s0)
                print ("hshb:", h)
                rt = (s0, s)
#      break
 #               return rt

#hsh.append(h)
#st.append(s)


"""

s = input('String...: ')

hashs = weak_md5(s.encode())


print("The hexadecimal equivalent of MD5 hash is : ", end ="") 
print(hashs) 

s2 = find_collisions()

print ("s2 = ", s2)

"""