### Last seen beauty

> DESCRIPTION - 
Once there Was a Beautiful girl In my College but I forgot Her name. she used to live in Forty Avenue Street but no track of her now. I am blacked out !!!. All i have got is a graduation pic of our batch and some fading reminiscence of her. Sending you the picture, Capitalize on it.

> HINT : Key is hidden in plainsight !, zoom in near elbow !!

Author - `@ckc9759`

FLAG FORMAT: `GREP{...}`

---

### Solution 

The challenge name indicated towards LSB, if you search about LSB forensics or LSB steganography, you will find some writeups and blogs about a tool called `zsteg` and also a
python module named `PIL` which can be used to hide data in LSB of an image.

Dec.py script

```py
import numpy as np
import PIL.Image

image=PIL.Image.open('encoded.png','r')
img_array=np.array(list(image.getdata()))
channels = 4 if image.mode=='RGBA' else 3

pixels = img_array.size//channels

secret_bits=[bin(img_array[i][j])[-1] for i in range (pixels) for j in range(0,3)]
secret_bits=''.join(secret_bits)
secret_bits=[secret_bits[i:i+8] for i in range(0,len(secret_bits),8)]
# print(secret_bits)
secret_message = [chr(int(secret_bits[i],2)) for i in range (len(secret_bits))]
secret_message=''.join(secret_message)
stop_indicator="$ckc$" 

if stop_indicator in secret_message:
   print(secret_message[:secret_message.index(stop_indicator)])
else:
   print("Not found")
```

Either you can write a code or use the tool zsteg to get a ciphertext :

![image](https://user-images.githubusercontent.com/95117634/230290660-4b2d4c47-a038-484e-829c-425e92ddb2b4.png)

ct = `GVNJ{B1ur_c4u_f3a_lman}`

Looks like a substitution cipher but it isn't.

If we check the metadata of image using `exiftool`, we get a hint :

![image](https://user-images.githubusercontent.com/95117634/230290812-cb48c48b-694a-4103-a01d-fe048c037033.png)

It hints toward Port Royal, SC. Searching it on google you will find it's in Beaufort country. Now that's a big hint for beaufort cipher.

![image](https://user-images.githubusercontent.com/95117634/230291002-df51ba6b-9cf4-4908-905f-7a788baceb45.png)

Once you know the cipher, you need a key which can either be bruteforced using flag format and also is hidden in plainsight near the elbow in image.  

The desc words `I am blacked out !!!` is a hint for the hidden key, `capitalize on it` hints towards the LSB in challenge name and also   
`Beau`tiful girl In my College but I forgot Her name. she used to live in `Fort`y Avenue Street hints towards `Beaufort Cipher`.

Using [decode.fr](https://dcode.fr/) or [Boxentriq](https://www.boxentriq.com/code-breaking/beaufort-cipher), we can get the flag.

![image](https://user-images.githubusercontent.com/95117634/230292023-74849fc5-25a6-47f3-8c26-9894c86e3b00.png)

The hidden key in image : ![image](https://user-images.githubusercontent.com/95117634/230292159-c92949d6-0c9d-4b70-9aad-59489399daaa.png)

I know it was hard to observe but again there was bruteforce method to solve it !!

---

Thank you





