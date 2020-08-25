package main
import "fmt"
func main(){
	for true{
		fmt.Print("单位是摄氏度的输入0,是华氏度的输入1,是开尔文的输入2：")
		var a float64
		fmt.Scan(&a)
		if a==0{
			fmt.Print("c=")
			var c,f,k float64
			fmt.Scan(&c)
			f=c*1.8+32
			fmt.Printf("f=%f\n",f)
			k=c+273.15
			fmt.Printf("K=%f\n",k)	
		}else{
			if a==1{
				fmt.Print("f=")
				var cc,ff,kk float64
				fmt.Scan(&ff)
				cc=(ff-32)/1.8
				kk=cc+273.15
				fmt.Printf("c=%f\n",cc)
				fmt.Printf("K=%f\n",kk)
			}else{
				fmt.Print("K=")
				var ccc,fff,kkk float64
				fmt.Scan(&kkk)
				ccc=kkk-273.15
				fff=ccc*1.8+32
				fmt.Printf("c=%f\n",ccc)
				fmt.Printf("f=%f\n",fff)
			}
		}
	}
}
