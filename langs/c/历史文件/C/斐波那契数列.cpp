/*
对于斐波那契数列1、1、2、3、5、8、13、……。有如下定义
F(n)=f(n-1)+f(n-2)
F(1)=1
F(2)=1
对于以下矩阵乘法
F(n+1) = 11 F(n)
F(n) 10 F(n-1)
*/

#include <stdio.h>

int main()
{
    int n, i , f1 , f2 , f3 ;

    f1 = 1 ;
    f2 = 2 ;
    scanf ("%d", &n);
    if(n == 1)
    {
        f3 = 1;
    }

    else if(n == 2)
    {
        f3 = 2;
    }

    else
    {
        for(i = 3; i <= n; ++i)
        {
            f3 = f1 + f2;
            f1 = f2;
            f2 = f3;

        }
    }


    printf("%d", f3);
    return 0;
}
