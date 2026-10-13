# pip install torch requests
import collections
import requests
import torch

torch.manual_seed(42)
dev = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# text8: the first 100 million characters of Wikipedia, lower case, no punctuation
r = requests.get('https://huggingface.co/datasets/ardMLX/text8/resolve/main/text8')
words: list[str] = r.text.split()
print(words[:7])  # ['anarchism', 'originated', 'as', 'a', 'term', 'of', 'abuse']

# the vocabulary is the 10,000 most common words
vocab = [w for w, _ in collections.Counter(words).most_common(10_000)]
words_to_ids = {w: i for i, w in enumerate(vocab)}
ids_to_words = {i: w for i, w in enumerate(vocab)}
ids = torch.tensor([words_to_ids[w] for w in words if w in words_to_ids])
print(len(vocab), len(ids))

# a batch of examples: two words either side as the context, the middle word as the target
def get_batch(size: int = 256):
    idx = torch.randint(2, len(ids) - 2, (size,))
    ipt = ids[idx[:, None] + torch.tensor([-2, -1, 1, 2])]
    trg = ids[idx]
    return ipt.to(dev), trg.to(dev)

# the embedding matrix, the average, and the output matrix
class CBOW(torch.nn.Module):
    def __init__(self, voc, emb):
        super().__init__()
        self.emb = torch.nn.Embedding(num_embeddings=voc, embedding_dim=emb)
        self.ffw = torch.nn.Linear(in_features=emb, out_features=voc, bias=False)

    def forward(self, inpt):
        emb = self.emb(inpt).mean(dim=1)
        out = self.ffw(emb)
        return out

# nearest neighbours by cosine similarity
def topk(model, word: str, k: int = 5):
    with torch.no_grad():
        emb = torch.nn.functional.normalize(model.emb.weight, dim=1)
        sim = emb @ emb[words_to_ids[word]]
        top = torch.topk(sim, k + 1).indices[1:]
        print(word, '->', [ids_to_words[int(i.item())] for i in top])

model = CBOW(len(vocab), 128).to(dev)
optimiser = torch.optim.Adam(model.parameters(), lr=0.003)
criterion = torch.nn.CrossEntropyLoss()
ipt, trg = get_batch()
print(criterion(model(ipt), trg).item())  # about 9.21, which is log(10,000)

# training: a guess, the loss, and a nudge to both matrices
for i in range(30_000):
    ipt, trg = get_batch()
    out = model(ipt)
    loss = criterion(out, trg)
    optimiser.zero_grad()
    loss.backward()
    optimiser.step()
    if i % 1_000 == 0: print(i, loss.item())
    if i % 10_000 == 0: topk(model, 'computer')

for word in ['king', 'france', 'three', 'computer', 'war']: topk(model, word)