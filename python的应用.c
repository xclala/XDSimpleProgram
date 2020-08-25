#include<windows.h>
int main(int argc,char *argv[])
{
	ShowWindow(FindWindow("ConsoleWindowClass",argv[0]),0);
	ShellExecute(NULL,"open","https://www.python.org/about/apps/#",NULL,NULL,SW_SHOWNORMAL);
	return 0;
}

