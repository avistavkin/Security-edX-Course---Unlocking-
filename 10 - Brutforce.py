
from hashlib import md5
from base64 import b64decode
from base64 import b64encode

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
#from Crypto.Cipher import AES
#from Crypto import Random
import itertools
import sys # ignore
sys.path.insert(0,'.') # ignore
#from Root.prev_func import aes_decrypt, is_english



class AESCipher:
    def __init__(self, key):
        self.key = md5(key.encode('utf8')).digest()

    def encrypt(self, data): # data - это текст
        iv = get_random_bytes(AES.block_size)
        self.cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return b64encode(iv + self.cipher.encrypt(pad(data.encode('utf-8'), 
            AES.block_size)))

    def decrypt(self, data):
        raw = b64decode(data)
        self.cipher = AES.new(self.key, AES.MODE_CBC, raw[:AES.block_size])
        return unpad(self.cipher.decrypt(raw[AES.block_size:]), AES.block_size)


    def brute_force_aes(ciphertext):
        block_size = 16
        PADDING = '0'
        pad = lambda s: s + (block_size - len(s) % block_size) * PADDING    
        lista = list(itertools.combinations_with_replacement("0123456789",6))
        for i in lista:
            k =  pad('036'+''.join(i))

            plaintext = decrypt(k, ciphertext)

            if (is_english(plaintext)): 
                print ("Key: ",k)
                print ("Plaintext: ", plaintext)
                return plaintext

if __name__ == '__main__':
#Производя подобную проверку, вы можете сделать так, что код будет исполняться только при условии, что данный модуль запущен как программа, и запретить исполнять его, если его хотят импортировать и использовать функции модуля отдельно.
    print('TESTING ENCRYPTION')
    #msg = input('Message...: ')
    msg = "036000000"
    #pwd = input('Password..: ')
    pwd = "test"
    ciphertext = AESCipher(pwd).encrypt(msg).decode('utf-8')
    print('Ciphertext:', AESCipher(pwd).encrypt(msg).decode('utf-8'))


    brute_force_aes(ciphertext)

    print('\nTESTING DECRYPTION')
    cte = input('Ciphertext: ')
    pwd = input('Password..: ')
    print('Message...:', AESCipher(pwd).decrypt(cte).decode('utf-8'))