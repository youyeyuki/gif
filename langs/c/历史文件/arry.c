#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{

    int a = 123;
    int arrLen, i;
    int *array;
    printf("�������鳤�ȣ�");
    scanf("%d", &arrLen);

    array = (int *)malloc(arrLen * sizeof(int));
    if (!array)
    {
        printf("��������ʧ��");
        exit(1);
    }
    for(i = 0; i < 3 ; i++)
    {
        array[i] = a % 10;
        a = a / 10 ;
    }

    
    for(i = 0 ; i < 3 ; i++ )
        printf("%d\n", array[i]);
        
        

}
