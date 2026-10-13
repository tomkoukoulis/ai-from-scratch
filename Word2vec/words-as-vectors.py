import numpy as np

vocab = ["the", "cat", "dog", "sat", "slept", "on", "mat", "sofa", "a", "chased", "ball", "ate"]
E = np.random.rand(12, 4) - 0.5

def cosine(a, b):
    return a @ b / (np.linalg.norm(a) * np.linalg.norm(b))

cat = E[vocab.index("cat")]
print(cat.round(2))
print(E.shape)
print(cosine(cat, E[vocab.index("dog")]).round(2))
print(cosine(cat, E[vocab.index("sofa")]).round(2))