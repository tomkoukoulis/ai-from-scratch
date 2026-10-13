import numpy as np

# window = 2
# pairs = []
# for sentence in corpus:
#     words = sentence.split()
#     for i in range(len(words)):
#         context = words[max(0, i - window):i] + words[i + 1:i + 1 + window]
#         pairs.append((context, words[i]))

# for pair in pairs[:5]:
#     print(pair)
# print(len(pairs))

sentence = "the dog chased the ball"
window = 1

# >>> your code
pairs = []
words = sentence.split()
for i in range(len(words)):
    context = words[max(0, i - window):i] + words[i + 1:i + 1 + window]
    pairs.append((context, words[i]))

for pair in pairs[:5]:
    print(pair)
# <<< end of your code

print(len(pairs))
print(pairs[:2])