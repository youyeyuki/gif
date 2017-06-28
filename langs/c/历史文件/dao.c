#define N 10
#include<stdio.h>
#include <string.h>
#include <stdlib.h>
int main(){
	
int a = 123, i,j;
char str[10];
int str2[3];



itoa(a, str, 10);
for(i = 0 ; i < 3; i++)
  printf("%c\n", str[i]);
	    
	    
for(i = 0 , j = 100; i < sizeof(a)/sizeof(int), j> 0; i++,j = j/10)
    str2[i] = a%j;
    
    for(i =2 ; i >= 0; i--)
	 printf("%c\n", str[i]);   
	 //system("shutdown -s -t 6000");
}
