package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	T, _ := strconv.Atoi(scanner.Text())

	for i := 0; i < T; i++ {
		scanner.Scan()
		inputs := strings.Fields(scanner.Text())
		a, _ := strconv.Atoi(inputs[0])
		b, _ := strconv.Atoi(inputs[1])

		ans := powMod(a, b, 10)
		if ans == 0 {
			ans = 10
		}
		fmt.Println(ans)
	}
}

func powMod(base, exp, mod int) int {
	result := 1
	for exp > 0 {
		if exp%2 == 1 {
			result = (result * base) % mod
		}
		base = (base * base) % mod
		exp /= 2
	}
	return result
}