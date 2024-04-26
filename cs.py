from constraint import Problem, AllDifferentConstraint

# Create a new constraint problem
problem = Problem()

# Define the unique letters in the puzzle
letters = ["T", "W", "O", "F", "U", "R"]

# Add variables for each unique letter with domain 0-9
problem.addVariables(letters, range(10))

# Add a constraint to ensure all variables have different values
problem.addConstraint(AllDifferentConstraint(), letters)

# Add the arithmetic constraint for the cryptarithmetic puzzle
def check_solution(T, W, O, F, U, R):
    # Convert letters to numbers
    TWO = T * 100 + W * 10 + O
    FOUR = F * 1000 + O * 100 + U * 10 + R
    return (TWO + TWO) == FOUR

problem.addConstraint(check_solution, letters)

# Get solutions
solutions = problem.getSolutions()

# Print all solutions
if solutions:
    print("Solutions found:")
    for sol in solutions:
        print("TWO =", sol["T"] * 100 + sol["W"] * 10 + sol["O"])
        print("FOUR =", sol["F"] * 1000 + sol["O"] * 100 + sol["U"] * 10 + sol["R"])
        print()
else:
    print("No solution found.")
