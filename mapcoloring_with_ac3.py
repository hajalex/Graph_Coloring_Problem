from collections import defaultdict

# Define variables (representing the states of Australia)
variables = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]

# Define color domains
domains = {
    "WA": ["Red", "Green", "Blue"],
    "NT": ["Red", "Green", "Blue"],
    "SA": ["Red", "Green", "Blue"],
    "Q": ["Red", "Green", "Blue"],
    "NSW": ["Red", "Green", "Blue"],
    "V": ["Red", "Green", "Blue"],
    "T": ["Red", "Green", "Blue"],
}

# Define constraints (neighboring states should have different colors)
constraints = [("WA", "NT"), ("WA", "SA"), ("NT", "SA"), ("NT", "Q"), ("SA", "Q"),
               ("Q", "NSW"), ("SA", "NSW"), ("SA", "V"), ("NSW", "V"), ("Q", "T"), ("V", "T")]

# Define the Constraint Satisfaction Problem (CSP)
class ConstraintSatisfactionProblem:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints
        self.neighbors = defaultdict(list)
        
        # Fill the neighbors dictionary
        for (X, Y) in constraints:
            self.neighbors[X].append(Y)
            self.neighbors[Y].append(X)

# Define a function to check the satisfaction of color constraints
def satisfies_color_constraint(color1, color2):
    return color1 != color2

# Main function for coloring using AC-3
def color_map_with_ac3(csp):
    for var in csp.variables:
        for color in csp.domains[var]:
            if all(satisfies_color_constraint(color, csp.domains[neighbor][0]) for neighbor in csp.neighbors[var]):
                csp.domains[var] = [color]
                break

# Create the CSP problem instance
csp = ConstraintSatisfactionProblem(variables, domains, constraints)

# Run AC-3 for coloring
color_map_with_ac3(csp)

# Print the coloring results
for var in csp.variables:
    print(f"{var}: {csp.domains[var][0]}")
