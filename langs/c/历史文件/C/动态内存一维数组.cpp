#include<stdio.h>
#include<malloc.h>
int main()
{
    int len;
    printf("����ĸ���");
    scanf("%d", &len);
    int *pArr = (int *)malloc(4 * len) ; //�����4*len�ֽڵĿռ�

    int i;
    for(i = 0 ; i < len ; i++)
        scanf("%d", &*(pArr + i )); //�ȼ���pArr[i]


    for(i = 0 ; i < len ; i++)
        printf("%d\n", *(pArr + i));

    return 0;
}
