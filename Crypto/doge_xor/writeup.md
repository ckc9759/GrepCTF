### Challenge Name : DOGE DOGE DOGE

### Description : Doge

Author - @FusterCluck

FLAG FORMAT: grepCTF{...}

```py
from Crypto.Util.number import *
from pwn import xor
flag = b'REDACTED'
key = b'REDACTED'
enc = b''
for i in range(len(flag)):
    enc += xor(key[i], flag[i])
print(enc)
# b'#="5\x07\x1b\x01>4#s<u! \x1a3~3-\x1b7w7\x1b&4\x1a":)8'
```

### Solution 

XOR is a reversible process; if you XOR the result with the same 2-byte array you used in the first example, you will get back the original. Using this fact we can figure out the message by XORing the key with the ciphertext. 

The challenge presents us with only one word "DOGE" since this is our only hint. We try to use the DOGE as the key.

```py
ct = b'#="5\x07\x1b\x01>4#s<u! \x1a3~3-\x1b7w7\x1b&4\x1a":)8'
key = "DOGE"*(len(ct)//4)

for i,j in zip(ct,key):
    print(chr(i^ord(j)),end="")

```
the above code Performs the XOR operation on the ciphertext hence outputing the flag. 

key = 'DOGEDOGEDOGEDOGEDOGEDOGEDOGEDOGE'

### Flag : grepCTF{pl4y1ng_w1th_x0r_is_fun}