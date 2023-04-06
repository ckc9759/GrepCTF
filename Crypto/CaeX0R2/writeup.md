### Chall name : CaeX0R2

---

#### Desc : Ooops, i forgot the shift this time. Can you still figure out my flag.

Flag Format : GREP{}

```py
#enc.py
from random import *
flag="REDACTED"
a=randint(1,1000)
c=[]
for f in flag:
   c.append(str(ord(f)^a))
print(c)
print(a)

#c=['313', '296', '295', '304', '274', '280', '263', '280', '263', '310', '315', '310', '316', '345', '268', '263', '310', '302', '345', '296', '276']
#a=REDACTED
```

### Solution

'c' contains our cipher text from a previous run of enc.py
first we try to reverse the XOR operation since it was done with a
random number we will have to use brute force to try out all possible
values of i same as we did in CaeXOR:
```PY
    c= ['313', '296', '295', '304', '274', '280', '263', '280', '263', '310', '315', '310', '316', '345', '268', '263', '310', '302', '345', '296', '276']
    for  i  in  range(1,1000):
        print(i,"".join([chr(int(x)^i) for  x  in  c]))
        #this displays the c one by one XORed with 1 -> 1000
```

here looking at the output of our above loop we find that with key 361 
we find a text which resembles our Flag format GREP{} : -

PANY{qnqn_R_U0en_G0A}

Alternatively,

```py
from random import *
c=['313', '296', '295', '304', '274', '280', '263', '280', '263', '310', '315', '310', '316', '345', '268', '263', '310', '302', '345', '296', '276']
enc=[int(m) for m in c]
flag=""
a=1
temp2=[]
while a<=1000:
   k=chr(enc[0]^a)
   temp=""
   if k.isalpha():
      for e in enc:
        temp+=chr(e^a)
      if temp[4]=='{':
        key=a
        temp2.append(temp)
   else:
      print(f"Not found, key ={a}")
   a+=1
print(temp2)
print(f"Key is {key}")
z=temp2[0]
print(z)
ans1=""
ans2=""
print(chr((ord(z[0])-9)))
for c in z:
   ans1+=chr((ord(c)-9))
   ans2+=chr((ord(c)+17))
   
print(ans1)
print(ans2)
```

for our flag to be valid PANY must correspond to GREP, which is only possible with shift = 17 

### FLAG : GREP{hehe_I_L0ve_X0R}
