#include <stdio.h>

#include <stdlib.h>
void main()
{
    void move(int [20], int, int);
    int number[20], n, m, i;
    printf("how many number?");
    scanf("%d", &n);
    printf("input %d number:", n);
    for(i = 0; i < n; i++)
        scanf("%d", &number[i]);
    printf("how many place you want move?");
    scanf("%d", &m);
    move(number, n, m);
    printf("Now,they are: \n");
    for(i = 0; i < n; i++)
        printf("%d", number[i]);
    printf("\n");
}
void move(int arry[20], int n, int m)
{
    int *p, arry_end;
    arry_end = *(arry + n - 1);
    for (p = arry + n - 1; p > arry; p--)
        *p = *(p - 1);
    *arry = arry_end;
    m--;

    if(m > 0)
        move(arry, n, m);
}
