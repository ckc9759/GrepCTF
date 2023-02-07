### Challenge name - Nine Musketeers

Our Captain is missing. He was on a search for new Army Bases, but lost hist path. Can you help him come back !!
Find the path to decode the message

Message.txt
```txt
MDM6JWc3Ul4kLDZvN00lLm11XV42OHFELTc5MjA0PF5dOEAxSU5zJDMncFAlNXJoQ20wZ1tsZDdSZjolLHJlQGA+IVl0RTZzO0I5MmIkNS8sclNkXDJiNmgpPUFWQDs3bERsIzMnb28jMkdIKGEyYFhEaTJFKyxhNjZudU04MnIrWDY5ODo5Oi5uJk4vTzs5STZTcVMpMGo2Uy89dWUmZjZxXks9PiIoa1Q6LGw/WTVyKG51PSY7N0EzJ3AsNzMoUiU4PVg+c2A4TjgxZzdTLCdmPVtQSkkvT05FNTc4P2lLPF1FTjo5MTJjTjV1OiE8OGhFRDE9I05ULTV1XWc0Njg6SkcubVpeJzc1Ul5zO2Mja183NzozOjc0VFpCNzc5RkM7RHFFPzV1MG05OWdVY3Q3NzBLczZucDhSPVtQSXQ4TzRJWTc4UGcxN2tja1I2VUVVYTNBalcjMWFHRko2cFc7KTJHWWVcNnFvWEI9I08vQDc0Z25vNjg4
```

```py
#path.py
import numpy as np
import binascii

message ="856485325862584564"
key="Musketeer"

list=[message[i:i+2] for i in range (0,len(message),2)]
list = [eval(i) for i in list]

list2=[key[i] for i in range(len(key))]

#print(list)
#print(list2)

val=[chr(x) for x in list]
#print(val)

new = [ord(i)^ord(j) for i,j in zip(list2,val)]
#print(new)

new_list=[]
new_list2=[]
for word in new:
   c=0
   if word>=1:
      new_list.append(format(word,'08b'))

ctext=''.join(new_list)

#print(ctext)
cipher=[ctext[i:i+36] for i in range(0,len(ctext),36)]
m1=cipher[0]
m2=cipher[1]
#print(m1)
#print(m2)
m3=[]
j=0
k=0
for i in range(2*len(m1)):
    if i%2==0:
        m3.append(m1[j])
        j+=1
    else:
        m3.append(m2[k])
        k+=1
m3=''.join(m3)
print(m3)

# 010101111001000001001110001100110101110100111000011000001000111100100110 -> ciphertext
```
