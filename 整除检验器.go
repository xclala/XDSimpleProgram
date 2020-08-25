package main
import "fmt"
func main(){
	for true{
		var num1,num2 int
		fmt.Print("您要检测哪个数字？")
		fmt.Scan(&num1)
		fmt.Printf("您要检测%d能否被哪个数整除？",num1)
		fmt.Scan(&num2)
		if num1%num2==0{
			fmt.Printf("%d能被%d整除。\n",num1,num2)
			fmt.Println("")
		}else{
			fmt.Printf("%d不能被%d整除。\n",num1,num2)
			fmt.Println("")
		}
	}
}