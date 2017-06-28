#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int *array = NULL;
    int *a = NULL ;
    int len, i;
    printf("输入数组个数");
    scanf("%d", &len);
    printf("%d ",len);
     
    array = (int *)malloc(len * sizeof(int));
    for(i = 0; i < len; i++)
        scanf("%d", &array[i]);

     if (!array)
    {
        printf("创建数组失败");
        exit(1);
    }
    for(i = 0; i < len; i++)
    printf("%d", array[i]);
    return 0;
}
