### Monke

> Description - I was playing guitar and then this monkey came and broke all my strings 😢

Author - `@FusterCluck` `@ckc9759`

FLAG FORMAT: `grepCTF{...}`

---

### Solution 

The description hints towards the use of `strings` command of linux. We can also use online steganography tools like [Aperisolve](https://aperisolve.fr/)
or [stegonline](tegonline.georgeom.net/image) to find the base64 encoded text in the file !!

base64 - `Z3JlcENURntyM2ozY3RfaHVtNG4xdHlfZzBfYjRja190MF9tMG5rM30K`

use the following command on linux to get the flag or use an online base64 decoder !

```
echo "Z3JlcENURntyM2ozY3RfaHVtNG4xdHlfZzBfYjRja190MF9tMG5rM30K" | base64 -d
```

Flag : grepCTF{r3j3ct_hum4n1ty_g0_b4ck_t0_m0nk3}

Thank you
