#include <stdio.h>
#include <string.h>
void main(void)
{
	char str[80];
	int i,j,iStrlenstr,iFlag;
	printf("�������ַ�����\n");
	gets(str);
	iStrlenstr=strlen(str);
	for (i=0,j=iStrlenstr-1;i<=j;i++,j--)
	{
		if (str[i]==str[j])
		{iFlag=1;}
		else
		{iFlag=0;break;}
	}
	if (iFlag==1)
	{printf("������ǻ��ģ�\n");system("pause");}
	else
	{printf("����Ĳ��ǻ��ģ�\n");system("pause");}
}
