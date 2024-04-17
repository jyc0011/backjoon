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
	N, _ := strconv.Atoi(scanner.Text())
	maxPrize := 0
	for i := 0; i < N; i++ {
		scanner.Scan()
		input := scanner.Text()
		dice := strings.Fields(input) 
		a, _ := strconv.Atoi(dice[0])
		b, _ := strconv.Atoi(dice[1])
		c, _ := strconv.Atoi(dice[2])
		var prize int
		if a == b && b == c {
			prize = 10000 + a * 1000
		} else if a == b || a == c || b == c {
			var same int
			if a == b || a == c {
				same = a
			} else {
				same = b
			}
			prize = 1000 + same * 100
		} else {
			prize = max(a, b, c) * 100
		}
		if prize > maxPrize {
			maxPrize = prize
		}
	}
	fmt.Println(maxPrize)
}

func max(a, b, c int) int {
	if a > b {
		if a > c {
			return a
		}
		return c
	}
	if b > c {
		return b
	}
	return c
}