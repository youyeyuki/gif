#include <stdio.h>
#include <stdlib.h>
void str1(int num, int i){
	int N;
	if('A' <= num && num <= 'Z' )
	     N =90;
    else if('a' <= num && num<= 'z')
         N = 122;
	 
	if (N-26 < num && num<= N -i ) //��д64<num<= 85 
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
	int i, guess = 1 ;//guess ��ʼΪ0 

	// guess++ <= 26  ��Ϊ++ �����ȼ� �� ��= ������ִ�� ��ʹ��guess��ֵ  ���бȽ�����  Ȼ����ټ���1  �����ֿ����ƻᱻ���� 
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
