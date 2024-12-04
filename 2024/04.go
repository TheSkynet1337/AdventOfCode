package main

import (
	"fmt"
	"os"
	// "os"
	"strings"
)

func checkInDirection(input []string, direction []int, xy []int) bool {
	x := xy[0]
	y := xy[1]
	if x < 3 && direction[0] < 0 {
		return false
	}
	if y < 3 && direction[1] < 0 {
		return false
	}
	if len(input)-x-1 < 3 && direction[0] > 0 {
		return false
	}
	if len(input[0])-y-1 < 3 && direction[1] > 0 {
		return false
	}
	for i, _ := range "XMAS" {
		if input[x+i*direction[0]][y+i*direction[1]] != "XMAS"[i] {
			return false
		}
	}
	return true
}

func checkWordInDirection(input []string, xy []int, word string, direction []int) bool {
	x := xy[0]
	y := xy[1]
	for i, _ := range word {
		if input[x+i*direction[0]][y+i*direction[1]] != word[i] {
			return false
		}
	}
	return true
}
func checkForX(input []string, xy []int) bool {
	x := xy[0]
	y := xy[1]
	if x < 1 {
		return false
	}
	if y < 1 {
		return false
	}
	if len(input)-x-1 < 1 {
		return false
	}
	if len(input[0])-y-1 < 1 {
		return false
	}
	xFound := 0
	directions := [][]int{{-1, -1}, {-1, 1}, {1, -1}, {1, 1}}
	for _, direction := range directions {
		start := []int{x + direction[0], y + direction[1]}
		if checkWordInDirection(input, start, "MAS", []int{direction[0] * -1, direction[1] * -1}) {
			xFound += 1
		}
	}
	if xFound < 2 {
		return false
	}
	return true
}
func main() {
	// 	rawin :=
	// 		`MMMSXXMASM
	// MSAMXMSMSA
	// AMXSXMAAMM
	// MSAMASMSMX
	// XMASAMXAMM
	// XXAMMXXAMA
	// SMSMSASXSS
	// SAXAMASAAA
	// MAMMMXMMMM
	// MXMXAXMASX`
	rawIn, _ := os.ReadFile("04.txt")
	in := string(rawIn)
	inA := strings.Split(in, "\n")
	inTrim := inA[:140]
	directions := [][]int{{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}}
	xmases := 0
	crosses := 0
	for x, _ := range inTrim {
		for y, _ := range inTrim[x] {
			if inTrim[x][y] != 'X' {
				continue
			}
			for _, direction := range directions {
				if checkInDirection(inTrim, direction, []int{x, y}) {
					xmases += 1
				}
			}
		}
	}
	for x, _ := range inTrim {
		for y, _ := range inTrim[x] {
			if inTrim[x][y] != 'A' {
				continue
			}
			if checkForX(inTrim, []int{x, y}) {
				crosses += 1
			}
		}
	}
	fmt.Println("Part 1:", xmases)
	fmt.Println("Part 2:", crosses)
}
