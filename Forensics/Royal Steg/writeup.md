### Royal Steg

> DESCRIPTION -
Then Jesus turned, and seeing them following, said to them, 'what do you SEEK?

- JOHN 1:38

FLAG FORMAT: `grepCTF{...}`

---

### Solution 

It's a steganography challenge indicated by challenge name and we have a word SEEK in caps which also looks some kind of hint. 

Searching on google words like steg and seek, you will come accross a tool called stegseek which can be used to find passwords used for hiding data using steghide.

Here is the walkthrough on how to solve the challenge !!

Step 1. Use the command stegseek with a known wordlist like rockyou.txt

![image](https://user-images.githubusercontent.com/95117634/230293813-88f709f2-cbb3-44b1-8bd7-2e16cd667c5d.png)

Step 2. Find the password of zip file by renaming the extension and using a zip password cracking tool. In my case `fcrackzip`, but `john` is more powerful.

![image](https://user-images.githubusercontent.com/95117634/230293994-19e9a618-75d8-44df-b2ad-8f133559c2ad.png)

Once you find the password, it's just flag.txt and cat it out to get the flag.

Flag : grepCTF{tw0_l3v3ls_0f_st3g}

---

Thank you
