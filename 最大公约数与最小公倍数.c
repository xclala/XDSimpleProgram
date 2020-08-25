#include <stdio.h>
main(){
	int m,n,temp,i,num1;
	printf("欢迎使用本程序！\n"); 
	printf("请输入m和n，只能用空格分隔：");
	scanf("%d%d",&m,&n);
	if (m<n){
		temp=m;
		m=n;
		n=temp;
	}
	printf("您要求最大公约数还是最小公倍数？1：最大公约数  2：最小公倍数");
	scanf("%d",&num1);
	if (num1==1){
		for (i=n;i>0;i--)
			if (m%i==0 && n%i==0){
				printf("%d和%d的最大公约数是：%d\n", m, n, i);
				printf("欢迎再次使用本程序。"); 
				system("pause");
				break;}
	}
	else{
		for (i=n;i>0;i++)
			if (m%i==0 && n%i==0){
				printf("%d和%d的最小公倍数是：%d\n", m, n, i);
				printf("欢迎再次使用本程序。");
				system("pause");
				break;}
	}
}
