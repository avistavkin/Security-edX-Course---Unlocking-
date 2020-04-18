src = "Hello, World!"
code = "secret"
xorWord = lambda ss,cc: ''.join(chr(ord(s)^ord(c)) for s,c in zip(ss,cc*100))
encrypt = xorWord(src, code)
print ("Encrypt: ", encrypt)
decrypt = xorWord(encrypt,code)
print (decrypt)


