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
key="Musketeer"

new_ctext=[(ord(i)^ord(j)) for i,j in zip(ctext,key)]
output=[chr(x) for x in new_ctext]
ciphertext='$'.join(output) 
print(ciphertext)

# |$E$B$[$T$D$T$T$B -> ciphertext
```
