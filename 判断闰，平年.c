#include <stdio.h>
main(){
	int year,a;
	printf("请输入年份：\n");
	scanf("%d",&year);
	if (year%400==0)
	{a=1;}
	else
	{
		if (year%4==0 && year%100!=0)
		{a=1;}
		else
		{a=0;}
	}
	if (a==1)
	{printf("%d，此年是闰年。\n",year);
	system("pause");}
	else
	{printf("%d，此年非闰年。\n",year);
	system("pause");}
}
