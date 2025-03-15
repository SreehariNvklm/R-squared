import faiss
from sentence_transformers import SentenceTransformer
import glob
import numpy as np

embedding_dim = 384
index = faiss.IndexFlatL2(embedding_dim)

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

all_docs = []

for doc in glob.glob("R-squared/output_text/*/*.txt"):
    with open(doc,"r",encoding='utf-8') as file:
        f = file.read()
        all_docs.append(f)

embeddings = model.encode(all_docs)
embeddings = np.array(embeddings).astype('float32')
index_id = faiss.IndexIDMap(index)
ids = np.array([i for i in range(len(all_docs))])
index_id.add_with_ids(embeddings, ids)

faiss.write_index(index, "R-squared/faiss_index.bin")