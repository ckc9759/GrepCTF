### CaeX0R

> DESCRIPTION
I pressed shift key 10 times and lost the flag. Can you find my flag.

> HINT : Xor is reversible and u know flag format !

Author - `@ckc9759`

FLAG FORMAT: `GREP{...}`

---

### Solution 
the Challenge starts with a hint given below and a file enc.py which was
used to encrypt the cipher : \> I pressed shift key 10 times and lost
the flag. Can you find my flag.

enc.py :
```PY
#enc.py
from  random  import  *
flag="REDACTED"
a=randint(1,1000)
c=[]
for  f  in  flag:
c.append(str(ord(f)^a))
print(c)
print(a)
#c=['162', '177', '188', '169', '136', '187', '138', '145', '172', '187', '138', '145', '172', '190', '152', '156', '187', '195', '177', '142']    
#a=REDACTED
```

'c' contains our cipher text from a previous run of enc.py
first we try to reverse the XOR operation since it was done with a
random number we will have to use brute force to try out all possible
values of i :
```PY
    c  = ['162', '177', '188', '169', '136', '187', '138', '145', '172', '187', '138', '145', '172', '190', '152', '156', '187', '195', '177', '142']
    for  i  in  range(1,1000):
        print(i,"".join([chr(int(x)^i) for  x  in  c]))
        #this displays the c one by one XORed with 1 -> 1000
```

here looking at the output of our above loop we find that with key 243
we find a text which resembles our Flag format GREP{} : -

QBOZ{Hyb_Hyb_MkoH0B}

Now remeber the hint given to us in the description of the challenge I
pressed shift 10 time - we can infer that we may have to use shift
cipher with a key 10.

decoding the shift cipher using key = 10 we get -
### flag : - GREP{Xor_Xor_CaeX0R}
