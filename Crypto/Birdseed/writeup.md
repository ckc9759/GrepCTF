### Birdseed

![image](https://user-images.githubusercontent.com/95117634/230303137-323105cd-7559-40ab-9b6a-bfae60d544a0.png)

seed() function

---

### Solution

Find the seed and decode the message.

sol.py
```py
import random

enc = open('out.txt').read()
nums = []

for i in range(0, len(enc) - 1, 2):
    nums.append(int(enc[i] + enc[i + 1], 16))
    
partial_flag = 'grepCTF{'

for i in range(1000):
    flag_check = ''
    random.seed(i)
    for j in range(8):
        flag_check += chr(nums[j] ^ random.randint(0, 255))
    if flag_check == partial_flag:
        seed = i

print(f'Seed: {seed}')
random.seed(seed)    
for i in nums:
    print(chr(i ^ random.randint(0, 255)), end='')
print()
```

![image](https://user-images.githubusercontent.com/95117634/230302624-148f1f4b-95b9-4aee-ad16-c9f09a900b65.png)

Flag : grepCTF{n3v3r_tru1y_r4nd0m}

---

Thank you
