# Forest Area Calculator

This is a simple Python script that calculates the total area and the maximum single cell area of a forest in a grid.

## Usage

To run the script, you need to have Python 3 installed on your system. You can then run the script as follows:

python3 forest_area.py <file>

Where `<file>` is the path to the input file containing the test cases.

The input file must have the following format:

<number of test cases>

<test case 1>

<test case 2>

...

```

Each test case must have the following format:
<number of rows> <number of columns>
<row 1>
<row 2>
...

The rows must be strings of T and . characters, where T represents a tree and . represents an empty cell.

For each test case, the script will output the total area and the maximum single cell area, in the following format:

Case #<test case number>: <total area> <maximum single cell area>

#Example

Suppose we have the following input file:

2
3 3
T..
...
T..
5 5
T...T
.....
..T..
.....
T...T

We can then run the script as follows:

python3 forest_area.py input.txt

The script will then output the following:

Case #1: 4 2
Case #2: 14 6

