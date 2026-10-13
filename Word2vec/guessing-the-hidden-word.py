import numpy as np

# ids of [the, cat, on, the]
context_ids = [0, 1, 5, 0]

rows = E[context_ids]
print(rows.round(2))

context = rows.mean(axis=0)
print(context.round(2))