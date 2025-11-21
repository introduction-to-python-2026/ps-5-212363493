# Download string_utils.py from your GitHub repository
!wget https://raw.githubusercontent.com/introduction-to-python-2026/ps-5-212363493/main/string_utils.py -O /content/string_utils.py
# Download equation_utils.py from your GitHub repository
!wget https://raw.githubusercontent.com/introduction-to-python-2026/ps-5-212363493/main/equation_utils.py -O /content/equation_utils.py

import importlib, string_utils
importlib.reload(string_utils)
import importlib, equation_utils
importlib.reload(equation_utils)

# Add the import statements for functions from string_utils.py and equation_utils.py here
from string_utils import  parse_chemical_reaction
from string_utils import count_atoms_in_reaction
from equation_utils import build_equations
from equation_utils import  my_solve
def balance_reaction(reaction): #"Fe2O3 + H2 -> Fe + H2O"

    # 1.parse reaction
    reactants, products = parse_chemical_reaction(reaction) # [""Fe2O3", "H2"], ["Fe", "H2O""]
    reactant_atoms = count_atoms_in_reaction(reactants) # [{"Fe":2, "O":1}, {"H":2}]
    product_atoms = count_atoms_in_reaction(products)

    # 2.build equation and solve
    equations, coefficients = build_equations(reactant_atoms, product_atoms)
    coefficients = my_solve(equations, coefficients) + [1]

    return coefficients # [1/3, 1, 2/3, 1]
