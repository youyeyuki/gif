#include <stdio.h>
void str2(int num, int i)
{
    int N;
    if('A' <= num && num <= 'Z' )
        N = 90;
    else if('a' <= num && num <= 'z')
        N = 122;

    if (N - 26 < num && num <= N - 26 - i)
        num = num + 26 + i;
    else if(N - 26 - i < num && num <= N )
        num = num + i ;

    printf("%c", num);
}
int main()
{

    int i, guess = -1;
    char *s = "flag{5cd1004d-86a5-46d8-b720-beb5ba0417e1}";
    char *p = s;
    while(guess >= -26)
    {
        printf("%d    ", guess);
        while(*s != '\0')
        {
            i = *s;
            str2(i, guess);
            s++;
        }
        printf("\n\n");
        s = p;
        guess--;

    }

}

