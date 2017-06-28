#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main()
{
    char d[20] = "shutdown -s -t ";
    char* s = "3000";
    system("cls");
    strcat(d,s);
    printf("%s",d);
    system(d);
    return 0;
}
