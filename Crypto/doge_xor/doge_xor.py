from Crypto.Util.number import *
from pwn import xor
# flag = b'grepCTF{pl4y1ng_w1th_x0r_is_fun}'
# key = b'DOGEDOGEDOGEDOGEDOGEDOGEDOGEDOGE'
flag = b'REDACTED'
key = b'REDACTED'
enc = b''
for i in range(len(flag)):
    enc += xor(key[i], flag[i])
print(enc)
# b'#="5\x07\x1b\x01>4#s<u! \x1a3~3-\x1b7w7\x1b&4\x1a":)8'