package main

import "fmt"

func main() {
	fmt.Print("你家狗狗几岁？")
	var dog_age int
	fmt.Scan(&dog_age)
	var a string
	if dog_age <= 0 {
		fmt.Print("你开玩笑吧。alt+f4退出。\a")
		fmt.Scan(&a)
	} else {
		var man_age int
		man_age = 22 + (dog_age-2)*5
		fmt.Printf("对应人类年龄%d岁。\n", man_age)
		fmt.Print("alt+f4退出。")
		fmt.Scan(&a)
	}
}
