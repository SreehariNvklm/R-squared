# import glob
# import faiss
# import numpy as np
# from sentence_transformers import SentenceTransformer
# import textwrap

# def chunk_text(text, chunk_size=50):
#     """
#     Splits text into smaller chunks of approximately `chunk_size` words.
#     """
#     words = text.split()
#     chunks = [" ".join(words[i : i + chunk_size]) for i in range(0, len(words), chunk_size)]
#     return chunks

# text_files = glob.glob("R-squared/output_text/*/*.txt")
# chunks = []
# for text in text_files:
#     chunk = chunk_text(text,chunk_size=100)
#     chunks.append(chunk)

# model = SentenceTransformer("all-MiniLM-L6-v2")
# embeddings = np.array(model.encode([chunks]), dtype=np.float32)

# d = embeddings.shape[1]  # Vector dimensionality
# index = faiss.IndexFlatL2(d)

# d = embeddings.shape[1]  # Vector dimensionality
# index = faiss.IndexFlatL2(d)

# # Wrap in IndexIDMap for unique IDs
# index_with_ids = faiss.IndexIDMap(index)
# index_with_ids.add(embeddings)

# print(f"Total chunks stored: {index_with_ids.ntotal}")

# query_text = "efficient similarity search"
# query_vector = np.array(model.encode([query_text]), dtype=np.float32)

# # Perform search (top 2 results)
# k = 2
# distances, retrieved_ids = index_with_ids.search(query_vector, k)

# # Show results
# print("\nTop Matching Chunks:")
# for i, idx in enumerate(retrieved_ids[0]):
#     print(f"Match {i+1}: {chunks[idx]} (Distance: {distances[0][i]:.4f})")
