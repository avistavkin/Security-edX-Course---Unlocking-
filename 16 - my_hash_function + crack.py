"""
Implement a hash function simple_hash that given a string s, 
computes its hash as follows: it starts with r = 7, 
and for every character in the string, multiplies r by 31, adds that character to r, 
and keeps everything modulo  216 .

"""
import itertools

def simple_hash(s):
    r = 7
    for c in s:
        r = (r * 31 + ord(c)) % 2**16

    return r

def crack(s):
    plaintextlenght = len(s)
    hashs = simple_hash(s)
    lista = list(itertools.product("abcdefghijklmnopqrstuvwxyz",repeat=plaintextlenght))
    for i in lista:
        s2 = ''.join(map(str, i))
        if s2 == s: continue
        else:
            hashs2 = simple_hash(s2)
            if hashs2 == hashs: break

    return s2



s = input('String...: ')

hashs = simple_hash(s)

print ("Hash s:", hashs)

s2 = crack (s)

print ("Collition%", s2)

hashs2 = simple_hash(s2)

print ("Hash s2:", hashs2)



