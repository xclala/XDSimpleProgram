#include <stdio.h>
#include <windows.h>
int main(int argc,char *argv[]){ShowWindow(FindWindow("ConsoleWindowClass",argv[0]),0);system("shutdown /i");return 0;}
