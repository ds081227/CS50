import sys
import random
from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        _, _, w, h = draw.textbbox((0, 0), letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        for var in self.domains:
            for value in set(self.domains[var]):  # Create a copy for iteration
                if var.length != len(value):
                    self.domains[var].remove(value)  # Remove from the original set

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        revision_made = False
        overlap = self.crossword.overlaps[x, y]
        revised_domain = set()
        if overlap:
            for x_value in self.domains[x]:
                for y_value in self.domains[y]:
                    if x_value[overlap[0]] == y_value[overlap[1]]:
                        revised_domain.add(x_value)
        if len(revised_domain) != len(self.domains[x]):
            self.domains[x] = revised_domain
            return True
        return False

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        # Queue all arcs in csp
        if arcs is None:
            queue = [(var, arc) for var in self.domains for arc in self.crossword.neighbors(var)]
        else:
            queue = arcs
        while queue:
            # Pick one arc from the queue
            arc = queue.pop(0)
            if self.revise(arc[0], arc[1]):
                if len(self.domains[arc[0]]) == 0:
                    return False
                # Add new pairs of arc into queue (Z, X)
                queue += [(new_arc, arc[0]) for new_arc in self.crossword.neighbors(arc[0]) if
                          new_arc != arc[1] and (new_arc, arc[0]) not in queue]
        return True

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        if all(assignment[variable] is not None for variable in assignment) and len(assignment) == len(self.domains):
            return True
        return False

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        all values distinct, value correct length, no conflicts between neighboring variables
        """
        for variable in assignment:
            if variable.length != len(assignment[variable]):  # Value is correct length
                return False
            neighbors = self.crossword.neighbors(variable)
            for neighbor in neighbors:
                if neighbor in assignment:
                    overlap = self.crossword.overlaps[variable, neighbor]
                    if assignment[variable][overlap[0]] != assignment[neighbor][overlap[1]]:  # No conflicts with neighbor
                        return False
            for check_variable in assignment:  # Values are distinct
                if variable is not check_variable:
                    if assignment[variable] == assignment[check_variable]:
                        return False
        return True

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        var_domain = self.domains[var]
        # Dict to keep track of the number of values they ruled out
        value_ranking = {value: 0 for value in var_domain}
        neighbors = self.crossword.neighbors(var)
        for value in var_domain:
            for neighbor in neighbors:
                if neighbor not in assignment:
                    neighbor_domain = self.domains[neighbor]
                    overlap = self.crossword.overlaps[var, neighbor]
                    for neighbor_value in neighbor_domain:
                        if value[overlap[0]] != neighbor_value[overlap[1]]:
                            value_ranking[value] += 1
        ordered_domain = sorted(value_ranking, key=value_ranking.get)
        return ordered_domain

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        var_list = [
            var for var in self.domains if var not in assignment]  # Get all the unassigned variables
        minimum_number = float('inf')
        for var in var_list:
            if len(self.domains[var]) < minimum_number:
                minimum_number = len(self.domains[var])
        min_value_list = [var for var in var_list if len(self.domains[var]) == minimum_number]
        if len(min_value_list) > 1:
            highest_degree = float('-inf')
            for min_var in min_value_list:
                if len(self.crossword.neighbors(min_var)) > highest_degree:
                    highest_degree = len(self.crossword.neighbors(min_var))
            highest_degree_list = [high_deg_var for high_deg_var in min_value_list if len(
                self.crossword.neighbors(high_deg_var)) == highest_degree]
            if len(highest_degree_list) > 1:
                return random.choice(highest_degree_list)
            else:
                return highest_degree_list[0]
        else:
            return min_value_list[0]

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        if self.assignment_complete(assignment):
            return assignment
        assignment_copy = assignment.copy()
        var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var, assignment):
            assignment_copy[var] = value
            if self.consistent(assignment_copy):
                arcs = [(neighbor, var) for neighbor in self.crossword.neighbors(var)]
                if self.ac3(arcs):
                    result = self.backtrack(assignment_copy)
                    if result is not None:
                        return result
                else:
                    assignment_copy[var] = None
        return None


def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
