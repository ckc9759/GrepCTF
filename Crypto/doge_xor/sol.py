from pwn import xor
enc = b'#="5\x07\x1b\x01>4#s<u! \x1a3~3-\x1b7w7\x1b&4\x1a":)8'
part_flag = b'grepCTF{'
part_key = b''
key = b''
msg = b''

for i in range(len(part_flag)):
    part_key += xor(part_flag[i], enc[i])
print(f'Key: {str(part_key)}')
key = part_key * 4

msg = xor(enc, key)

print(f'Message: {msg}')