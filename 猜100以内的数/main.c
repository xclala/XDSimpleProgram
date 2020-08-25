#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
menu(){
	printf("1.play\n");
	printf("0.exit\n");}
game(){
	int ret=0;
	int guess=0;
	ret=rand()%100+1;
	while(1){
		printf("请猜数字：");
		scanf("%d",&guess);
		if (guess>ret){
			printf("猜大了。");
		}
		else if (guess<ret){
			printf("猜小了。");
		}
		else{
			printf("恭喜你，猜对了！\n");
			break;
		}
	}
}
main(){
	int input=0;
	srand((unsigned int)time(NULL));
	printf("欢迎使用本程序！\n"); 
	do{
		menu();
		printf("请选择：");
		scanf("%d",&input);
		switch(input){
			case 1:
				game();
				break;
			case 0:
				break;
			default:
				printf("选择错误，请重新选择！\n");
		}
	}while (input);
}	
