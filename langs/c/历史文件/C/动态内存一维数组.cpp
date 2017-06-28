#include<stdio.h>
#include<malloc.h>
int main()
{
    int len;
    printf("输入的个数");
    scanf("%d", &len);
    int *pArr = (int *)malloc(4 * len) ; //分配额4*len字节的空间

    int i;
    for(i = 0 ; i < len ; i++)
        scanf("%d", &*(pArr + i )); //等价于pArr[i]


    for(i = 0 ; i < len ; i++)
        printf("%d\n", *(pArr + i));

    return 0;
}
