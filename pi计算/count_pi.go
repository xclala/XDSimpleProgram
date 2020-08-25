//我想搞python和go交互，https://www.cnblogs.com/huangguifeng/p/8931837.html，https://www.cnblogs.com/dhcn/p/12044521.html,失败原因如下，不能return有啥用，就相当于没有输出。唉，人生苦短，我学python不假呀！水平有限，只能用go编小程序,python编大程序，也好，分工协作。
/*# command-line-arguments
.\count_pi.go:10:26: invalid indirect of -level (type int)
.\count_pi.go:17:4: too many arguments to return
        have (float64, float64)
        want (float64)
.\count_pi.go:20:1: missing return at end of function*/
package main

import "C"
import "math"

func count_pi(level int) float64 {
	for true {
		var a, b, pi, i, tmp float64
		a, b, pi, tmp, i = 1, 1, 0, 1, 0
		if math.Abs(tmp) >= 10**-level {
			pi += tmp
			b += 2
			a = -a
			tmp = a / b
			i += 2
		} else {
			return i, pi
		}
	}
}
func main() {

}
