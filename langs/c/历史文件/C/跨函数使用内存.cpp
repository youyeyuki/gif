/*
ԭ��  ͨ��malloc����һ������ ����ͨ���޸ĸñ����ĵ�ַ���޸���ֵ 
*/

#include <stdio.h>
#include <malloc.h>
void f(int * *q)
{
	printf("����������q�ĵ�ַ��%d\n",&q);
	printf("qָ��ĵ�ַ%d\n",q);
	printf("��*qȡ��p�е�ַ��ֵ%d\n",*q);  //*q ��p��ֵ  p=5; 
	*q = (int *)malloc(sizeof(int)); //���ظ�q 
    printf("qָ��Ķ�̬�ڴ��ַ%d\n",*q);
	//q = 5 ; q��p�ĵ�ַ ����&p 
	//*q = 5 ; *q = *&p ; ���Ǵ���p ָ��һ����ַ  �õ�ַ�Ѿ���malloc ���������Ķ�̬�ڴ������ 
	**q = 5;
	//**q ���� **q  **&p *p ȡ��pָ���ַ��ֵ  ��˵���ǿ���ͨ������޸�ֵ �ﵽ��̬���� 

}


int main()
{
	
	int * p;

	printf("p�ĵ�ַ��%d\n",&p);
	f(&p);//����p�ĵ�ַ 
}
