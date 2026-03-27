//
// This script aligns cells of a text table by a separator character.
// I am almost certain that this can be done by combining other
// unix tools, I just have not found it yet.
//

package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

var lines [][]string
var lengths []int

func main() {
	// Match arguments
	args := os.Args[1:]
	if len(args) != 1 {
		fmt.Fprintf(os.Stderr, "usage: [stream] | align [separator]\n")
	}

	separator := args[0]

	// Read every line from stdin
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())
		if len(line) == 0 {
			continue
		}

		parts := strings.Split(line, separator)
		for i, part := range parts {
			parts[i] = strings.TrimSpace(part)
		}

		lines = append(lines, parts)
	}

	// Figure out how many cols we have
	if len(lines) == 0 {
		return
	}
	firstLine := lines[0]
	colCount := len(firstLine)

	// Figure out longest length per col
	lengths = make([]int, colCount)
	for i, line := range lines {
		if len(line) != colCount {
			fmt.Fprintf(os.Stderr, "mismatched column count on line %d, expected %d got %d\n", i+1, colCount, len(line))
			os.Exit(1)
		}

		for j, part := range line {
			if lengths[j] < len(part) {
				lengths[j] = len(part)
			}
		}
	}

	// Print with padding
	for _, line := range lines {
		for i, part := range line {
			wrote, _ := fmt.Printf("%s", part)

			if i != len(line)-1 {
				left := lengths[i] - wrote
				fmt.Printf("%s %s ", strings.Repeat(" ", left), separator)
			}
		}
		fmt.Printf("\n")
	}
}
