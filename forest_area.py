import sys

def main():
    # Check if the user provided a file to read
    if len(sys.argv) < 2:
        print("Usage: python3 " + sys.argv[0] + " <file>")
        sys.exit(1)

    # Read the input file and process it
    with open(sys.argv[1], "r") as input_file:
        # Read the number of test cases
        t = int(input_file.readline())

        # Iterate over the test cases
        for i in range(t):
            # Read the line with the test case data
            n, m = map(int, input_file.readline().strip().split())

            # Initialize the grid
            grid = []
            for j in range(n):
                grid.append(list(input_file.readline().strip()))

            # Process the test case
            result = process_test_case(n, m, grid)

            # Print the result
            print("Case #{}: {}".format(i + 1, result))

def process_test_case(n, m, grid):
    # Initialize the variables
    total_area = 0
    max_single_cell = 0

    # Iterate over the rows and columns of the grid
    for i in range(n):
        for j in range(m):
            # If the cell is a tree, compute the area of its forest
            if grid[i][j] == "T":
                area = compute_forest_area(i, j, n, m, grid)
                total_area += area

                # Update the maximum single cell area
                if area > max_single_cell:
                    max_single_cell = area

    return "{} {}".format(total_area, max_single_cell)

def compute_forest_area(i, j, n, m, grid):
    # Check if the cell is outside the grid or not a tree
    if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] != "T":
        return 0

    # Mark the cell as visited
    grid[i][j] = "V"

    # Compute the size of the forest by adding 1 (for the current cell)
    # and the size of the forests in the adjacent cells
    size = 1 + compute_forest_area(i - 1, j, n, m, grid)
    size += compute_forest_area(i + 1, j, n, m, grid)
    size += compute_forest_area(i, j - 1, n, m, grid)
    size += compute_forest_area(i, j + 1, n, m, grid)

    return size

if __name__ == "__main__":
    main()
