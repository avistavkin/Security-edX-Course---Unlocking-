
import time
"""
import sys # ignore
sys.path.insert(0,'.') # ignore
#from Root.pswd import real_password
"""
real_password = "9999999998"

print (real_password)
password = "9998"
lenpass = len(password)
print (lenpass)
"""
if len(password) == len(real_password):
    print ("equal")
else:
    print ("not equal")
"""


password = [0,0,0,0,0,0,0,0,0,0]

start = time.perf_counter()
for i in range(len(password)):
        for j in range(10):
            password[i] = j
            print (password)
            x=(''.join(map(str,password)))
            if x == real_password:
                print ("found")
                break
            else: 
                print (x)
                print (real_password)
            """
            start = time.perf_counter()
            check_password(password)
            finish = time.perf_counter() - start
            x=(''.join(map(str,password)))
            if finish>z or check_password(x)==True:
                z+=.1
                break

"""
finish = time.perf_counter() - start
print (finish)    
"""


#print ("passwords are not equal")
"""