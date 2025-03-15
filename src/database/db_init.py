from pymilvus import model
from pymilvus import MilvusClient
import os

client = MilvusClient("milvus_demo.db")

if client.has_collection(collection_name="demo_collection"):
    client.drop_collection(collection_name="demo_collection")
client.create_collection(
    collection_name="demo_collection",
    dimension=768,  # The vectors we will use in this demo has 768 dimensions
)

embedding_fn = model.DefaultEmbeddingFunction()

# docs = [
#     "Artificial intelligence was founded as an academic discipline in 1956.",
#     "Alan Turing was the first person to conduct substantial research in AI.",
#     "Born in Maida Vale, London, Turing was raised in southern England.",
# ]
#
# vectors = embedding_fn.encode_documents(docs)
# print("Dim:", embedding_fn.dim, vectors[0].shape)  # Dim: 768 (768,)
#
# data = [
#     {"id": i, "vector": vectors[i], "text": docs[i], "subject": "history"}
#     for i in range(len(vectors))
# ]
#
# print("Data has", len(data), "entities, each with fields: ", data[0].keys(), "vector value is ", vectors[0])
# print("Vector dim:", len(data[0]["vector"]))


data_dir = "R-squared/R-squared/text_files"


# Process each file (assuming filenames are 1.txt, 2.txt, ..., 1000.txt)
for i in range(1, 1001):
    file_path = os.path.join(data_dir, f"{i}.txt")

    if os.path.exists(file_path):  # Ensure file exists
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read().strip()  # Read text and remove extra spaces

        # Generate embedding
        embedding = model.encode(text)
        # data =
        # Store in dictionary
    res = client.insert(collection_name="demo_collection", data=data)
# Save embeddings as a NumPy file

print(f"Saved files")