import numpy as np

def normalise(v):
    magnitude = np.linalg.norm(v)
    return v / magnitude

pasta = np.array([3, 0, 2], dtype=float)
pasta_hat = normalise(pasta)

print("Original:  ", pasta)
print("Normalised:", pasta_hat)
print("Magnitude after:", np.linalg.norm(pasta_hat))

## Manual normalisation
v = np.array([3, 0, 4], dtype=float)

## Step 1: square each component
squares = v ** 2
print("Squares:", squares)  # [9, 0, 16]

## Step 2: sum them
total = np.sum(squares)
print("Sum:", total)  # 25

## Step 3: square root (the magnitude)
mag = np.sqrt(total)
print("Magnitude:", mag)  # 5.0  -- a 3-4-5 triangle

## Step 4: divide each component by the magnitude
v_hat = v / mag
print("Normalised:", v_hat)  # [0.6, 0.0, 0.8]

## Step 5: verify
print("Verify magnitude:", np.linalg.norm(v_hat))  # 1.0

## Normalisation removes magnitude, but preserves direction
pasta   = np.array([3, 0, 2], dtype=float)
spicy   = np.array([6, 0, 4], dtype=float)
cake    = np.array([0, 8, 0], dtype=float)

pasta_hat = normalise(pasta)
spicy_hat = normalise(spicy)
cake_hat  = normalise(cake)

print("Pasta normalised:  ", np.round(pasta_hat, 4))
print("Spicy normalised:  ", np.round(spicy_hat, 4))
print("Cake normalised:   ", np.round(cake_hat, 4))

print()
print("Pasta == Spicy after normalisation:", np.allclose(pasta_hat, spicy_hat))

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def dot_product(a, b):
    return np.dot(a, b)

pasta   = np.array([3, 0, 2], dtype=float)
cake    = np.array([0, 8, 0], dtype=float)
spicy   = np.array([6, 0, 4], dtype=float)

pasta_hat = normalise(pasta)
cake_hat  = normalise(cake)
spicy_hat = normalise(spicy)

## On normalised vectors, these should be equal
print("Cosine similarity (pasta vs cake): ", cosine_similarity(pasta_hat, cake_hat))
print("Dot product (pasta vs cake):       ", dot_product(pasta_hat, cake_hat))

print()
print("Cosine similarity (pasta vs spicy):", cosine_similarity(pasta_hat, spicy_hat))
print("Dot product (pasta vs spicy):      ", dot_product(pasta_hat, spicy_hat))