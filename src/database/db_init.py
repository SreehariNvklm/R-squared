from pymilvus import MilvusClient, CollectionSchema, FieldSchema, DataType, Collection
from sentence_transformers import SentenceTransformer
import os

# Initialize the embedded Milvus instance with a local database file.
# This creates/opens a Milvus database in-process.
client = MilvusClient("milvus_demo.db")

# Load SentenceTransformer model and determine the embedding dimension.
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
embedding_dim = model.get_sentence_embedding_dimension()

collection_name = "text_embeddings"

# Define the collection schema.
schema = CollectionSchema(
    fields=[
        FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
        FieldSchema(name="file_number", dtype=DataType.INT64),
        FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=embedding_dim),
    ],
    description="Text file embeddings collection"
)

# Create collection if it does not exist; otherwise, get the existing collection.
# if not client.has_collection(collection_name):
#     collection = client.create_collection(collection_name, schema)
# else:
#     pass
# Directory where text files are stored
collection1 = Collection(name=collection_name, schema=schema, using='default' )
data_dir = "/path"

# Process text files and prepare data for insertion.
entities = []
for i in range(0, 2):
    file_path = os.path.join(data_dir, f"text_{i}.txt")
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read().strip()
        # Generate embedding and convert to list format.
        embedding = model.encode(text).tolist()
        entities.append([i, embedding])

# Insert embeddings into Milvus and load the collection.
if entities:
    data = {
        "file_number": [row[0] for row in entities],
        "embedding": [row[1] for row in entities]
    }
    client.insert(collection_name, data)
    collection1.load()
    print(f"Inserted {len(entities)} embeddings into Milvus")
