### 9 Musketeer

> DESCRIPTION
Our Captain is missing. He was on a search for new Army Bases, but lost hist path. Can you help him come back !! Find the path to decode the message

> HINT : There is a path message and then there is an encrypted one !! Relate

Author - `@ckc9759`

FLAG FORMAT: `GREP{...}`

---

### Solution 

There were two files given. One of them was the path and the other one was the message. 9 indicated that the message has been encrypted 9 times with a key of size 9 already 
given as `Musketeer`.

After running [dec.py](dec.py), you will get a message like this : `856485325862584564`

Output of dec.py : 

```py
72
000110000011010100100110010010110101
111101001010010111110100100000110010
000110000011010100100110010010110101111101001010010111110100100000110010
['00011000', '00110101', '00100110', '01001011', '01011111', '01001010', '01011111', '01001000', '00110010']
[24, 53, 38, 75, 95, 74, 95, 72, 50]
[85, 64, 85, 32, 58, 62, 58, 45, 64]


final message : 856485325862584564
```

Now you have a string in Message2.txt which looks like a base64 and if u split the final path in groups of two, you will get the path to reverse the encoding using different bases.

![image](https://user-images.githubusercontent.com/95117634/230007334-4179b8d7-b67d-4c8d-af59-1ce8bbfeb69e.png)

I used Cyberchef to reverse it and here's your flag : ***GREP{C4pt@in_h3ad_N0Rth}***

---

Thank you


