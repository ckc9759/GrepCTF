import numpy as np
import binascii

message ="856485325862584564"

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
print(new_ctext)
print(output)
print(ciphertext)
