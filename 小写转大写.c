#include <stdio.h>
main(){
	char a,b;
	printf("请输入一个小写字母,只能输入一个字母:\n");
	a=getchar();
	b=a-32;
	printf("转换后的字母为：%c\n",b,b);
	system("pause");
}
