#include <stdio.h>
main(){
	int m,n,temp,i,num1;
	printf("��ӭʹ�ñ�����\n"); 
	printf("������m��n��ֻ���ÿո�ָ���");
	scanf("%d%d",&m,&n);
	if (m<n){
		temp=m;
		m=n;
		n=temp;
	}
	printf("��Ҫ�����Լ��������С��������1�����Լ��  2����С������");
	scanf("%d",&num1);
	if (num1==1){
		for (i=n;i>0;i--)
			if (m%i==0 && n%i==0){
				printf("%d��%d�����Լ���ǣ�%d\n", m, n, i);
				printf("��ӭ�ٴ�ʹ�ñ�����"); 
				system("pause");
				break;}
	}
	else{
		for (i=n;i>0;i++)
			if (m%i==0 && n%i==0){
				printf("%d��%d����С�������ǣ�%d\n", m, n, i);
				printf("��ӭ�ٴ�ʹ�ñ�����");
				system("pause");
				break;}
	}
}
