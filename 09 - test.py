data = bytes(plain_text,"utf-8")

key = get_random_bytes(32)
iv = get_random_bytes(16)

cipher = AES.new(key, AES.MODE_CBC, iv)
ct_bytes = iv + cipher.encrypt(pad(data,16))
return ct_bytes, key