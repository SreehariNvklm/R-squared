import glob
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import textwrap

def chunk_text(text, chunk_size=50):
    """
    Splits text into smaller chunks of approximately `chunk_size` words.
    """
    words = text.split()
    chunks = [" ".join(words[i : i + chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks

text_files = glob.glob("R-squared/output_text/*/*.txt")
chunks = []
for text in text_files:
    chunk = chunk_text(text,chunk_size=100)
    chunks.append(chunk)

model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = np.array(model.encode([chunks]), dtype=np.float32)

ids = np.arange(len(embeddings))

d = embeddings.shape[1]  # Vector dimensionality
index = faiss.IndexFlatL2(d)

# Wrap in IndexIDMap for unique IDs
index_with_ids = faiss.IndexIDMap(index)
index_with_ids.add_with_ids(embeddings, ids)

faiss.write_index(index_with_ids, "R-squared/faiss_index_chunk.bin")

query_text = """ANNEXURE A ‘A TRUE COPY OF THE FIR WITH Fl STATEMENT
IN CRIME NO. 75/2018 OF KULAMAVU POLICE.
STATION.
"""
query_vector = np.array(model.encode([query_text]), dtype=np.float32)

k = 2
distances, retrieved_ids = index_with_ids.search(query_vector, k)

# Show results
print("\nTop Matching Chunks:")
for i, idx in enumerate(retrieved_ids[0]):
    print(f"Match {i+1}: {chunks[idx]} (Distance: {distances[0][i]:.4f})")
