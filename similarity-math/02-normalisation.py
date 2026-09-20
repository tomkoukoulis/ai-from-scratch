import numpy as np

def normalise(v):
    magnitude = np.linalg.norm(v)
    return v / magnitude

pasta = np.array([3, 0, 2], dtype=float)
pasta_hat = normalise(pasta)

print("Original:  ", pasta)
print("Normalised:", pasta_hat)
print("Magnitude after:", np.linalg.norm(pasta_hat))