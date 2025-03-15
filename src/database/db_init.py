import faiss
from sentence_transformers import SentenceTransformer
import glob
import numpy as np

embedding_dim = 768
index = faiss.IndexFlatL2(embedding_dim)

model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")

all_embeddings = []

for doc in glob.glob("output_text/*/*.txt"):
    with open(doc,"r",encoding='utf-8') as file:
        f = file.read()
        embeddings = model.encode(f)
        all_embeddings.append(embeddings)

index.add(np.array(all_embeddings, dtype=np.float32))
faiss.write_index(index, "faiss_index.bin")