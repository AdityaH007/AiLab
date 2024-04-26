from constraint import Problem, AllDifferentConstraint

# Create a new problem instance
problem = Problem()

# Define the domain for each variable (the chessboard positions, 1 through 8)
queens = list(range(1, 9))  # Positions 1 through 8
problem.addVariables(queens, queens)  # Each queen has 8 possible positions

# Add constraints to ensure no queens are in the same row
problem.addConstraint(AllDifferentConstraint(), queens)

# Add constraints to ensure no queens are in the same diagonal
# The diagonal check is based on the absolute difference between column and row
problem.addConstraint(
    lambda col1, col2, row1, row2: abs(row1 - row2) != abs(col1 - col2),
    [(i, j) for i in queens for j in queens if i != j]
)

# Find all possible solutions to the problem
solutions = problem.getSolutions()

# Display a sample solution
if solutions:
    print("Found a solution:")
    solution = solutions[0]  # Get the first solution
    for row in sorted(solution.keys()):
        print(f"Queen in row {row} at column {solution[row]}")
else:
    print("No solution found")
