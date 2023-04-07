### Doctored image

> DESCRIPTION -
Help, my images are all corrupted!!

Author - `@FusterCluck`

FLAG FORMAT: `grepCTF{...}`

---

### Solution 

We get a jpg file which doesn't open. It seems it's correupted.

![image](https://user-images.githubusercontent.com/95117634/230551113-39aafa14-0674-4677-a9db-5bdbfdfa575a.png)

Using a [hexeditor](https://hexed.it/) to view the hex code of the file, 

![image](https://user-images.githubusercontent.com/95117634/230551526-1cb50cbb-d8ee-44f0-8b5d-1c010120f7f3.png)

Now, we will find the jpg magic number which is the actual hex 

![image](https://user-images.githubusercontent.com/95117634/230555783-e271b396-c917-4d94-b655-ce2eb08e3403.png)

So, we see it's `ff d8 ff`. On changing the hex and saving the new image, we get our flag !!
![image](https://user-images.githubusercontent.com/95117634/230555872-a0aee698-408b-41ad-b67d-3091f2a7a43a.png)

Flag : grepCTF{m00n_kn1ght}

---

Thank you
