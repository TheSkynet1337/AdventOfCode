package main

import (
	"fmt"
	"os"
	// "os"
	"regexp"
	"strconv"
)

func part1() int {

	in := `xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))`
	rawIn, err := os.ReadFile("03.txt")
	if err != nil {
		fmt.Println(err.Error())
	}
	in = string(rawIn)
	reg, err := regexp.Compile(`mul\(\d{1,3},\d{1,3}\)`)
	if err != nil {
		fmt.Println(err.Error())
	}
	matches := reg.FindAllString(in, -1)
	numberReg, err := regexp.Compile(`\d{1,3}`)
	if err != nil {
		fmt.Println(err.Error())
	}
	sum := 0
	for _, mul := range matches {
		numsString := numberReg.FindAllString(mul, -1)
		leftNum, err := strconv.Atoi(numsString[0])
		if err != nil {
			fmt.Println(err.Error())
		}
		rightNum, err := strconv.Atoi(numsString[1])
		if err != nil {
			fmt.Println(err.Error())
		}
		sum += leftNum * rightNum
	}
	return sum
}
func part2() int {
	in := `xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))`
	rawIn, err := os.ReadFile("03.txt")
	if err != nil {
		fmt.Println(err.Error())
	}
	in = string(rawIn)
	dontToDoReg, err := regexp.Compile(`(?s)don't\(\).*?do\(\)`)
	if err != nil {
		fmt.Println(err.Error())
	}
	matchedIn := in
	i := 0
	for dontToDoReg.FindStringIndex(matchedIn) != nil {
		i++
		match := dontToDoReg.FindStringIndex(matchedIn)
		matchedIn = matchedIn[:match[0]] + matchedIn[match[1]:]
	}
	reg, err := regexp.Compile(`mul\(\d{1,3},\d{1,3}\)`)
	if err != nil {
		fmt.Println(err.Error())
	}
	numberReg, err := regexp.Compile(`\d{1,3}`)
	if err != nil {
		fmt.Println(err.Error())
	}
	dontReg, err := regexp.Compile(`don't\(\)`)
	if err != nil {
		fmt.Println(err.Error())
	}
	index := dontReg.FindStringIndex(matchedIn)
	matchedIn = matchedIn[:index[0]]
	matches := reg.FindAllString(matchedIn, -1)
	sum := 0
	for _, mul := range matches {
		numsString := numberReg.FindAllString(mul, -1)
		leftNum, err := strconv.Atoi(numsString[0])
		if err != nil {
			fmt.Println(err.Error())
		}
		rightNum, err := strconv.Atoi(numsString[1])
		if err != nil {
			fmt.Println(err.Error())
		}
		sum += leftNum * rightNum
	}
	return sum
}
func main() {
	fmt.Println("Part 1:", part1())
	fmt.Println("Part 2:", part2())
}
