### SEM A4

> DESCRIPTION
Huhhh, finally Sèm brèak ! Timè to play some Valorant, but I've misplacèd my keys. I prèssèd shift walk, still thèy hèard me 😞. It isn't Right. Can't find my WASD kèys, hèlp hèlp... My rank is going down and down.

> HINT : 2 Encrypted parts, find them decode them conquer the challenge !

Author - `@ckc9759`

FLAG FORMAT: `GREP{...}`

---

### Solution 

We have two files, there is a png file with some kind of `Symbol Cipher` and a message again. The message seems to be gibberish and if you use any cipher identifier, it will direct you to a
keyboard shift cipher.

![image](https://user-images.githubusercontent.com/95117634/230008673-6b9e4b5f-41bf-4f05-8c94-a7ce6737c430.png)

Now, there is a string 'SEMBREAK' in cipher which indicates that there are two parts and you need to split it from there.

So the two ciphertexts become :

```c
C1 = "§ab< sp sa^hu huush oa :u $! oia^:uW Bmp $h omu :toouip jutj tqq omu o$suW £ bt!o !ub a!uh xX 567890+1 laaaa< Pa^ bt!o oa zqtp quo_h
zqtp Ztio 5 x moozhxXXja,hWlaalquW,asXja,^su!oXjX50B.m°kµu:SgU=sn+.ù^/?JuS%5£i§7.6%7=;Gm"

C2 = "OI96Z0UaNQIhhP91c3F9q2byuqxuEk=="
```

If it doesn't click you over here, try decoding the whole string with keyboard shift cipher and you see you get part 1, so obviously you've a part 2 as well. 

![image](https://user-images.githubusercontent.com/95117634/230009322-edadcca0-c40f-4580-8bcb-252a6041bee1.png)

If you notice the use of è in desc , you will realise it hints towards a french keyboard and `A` is for Azerty and `4` is the shift. The word `Right` mentioned in description
tells you about shifting towards right. 

I prèssèd `shift` walk, still thèy hèard me 😞. It isn't `Right`. --> Desc

---

Now, the drive link won't work as u need a part 2 as well. So here is the role of that image ![Dancing.png](Dancing.png)

The cipher is Flag Semaphore cipher (SEM A4 sounds the same), which will give a keyword - `SEMAFOUR`.

Now the second part C2, it's encoded by a french cipher named `Vigenère`, decoding which gives the second part : `XOz7E/edit?usp=sharing`

![image](https://user-images.githubusercontent.com/95117634/230010831-df257e89-8f91-43af-9ed5-2500cf0fc9f3.png)

Concatenate both the parts and you will get the drive link : https://docs.google.com/document/d/16WVh7fKebMqE_mx8VjuBCDeMJ1IrN3V2J3_vQhXOz7E/edit?usp=sharing

![image](https://user-images.githubusercontent.com/95117634/230011121-b7b56527-bd41-487c-a5f3-b7ec98bf23d0.png)

Flag is in the Title : ***GREP{B4ttl3_S@ge}***

---

Thank you


