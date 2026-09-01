# 3-SAT Problem using Backtracking and Pruning

# ---------------------------------------------------
# 3-SAT Formula
# ---------------------------------------------------
# Variables: A, B, C, D
#
# Each tuple represents one clause.
# Positive number  = variable
# Negative number  = NOT variable
#
# Example:
# (A OR B OR NOT C)
# is represented as (1, 2, -3)

clauses = [
    (1, 2, -3),
    (-1, 2, 4),
    (1, -2, 3),
    (-1, -3, -4)
]

num_variables = 4


# ---------------------------------------------------
# Check whether a clause is satisfied
# ---------------------------------------------------

def clause_status(clause, assignment):
    """
    Returns:
        True  -> clause is satisfied
        False -> clause is not satisfied
        None  -> clause is not yet decided
    """

    undecided = False

    for literal in clause:

        variable = abs(literal)

        # Variable not assigned yet
        if variable not in assignment:
            undecided = True
            continue

        value = assignment[variable]

        # Positive literal
        if literal > 0 and value:
            return True

        # Negative literal
        if literal < 0 and not value:
            return True

    # Some variables are still unassigned
    if undecided:
        return None

    return False


# ---------------------------------------------------
# Check partial assignment
# ---------------------------------------------------

def is_valid_partial_assignment(assignment):

    for clause in clauses:

        status = clause_status(clause, assignment)

        # If a clause is already false,
        # prune this branch
        if status is False:
            return False

    return True


# ---------------------------------------------------
# Backtracking Function
# ---------------------------------------------------

def solve(assignment, variable):

    # All variables assigned
    if variable > num_variables:

        # Check all clauses
        for clause in clauses:
            if clause_status(clause, assignment) is not True:
                return None

        return assignment.copy()

    # Try assigning False
    assignment[variable] = False

    if is_valid_partial_assignment(assignment):

        result = solve(assignment, variable + 1)

        if result is not None:
            return result

    # Try assigning True
    assignment[variable] = True

    if is_valid_partial_assignment(assignment):

        result = solve(assignment, variable + 1)

        if result is not None:
            return result

    # Remove assignment during backtracking
    del assignment[variable]

    return None


# ---------------------------------------------------
# Main Program
# ---------------------------------------------------

print("3-SAT PROBLEM")
print("--------------------------------")

solution = solve({}, 1)

if solution is not None:

    print("The formula is SATISFIABLE.")

    print("\nVariable Assignment:")

    for variable in range(1, num_variables + 1):
        print("Variable", variable, "=", solution[variable])

else:

    print("The formula is NOT SATISFIABLE.")
