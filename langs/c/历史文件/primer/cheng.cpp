#define  pfi(X) printf("%d\n",X)
#define  pfc(X) printf("%c\n",X)
#define  pfs(X) printf("%s\n",X)
#define  pff(X) printf("%f\n",X)
#define  pfe(X) printf("%e"\n,X)
#define  true 1
#define  false 0
#include <stdio.h>
#include <math.h>
#include <stdlib.h> //malloc ������ϵͳ����������
#include <windows.h>
#include <string.h>
#define MAXN 255
char *big(char line1[], char line2[]){
	short s1[MAXN]={0}, s2[MAXN]={0}, s[MAXN]={0};
	int len1, len2, lenMax;
	len1 = strlen(line1);
	len2 = strlen(line2);
	lenMax =  len1 + len2 ;
	int k,outlen,i,lenLimit,j;
	
	for(i = len1 -1; i >= 0; i-- ){
		s1[i] = line1[len1 - i -1] - '0';
	} 
	for(i = len2 -1; i >= 0; i-- ){
		s2[i] = line2[len2 - i -1] - '0';
	} 
	if(len1 > len2){
		lenLimit = len1;
	}else{
		lenLimit = len2;
	}
	for(i = 0 ; i < len1; i++ ){
		for(j = 0; j < len2; j++){
			s[i + j +1 ] = s[i + j +1 ] +s1[i] * s2[j];
			
			if((k = s[i + j +1] / 10) > 0){
				s[i + j +1] = s[i + j +1] % 10;
				s[i + j + 2] = s[i + j + 2]  + k;
				//printf("%d ��λ\n",i + j + 2);
				
			}
		}
	}
	for(i = lenMax; i >= 0; i--)
	    if(s[i] != 0) break;
	    outlen = i ; 



	for(i = outlen; i > 0; i--){
		printf("%d",s[i]);
	}	
    printf("\n");
	
	

	


}
main(){
		char line1[MAXN], line2[MAXN];
	printf("��������� �����ʽ 2333 2333 �����������ݲ��ÿո����\n"); 
	
	while(1){
		scanf("%s %s",line1,line2);
		printf("�����");
		big(line1,line2);
	}
}
