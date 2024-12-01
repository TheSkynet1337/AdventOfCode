package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func absDiffInt(x, y int) int {
	if x < y {
		return y - x
	}
	return x - y
}

func main() {
	in := `3   4
	4   3
	2   5
	1   3
	3   9
	3   3`
	rawIn, _ := os.ReadFile("01.txt")
	in = string(rawIn)
	lines := strings.Split(in, "\n")
	var leftNums []int
	var rightNums []int
	for _, line := range lines {
		nums := strings.Fields(line)
		if len(nums) == 0 {
			break
		}
		leftNum, _ := strconv.Atoi(nums[0])
		rightNum, _ := strconv.Atoi(nums[1])
		leftNums = append(leftNums, leftNum)
		rightNums = append(rightNums, rightNum)
	}
	sort.Ints(leftNums)
	sort.Ints(rightNums)
	sum := 0
	for i := 0; i < len(leftNums); i++ {
		sum += absDiffInt(leftNums[i], rightNums[i])
	}
	fmt.Println("Part 1:", sum)
	rightMap := make(map[int]int)
	for _, num := range rightNums {
		rightMap[num] += 1
	}
	similiarity := 0
	for _, num := range leftNums {
		similiarity += rightMap[num] * num
	}
	fmt.Println("Part 2:", similiarity)
}
