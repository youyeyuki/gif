#include <stdio.h>
#include <stdlib.h>
void str1(int num, int i){
	int N;
	if('A' <= num && num <= 'Z' )
	     N =90;
    else if('a' <= num && num<= 'z')
         N = 122;
	 
	if (N-26 < num && num<= N -i ) //大写64<num<= 85 
	    num+=i;
	else if(N -i < num && num <= N) //86 < num <=99
	    num = num + i - 26;
	 printf("%c",num);
}

void count_str(char *str){
	int count = 0; 
	while(*str != '\0'){
		count++;
		str++;				
	}
	printf("%d", count);
}
int main(){
	char  *s = "Happy New Year 2016#", *p = s; 
	int i, guess = 1 ;//guess 初始为0 

	// guess++ <= 26  因为++ 的优先级 比 《= 大所以执行 先使用guess的值  进行比较运算  然后就再加上1  给新手看估计会被打死 
	while(guess <= 26){
		printf("%d ", guess);
	while( *s != '\0')
	{
		i = *s;
		str1(i,guess);
		s++;
	}
    
    	printf("\n\n");
    	
    	s = p;
    	guess++;
    }
    system("pause");
}
