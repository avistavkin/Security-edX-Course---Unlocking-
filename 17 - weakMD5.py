import hashlib


def weak_md5(s):
    return hashlib.md5(s).digest()[:5]


def find_collisions():
    return # return (s1, s2) such that s1 != s2 and weak_md5(s1) == weak_md5(s2)




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

hashs = weak_md5(s.encode())


print("The hexadecimal equivalent of MD5 hash is : ", end ="") 
print(hashs) 


"""
import hashlib


def weak_md5(s):
    return hashlib.md5(s).digest()[:5]


def find_collisions():
    import itertools
    hsh = []
    st = []
    for i in range(1,37):
        l = list(itertools.product('abcdefghijklmnopqrstuvwxyz0123456789',repeat = i))
        for s in l:
            s = ''.join(s)
            h = weak_md5(s.encode())
            if h in hsh:
                s0 = st[hsh.index(h)]
                rt = (s0, s)
                return rt
            hsh.append(h)
            st.append(s)

"""