#include <stdio.h>
main(){
	#if _WIN32
	system("color c && echo Hello,world!");
	getch();
	#elif __linux__
	printf("\033[22;31mHello,world!\n\033[22;30m");
	getch();
	#else
	printf("Hello,world!");
	getch();
	#endif
}
