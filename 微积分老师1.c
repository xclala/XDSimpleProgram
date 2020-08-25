#include <windows.h>
int main(int argc,char *argv[]){
	ShowWindow(FindWindow("ConsoleWindowClass",argv[0]),0);
	ShellExecute(NULL,"open","https://weibo.com/sssmath?topnav=1&wvr=6&topsug=1&is_all=1",NULL,NULL,SW_SHOWNORMAL);
	return 0;
}
