#include <stdio.h>

int n=-1, a1 = 1, a2 = 1, loop,tmp;
int main(){

do
{
printf("������һ����");
scanf("%d", &n);
}while(n < 1 || n > 1000000); 

for(loop=3;loop<=n;loop++)
{
  //printf("%d\n",n); 
  tmp = a2%10007;
  a2 = (a1 + a2)%10007;  
  a1 = tmp;
  
}
printf("%d\n", a2);
printf("%d", a2%10007); 
return 0;
}

//ʲô��ȡģ����
