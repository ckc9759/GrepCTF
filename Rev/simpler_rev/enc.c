#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    char buf[100];
    printf("Enter flag: ");
    scanf("%s", buf);

    if (strcmp(buf, "grepCTF{sample_flag}") == 0)
        puts("Correct flag\n");
    else
        puts("Wrong flag\n");
}