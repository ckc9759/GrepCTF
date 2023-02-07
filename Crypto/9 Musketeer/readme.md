### Challenge name - Nine Musketeers

Our Captain is missing. He was on a search for new Army Bases, but lost hist path. Can you help him come back !!
Find the path to decode the message

Message.txt
```txt
L1c2NEZFTTJENEpBK0RCNkI3R0tFVjJFVkRCQjNEMVo4QlM2QTlGNjFCOUFGRjZBJThGRlpBUDhEWjNGN0ZFSyU2VjQ3SVI2K05BV0lBUlk5OjNFOFo4NVQ4LjNFSSU2RTdBICBEWVpBOlE2N1g2NjdCVEVESFdFTCtBKis4WlM4RFo5L0c2JDY5SFM4SzFCOFFFNUI2MEpBN1FERlQ4SVQ4RUNBV044S0I4OFZDVkE2Ki1DWi5ESUNCTkNBJSo5U0RCTVM2K0I3MzNFTlRBNTdBVFBENkVESkc2SlRBIDZBWjU5OElBSUg4UEVEMCo2RFQ4ODFCJERCMEVCIEZGRVM2U045Kzo2ICRFTEg5LUNDK0g5JCo4WjdESiRFTTU3OEtFU0Y2WlpDNSo2SzE=
```

```py
#path.py
# path.py
import numpy as np
import binascii

message = "REDACTED"
key = "Musketeer"

list = [message[i : i + 2] for i in range(0, len(message), 2)]
list = [eval(i) for i in list]

list2 = [key[i] for i in range(len(key))]

# print(list)
# print(list2)

val = [chr(x) for x in list]
# print(val)

new = [ord(i) ^ ord(j) for i, j in zip(list2, val)]
# print(new)

new_list = []
new_list2 = []
for word in new:
    c = 0
    if word >= 1:
        new_list.append(format(word, "08b"))

ctext = "".join(new_list)

# print(ctext)
cipher = [ctext[i : i + REDACTED ] for i in range(0, len(ctext), REDACTED)]
m1 = cipher[0]
m2 = cipher[1]
# print(m1)
# print(m2)
m3 = []
j = 0
k = 0
for i in range(2 * len(m1)):
    if i % 2 == 0:
        m3.append(m1[j])
        j += 1
    else:
        m3.append(m2[k])
        k += 1
m3 = "".join(m3)
print(m3)

# 010101111001000001001110001100110101110100111000011000001000111100100110 -> m3
```
