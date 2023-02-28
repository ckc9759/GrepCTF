import os
# Flag is in ./secret/flag.txt
print('-'*10)
print(open(__file__).read())
print('-'*10)
while(True):
    x = input('>>> ')
    whitelist = ['0','1','2','3','4','5','6','7','8','9','/','*','?','$','.',"'",'!','@','#']
    for i in range(11):
        whitelist += whitelist[i].upper()
    if any ([i for i in x if i not in whitelist]):
        print("Hacking detected! Exiting")
        exit(0)
    else:
        os.system(x)