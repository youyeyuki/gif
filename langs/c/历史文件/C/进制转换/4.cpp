#include <stdio.h>
#include <string.h>
 
#define DATALENGTH 1000
 
/**
 * m 进制数转化为 2进制数 输入说明：
 * char * mm : 格式化好的m进制数(格式化方法见stoc)
 * int m : m 进制
 * int ilen : 输入字符串长度
 * bool * bb : 输出的二进制数组（需要预留足够长的空间)&&(从低位到高位排列)
 * int &olen : 输出字符串长度
 *
 */
bool mtob(char *mm,int m,int ilen,bool *bb,int &olen) // mm -> bin
{
    int mlen = 0;
    int slen = 0;
    int elen = ilen;
    bool tt;
    int now;
    bb[mlen] = mm[elen-1] % 2;
    mlen ++;
    while(slen <= elen)
    {
        tt = 0;
        for(int i = slen ; i < elen ; i ++)
        {
            now = (mm[i] + tt * m )/ 2;
            tt = ((mm[i] + tt * m )%2 == 1)? 1 : 0;
            mm[i] = now ;
        }
        bb[mlen] = mm[elen-1] % 2;
        mlen ++;
        while(mm[slen] == 0 ) slen ++;
    }
    olen = mlen-1;
    return true;
}
 
// format string
int fmtstr(char str[],int n,int len)
{
    int tt = 0;
    int i;
    int now ;
    for(i = 0 ; i < len || tt ; i ++ )
    {
        if(str[i]+tt >= n)
        {
            now = (str[i] + tt) % n;
            tt = (str[i] + tt) / n;
            str[i] = now ;
        }else
        {
            str[i] = str[i] + tt;
            tt = 0;
        }
    }
    return i > len ? i : len;
}
 
 
// 值得一提的是,我没有传递str的len,原因有2:
// 1. 由于是从低位到高位,所以str的长度必然<=tmp的长度
// 2. str已经被撸顺了,所以只撸tmp和tmp+str中需要撸的那一段即可
//   比如:(从高位到低位)
//        123456
//     +      99
// ---------------
//           555
// 虽然返回长度为3,但实际上已经被处理完毕了: 123456+99 = 123555
// 但是,在调用的时候,就要比较一下,真实长度是3还是6了
// 如果要在其他地方也参考这个函数,请务必了解这点
int addit2(char str[],int n,int level)
{
    char tmp[DATALENGTH];
    int len = 1;
    tmp[0] = 1;
    for(int i = 1 ; i < DATALENGTH ; i++) tmp[i] = 0;
    // generate a 2^level string
    for(int i = 0 ; i < level ; i ++)
    {
        for(int j = 0 ; j < len ; j ++) tmp[j] *= 2;
        len = fmtstr(tmp,n,len);
    }
    // add tmp -> str
    for(int i = 0 ; i < len ; i++) str[i] += tmp[i];
    return fmtstr(str,n,len);
}
 
 
// 二进制到N进制
bool bton(bool *bb,int n,int ilen,char *nn,int &olen) // bin -> nn
{
    for(int i =0;i<ilen;i++)
        if(bb[i]) olen = addit2(nn,n,i);
    return true;
}
 
bool stoc(char str[],int m,int len) // show -> count
{
    for(int i=0;i<len;i++)
    {
        if (str[i] >= 'a' && str[i] <= 'z') str[i] -= 'a' - 10;
        if (str[i] >= 'A' && str[i] <= 'Z') str[i] -= 'A' - 10;
        if (str[i] >= '0' && str[i] <= '9') str[i] -= '0';
        if(str[i] >= m) return false;
    }
    return true;
}
 
char * ctos(char str[],int len) // count -> show
{
    static char buffer[DATALENGTH];
    int j = 0 ;
    char ch[]="0123456789ABCDEFGHIJKLMNOPQRST";
    for(int i = len -1 ; i >= 0; i--) buffer[j++] = ch[(int)str[i]];
    return buffer;
}
 
/**
 * usage :
 *  ./a.out
 *  ./a.out nn
 *  ./a.out mm nn
 */
int main(int argc, char *argv[])
{
    int m,n;
    char mm[DATALENGTH];
    bool bb[DATALENGTH];
    char nn[DATALENGTH];
    char *np;
    int bblen;
    int mmlen;
    int nnlen;
    switch(argc)
    {
        case 1:
            m = 10;
            n = 2;
            break;
        case 2:
            m = 10;
            n = 0;
            for(unsigned int i=0;i<strlen(argv[1]);i++) n = n * 10 + argv[1][i]-'0';
            break;
        case 3:
            m = 0;
            n = 0;
            for(unsigned int i=0;i<strlen(argv[1]);i++) m = m * 10 + argv[1][i]-'0';
            for(unsigned int i=0;i<strlen(argv[2]);i++) n = n * 10 + argv[2][i]-'0';
            break;
        default :
            return 0;
    }
    if(m>16 || n > 16)
    {
        printf("ERROR: both m & n should less than 16\n");
        return -1;
    }
    printf("SET : %d -> %d\n",m,n);
    printf("input a number : ");
    scanf("%s",mm);
    mmlen = strlen(mm);
    printf("your input: %s (%d)\n",mm,mmlen);
    if(!stoc(mm,m,mmlen))
    {
        printf("Error input : Input Number Is Out Of Range!\n");
        return -1;
    }
    //printf("m -> b ...");
    mtob(mm,m,mmlen,bb,bblen);
    //printf("[ok]\n");
    //printf("b -> n ...");
    for(int i=0;i<DATALENGTH;i++) nn[i] = 0;
    bton(bb,n,bblen,nn,nnlen);
    np = ctos(nn,nnlen);
    //printf("[ok]\n");
    printf("result is : %s\n",np);
    return 0;
}
