import hashlib

plaintext = "Hello, world!"



result = hashlib.md5(plaintext.encode()) 
  
# printing the equivalent byte value. 
print("The byte equivalent of MD5 hash is : ", end ="") 
print(result.digest()) 

print("The hexadecimal equivalent of MD5 hash is : ", end ="") 
print(result.hexdigest()) 



result = hashlib.sha1(plaintext.encode()) 
  
# printing the equivalent byte value. 
print("The byte equivalent of SHA1 hash is : ", end ="") 
print(result.digest()) 

print("The hexadecimal equivalent of SHA1 hash is : ", end ="") 
print(result.hexdigest()) 


result = hashlib.sha256(plaintext.encode()) 
  
# printing the equivalent byte value. 
print("The byte equivalent of SHA256 hash is : ", end ="") 
print(result.digest()) 

print("The hexadecimal equivalent of SHA256 hash is : ", end ="") 
print(result.hexdigest()) 


#как альтернатива - коротко, одной строкой

print(hashlib.sha256(b"Hello, world!").hexdigest())

"""
m = hashlib.sha256()
m.update(b"Nobody inspects")
>>> m.update(b" the spammish repetition")
>>> m.digest()
b'\x03\x1e\xdd}Ae\x15\x93\xc5\xfe\\\x00o\xa5u+7\xfd\xdf\xf7\xbcN\x84:\xa6\xaf\x0c\x95\x0fK\x94\x06'
>>> m.digest_size

"""