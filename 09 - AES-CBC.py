#!/usr/bin/env python3
#
# This is a simple script to encrypt a message using AES
# with CBC mode in Python 3.
# Before running it, you must install pycryptodome:
#
# $ python -m pip install PyCryptodome
#
# Author.: José Lopes
# Date...: 2019-06-14
# License: MIT
##
import itertools
import sys # ignore

import time

from hashlib import md5
from base64 import b64decode
from base64 import b64encode

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


class AESCipher:
    def __init__(self, key):
        self.key = md5(key.encode('utf8')).digest()

    def encrypt(self, data):
        iv = get_random_bytes(AES.block_size)
        self.cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return b64encode(iv + self.cipher.encrypt(pad(data.encode('utf-8'), 
            AES.block_size)))

    def decrypt(self, data):
        raw = b64decode(data)
        self.cipher = AES.new(self.key, AES.MODE_CBC, raw[:AES.block_size])
        return unpad(self.cipher.decrypt(raw[AES.block_size:]), AES.block_size)


if __name__ == '__main__':
    print('TESTING ENCRYPTION')
    #msg = input('Message...: ')
    msg = "abcdefgh"
    #pwd = input('Password..: ')
    pwd = "ahhhhhh"
    cte = AESCipher(pwd).encrypt(msg).decode('utf-8')
    print('Ciphertext:', cte)
    #print('Ciphertext:', AESCipher(pwd).encrypt(msg))

    print('\nTESTING DECRYPTION')
    #cte = input('Ciphertext: ')
    #pwd = input('Password..: ')
    listb = list(itertools.product("abcdefgh",repeat=7))
    start_time = time.time()
    for i in listb:
        try:
            #pwd = "".join(i)
            pwd = ''.join(map(str, i))
            print ("pwd", pwd)
            #pwd = ''.join(str(e) for e in listb)
            #print (i)
            #print (listb[0])
            plaintext = AESCipher(pwd).decrypt(cte).decode('utf-8')
            #plaintext = AESCipher(pwd).decrypt(cte)
            print ("Bingo! Plaintest:", plaintext)
            break
        except ValueError: print("Oops!  That was no valid key.", pwd, " Try again...")
    """
    if (is_english(plaintext)): 
    #print('Message...:', AESCipher(pwd).decrypt(cte).decode('utf-8'))
        print (plaintext)
    else: print ("Text not muched") 
    """
    print("--- %s seconds ---" % round((time.time() - start_time), 4))
    print ("the end")