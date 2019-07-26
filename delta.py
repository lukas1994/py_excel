from SALib.sample import latin
from SALib.analyze import delta
from SALib.test_functions import Ishigami
import numpy as np

# Define the model inputs
problem = {
    'num_vars': 3,
    'names': ['x1', 'x2', 'x3'],
    'bounds': [[0, 5], # (mean, std dev)
               [0, 5],
               [0, 5]],
    'dists': ['norm', 'norm', 'norm'],
}

# Generate samples
X = latin.sample(problem, 1000)
print(X)

# Run model (example)
Y = Ishigami.evaluate(X)

# Perform analysis
Si = delta.analyze(problem, X, Y, print_to_console=True)

# Print the first-order sensitivity indices
print(Si['S1'])
