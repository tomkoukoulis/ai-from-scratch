import numpy as np

## A recipe represented as a vector: [garlic, sugar, chilli] in teaspoons
pasta_arrabbiata = np.array([3, 0, 2])
spicy_noodles    = np.array([6, 0, 4])
chocolate_cake   = np.array([0, 8, 0])

print("Pasta Arrabbiata:", pasta_arrabbiata)
print("Spicy Noodles:   ", spicy_noodles)
print("Chocolate Cake:  ", chocolate_cake)
print()
print("Shape:", pasta_arrabbiata.shape)
print("Dimensions:", pasta_arrabbiata.ndim)
print("Length (number of components):", len(pasta_arrabbiata))

## You can add vectors component-wise
combined = pasta_arrabbiata + chocolate_cake
print("Pasta + Cake:", combined)

## You can scale a vector
double_pasta = pasta_arrabbiata * 2
print("Double pasta:", double_pasta)

## You can subtract
difference = spicy_noodles - pasta_arrabbiata
print("Spicy Noodles minus Pasta:", difference)

def magnitude(v):
    return np.sqrt(np.sum(v ** 2))

## Or equivalently, numpy has this built in:
## np.linalg.norm(v)

print("Magnitude of Pasta Arrabbiata:", magnitude(pasta_arrabbiata))
print("Magnitude of Spicy Noodles:   ", magnitude(spicy_noodles))
print("Magnitude of Chocolate Cake:  ", magnitude(chocolate_cake))

## Verify with numpy
print()
print("numpy norm (Pasta):", np.linalg.norm(pasta_arrabbiata))

## A 10-dimensional vector
v = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=float)

print("Vector:", v)
print("Magnitude:", np.linalg.norm(v))
print("Shape:", v.shape)

## Arithmetic works the same regardless of dimension
w = np.ones(10)
print("v + w:", v + w)
print("v * 3:", v * 3)

vector_a = np.array([1, 2, 3])
vector_b = np.array([2, 4, 6])

## Vectors with same direction but different magnitutes.
## Their difference is a vector in the same direction as well.
print("Vector A:", vector_a)
print("Vector A magnitude:", magnitude(vector_a))
print("Vector B:", vector_b)
print("Vector B magnitude:", magnitude(vector_b))

## Magnitute of a vector is proportional to the magnitude of any scalar multiple of that vector.
print("Magnitude of double components of A:", magnitude(vector_a * 2))

zero_vector = np.array([0, 0, 0])
print("Zero vector:", zero_vector)
print("Zero vector magnitude:", magnitude(zero_vector))

import time

big = np.random.randn(1536)
start = time.perf_counter()
for i in range(100_000):
    np.linalg.norm(big)
elapsed = time.perf_counter() - start
print(f"100k norm calculations on 1536-dim vector: {elapsed:.3f}s")