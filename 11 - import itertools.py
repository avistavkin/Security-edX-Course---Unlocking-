import itertools
import sys # ignore

s = "lkjlkjlkjlkjlkjlkjdgdfgdfgdfgd"
block_size = 16
PADDING = '0'
pad = lambda s: s + (block_size - len(s) % block_size) * PADDING    
print (pad)
lista = list(itertools.combinations_with_replacement("012",3)) #классная функция по подстановке

print (lista)

listb = list(itertools.product("012",repeat=3)) #А эта еще класнее!!!! классная функция по подстановке

print (listb)



