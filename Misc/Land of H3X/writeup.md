### Land of H3X

> DESCRIPTION - 
Morino Idate is on the run again. Uzumaki Xoruto has promised to help him and they reach Bits Pilani 😊. Ibiki is trapped by AOI in one of the bhawans but nobody knows which one. Help Morino meet his brother ! Anbu 🥷 members have got a secret scroll 📖 but they are unable to read it.

They say it's written by the shinobis of Land of H3X. 
Only info gathered yet is they use @ to denote 'a'. 
```
---
---
---
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣠⣶⣿⣿⡿⠿⠿⠿⠿⢿⣿⣿⣷⣦⣄⣀⣤⣶⣶
⠀⠀⠀⠀⠀⣰⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⣿⣿⠟⠋
⠀⠀⠀⠀⣼⣿⡿⠃⠀⢀⣤⣾⣿⣿⣿⣿⣷⣦⣄⠀⠀⠈⠉⠀⠀⠀
⠀⠀⠀⣸⣿⡿⠁⠀⢠⣿⣿⠟⠉⠀⠈⠉⠛⢿⣿⣷⡄⠀⠀⠀⠀⠀
⠀⠀⢀⣿⣿⡇⠀⠀⣾⣿⡟⠀⠀⢀⣤⣄⠀⠀⠹⣿⣿⡄⠀⠀⠀⠀
⠀⠀⣾⣿⣿⡇⠀⠀⢻⣿⣷⡀⠀⠘⣿⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀
⠀⣼⣿⡿⣿⣿⡄⠀⠈⠻⣿⣿⣷⣿⣿⡿⠃⠀⢀⣿⣿⡇⠀⠀⠀⠀
⣰⣿⣿⠁⠹⣿⣿⣦⡀⠀⠈⠉⠛⠋⠉⠀⠀⣠⣾⣿⡟⠀⠀⠀⠀⠀
⣿⣿⣧⣤⣤⣬⣿⣿⣿⣶⣦⣤⣤⣤⣴⣶⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀
⠙⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀
Find where Ibiki is before the room catches fire !
```

> HINT : The bhawan used starts with an 's'

Author - `@ckc9759`

FLAG FORMAT: `GREP{...}`

---

### Solution 

This one was a mixture of a little bit of OSINT and forensics.

So you get a file which has hex code, if you put that on cyberchef and use `from hex`, you will get this :

![image](https://user-images.githubusercontent.com/95117634/230047629-b88847f5-511c-4d81-b719-547aef46257c.png)

The description uses word `Xoruto` which is a clear hint towards XOR operation and there was also mention of Bhawans and use of a as @.
Now there are not many bhawans in BIT Pilani.

![image](https://user-images.githubusercontent.com/95117634/230048001-3f0fba1d-b04b-4c95-be0c-59175c63c54e.png)

We can eliminate some bhawans with no `a` such as `BUDH`.
If we keep trying the keys as bhawan names, we will find that shankar makes some sense. 

![image](https://user-images.githubusercontent.com/95117634/230048615-dbd838d5-c394-4b36-9866-5236fd377b56.png)

Since, a was to be used as @, the key is sh@nk@r.

![image](https://user-images.githubusercontent.com/95117634/230048883-938ecd7e-0295-4715-950f-21c6e02a79ab.png)

Now, we get a file with headers as `BNG` and `MKDHIR` which are wrong and should be replace with `PNG` and `IHDR`.
You can read about it over [here](https://hackmd.io/@FlsYpINbRKixPQQVbh98kw/Bk9Wj63vH)

After using any online hex editor or the command `hexedit` in linux, we fix the above hex codes. Moreover, the desc talks abt idate and if u look closely IDAT chunk is 
written as IPAT and that should also be fixed.

If you fix all these correctly, an image will be rendered containing flag in jumbled words

![](Bhawan.png)

---

Flag : GREP{H3x_H3x_c@N_B3!_FUN}

Thank you

