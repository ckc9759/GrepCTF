# Uneasy alliance
> quasar | 17-3-2023

# Description
You have seen people giving out p, q values and asking you to decrypt the cipher text. This time, you only have the cipher text. Good luck decrypting!

# Code

```py
from Crypto.Util.number import *
import math
import time
from random import Random

seed = math.floor(time.time())
rnd = Random(seed)

rand_fn = lambda n: long_to_bytes(rnd.getrandbits(n))
p = getPrime(128, randfunc=rand_fn)
q = getPrime(128, randfunc=rand_fn)
e = 65537
n = p * q

assert p != q

m = bytes_to_long(b"GREP{REDACTED}")
ct = pow(m, e, n)
print("Cipher text:", ct)
# Cipher text: 9898717456951148133749957106576029659879736707349710770560950848503614119828
# Seed: REDACTED
```

# Solution
`flag`: `GREP{Brut3D_M3!_f0r_l1f3}`
`seed`: `1679038148`