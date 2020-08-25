#include <stdio.h>
main()
{
	char str[30];
	printf("Could I have your name,please?");
	scanf("%s",&str);
	printf("Hello,%s!",str);
	getch();
}
