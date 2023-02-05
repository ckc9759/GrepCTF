import numpy as np
import PIL.Image

message="GVNJ{B1ur_c4u_f3a_lman}"

image = PIL.Image.open('mem2.png','r')
width,height=image.size

img_array = np.array(list(image.getdata()))

channels = 4 if image.mode=="RGBA" else 3

pixels = img_array.size // channels

stop_indicator="$ckc$"
stop_length=len(stop_indicator)

message+=stop_indicator

byte_message=''.join(f"{ord(c):08b}" for c in message)
bits = len(byte_message)

if bits>pixels:
   print("Not enough space")
else:
   index=0
   for i in range(pixels):
      for j in range(0,3):
         if index<bits:
            #ob100111011
            img_array[i][j]=int(bin(img_array[i][j])[2:-1]+byte_message[index],2)
            index+=1
   
img_array=img_array.reshape((height,width,channels))
result=PIL.Image.fromarray(img_array.astype('uint8'),image.mode)
result.save('encoded.png')            
