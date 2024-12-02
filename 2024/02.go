package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func absDiffInt(x, y int) int {
	if x < y {
		return y - x
	}
	return x - y
}
func tryLine(line []string) bool {
	increasing := true
	last := 0
	safeLine := true
	for i, num := range line {
		inum, _ := strconv.Atoi(num)
		switch i {
		case 0:
			last = inum
		case 1:
			increasing = (last - inum) > 0
			fallthrough
		default:
			if absDiffInt(inum, last) > 3 || ((last-inum) > 0) != increasing || inum-last == 0 {
				safeLine = false
				break
			}
		}
		last = inum
	}
	return safeLine
}
func main() {

	in := `7 6 4 2 1
	1 2 7 8 9
	9 7 6 2 1
	1 3 2 4 5
	8 6 4 4 1
	1 3 6 7 9`
	rawIn, _ := os.ReadFile("02.txt")
	in = string(rawIn)
	lines := strings.Split(in, "\n")
	safe := 0
	pt1safe := 0
	for _, line := range lines {
		strnums := strings.Fields(line)
		if len(strnums) == 0 {
			break
		}
		if tryLine(strnums) {
			safe += 1
			pt1safe += 1
		} else {
			for i, _ := range strnums {
				tmp := make([]string, len(strnums))
				copy(tmp, strnums)
				if tryLine(append(tmp[:i], tmp[i+1:]...)) {
					safe += 1
					break
				}
			}
		}
	}
	fmt.Println("Part 1:", pt1safe)
	fmt.Println("Part 2:", safe)
}
