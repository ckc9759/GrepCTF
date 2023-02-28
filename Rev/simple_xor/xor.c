#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

// flag = grepCTF{1nd3x_w1s3_x0r}

int main(void) {
    int a;
    char flag[28];

    printf("Enter the flag: ");
    scanf("%s", flag);

    for (int i = 0; i < 23; i++)
    {
        flag[i] = i ^ flag[i];
    }

    a = strcmp((char *)flag, "gsgsGQ@|9gn8tRy>c\"Mk$gk");
    if (a == 0) {
        puts("Correct flag!");
    }
    else {
        puts("Wrong flag!");
    }
    return 0;
}