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
		printf("������֣�");
		scanf("%d",&guess);
		if (guess>ret){
			printf("�´��ˡ�");
		}
		else if (guess<ret){
			printf("��С�ˡ�");
		}
		else{
			printf("��ϲ�㣬�¶��ˣ�\n");
			break;
		}
	}
}
main(){
	int input=0;
	srand((unsigned int)time(NULL));
	printf("��ӭʹ�ñ�����\n"); 
	do{
		menu();
		printf("��ѡ��");
		scanf("%d",&input);
		switch(input){
			case 1:
				game();
				break;
			case 0:
				break;
			default:
				printf("ѡ�����������ѡ��\n");
		}
	}while (input);
}	
