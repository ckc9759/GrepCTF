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