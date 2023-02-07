### Challenge name -

```py
import numpy as np
import binascii

message =<<<redacted>>>

list=[]

list=[message[i:i+2] for i in range (0,len(message),2)]
list = [eval(i) for i in list]

# print(list)

new_list=[]
for word in list:
   c=0
   if word>=1:
      new_list.append(bin(word).replace("0b",""))

ctext=''.join(new_list)
key="Chaitanya@"

new_ctext=[(ord(i)^ord(j)) for i,j in zip(ctext,key)]
output=[chr(x) for x in new_ctext]
ciphertext='$'.join(output) 
print(ciphertext)

# r$X$P$Y$E$Q$_$H$Q$p -> ciphertext
```
