from SALib.sample import latin
from SALib.analyze import delta, sobol
from SALib.test_functions import Ishigami
import numpy as np
import random

# Define the model inputs
problem = {
    'num_vars': 4,
    'names': ['apprecition', 'cost', 'returns', 'interest'],
}
with open("data.csv") as f:
	data = f.read().splitlines()
data = list(map(lambda x: list(map(float, x.split(","))), data))
print(data[:10])
X = np.array(data)
Y = X[:,4]
X = X[:, 0:4]
print(X)

# Perform analysis
Si = delta.analyze(problem, X, Y, print_to_console=True)

# Print the first-order sensitivity indices
print(Si['S1'])

s = sobol.analyze(problem, X, Y, print_to_console=True)
print(s)
