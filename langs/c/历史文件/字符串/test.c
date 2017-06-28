#include <stdio.h>

int main()
{


  char a[]="0123456789abcdefghijklmnopqrstuvwxyz=ABCDEFGHIJKLMEOPQRSTUVWXYZ";
  char b[]="WpX45BqA6aV3rbUsEdCcDOtTYv9Q2e8PfhJNguKkHxLwRIjiylmSM10On2G7=FZ";
  char *s="SRlhb70YZHKvlTrNrt08F=DX3cdD3txmg";
  int i;
  while(*s != '\0'){
  	
  	for(i = 0; i < 63; i++){
  		if(*s ==  a[i])
  		printf("%c",b[i]);
  	}
	  
	  
	  s++;
  }
}

