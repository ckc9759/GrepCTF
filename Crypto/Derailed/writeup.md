### Challenge Name - Derailed

### DESC - You have pwned a Railway website's database. You have the password.txt file which contains the password of their users in the line corresponding to the user ID. An Evil Scientist that goes by the name of Mr. Fence took 4 rails to his different labs. You want to find out his password so that you know where he is headed next. You have to find him fast and apprehend him otherwise the whole world rots. If I tell you his user ID is the 75th prime number - 1, Will You be able to save the world?

### Solution 
We know that password.txt contains the passwords of all users in encrypted format. 
Each of these passwords are stored in lines corresponding to the user ID. we know that Mr.fence's 
User Id is 75th prime number - 1 = 378 

on line number 378 we find the encrypted password : T_OF}ENI_NNfqR{rlQcjeCe_B

In the challenges we are hinted towards railway stations, suggesting that rail fence cipher may be used.
We know Mr. Fence took 4 rails, implying that key = 4

https://www.boxentriq.com/code-breaking/rail-fence-cipher 
using the above website to solve the rail cipher with key = 4 
we get another cipher text : TERC{N_Irel_ONQ_cNFfjBeq}

Now, it is indicated that the whole world may rot if the scientist isn't stopped, only cipher that comes to mind is ROT13

decoding the ROT13 cipher we get :

### FLAG : GREP{A_Very_BAD_pASswOrd}

