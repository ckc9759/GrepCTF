import numpy as np
import binascii

ct="010101111001000001001110001100110101110100111000011000001000111100100110"
key="Musketeer"

list1=[key[i] for i in range(len(key))]
m1=''
m2=''

n=len(ct)
print(n)

j=0
k=1
for i in range(72):
    if i%2==0:
        m1+=ct[j]
        j+=2
    else:
        m2+=ct[k]
        k+=2
   
print(m1)
print(m2)

ctext=''    
ctext+=m1
ctext+=m2
print(ctext)
new_list=[ctext[i:i+8] for i in range(0,len(ctext),8)]
print(new_list)
new=[int(i,2) for i in new_list]
print(new)
new = [chr(x) for x in new]
val=[ord(i)^ord(j) for i,j in zip(new,list1)]
print(val)
val=[str(x) for x in val]
message=''.join(val)
print("\n")
print(f"final message : {message}")
