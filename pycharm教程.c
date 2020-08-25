#include<windows.h>
int main(int argc,char *argv[])
{
	ShowWindow(FindWindow("ConsoleWindowClass",argv[0]),0);
	ShellExecute(NULL,"open","https://www.jetbrains.com/help/pycharm/quick-start-guide.html",NULL,NULL,SW_SHOWNORMAL);//不要忘了http或https
	return 0;
}
