from pymilvus import connections, utility, Collection

# Connect to Milvus
connections.connect("default", host="localhost", port="19530")

# Load the collection
collection_name = "my_collection"
collection = Collection(collection_name)

# Load a text embedding model (e.g., Sentence-BERT)

embedding_fn = model.DefaultEmbeddingFunction()
docs = [
    "Artificial intelligence was founded as an academic discipline in 1956.",
    "Alan Turing was the first person to conduct substantial research in AI.",
    "Born in Maida Vale, London, Turing was raised in southern England.",
]
vectors = embedding_fn.encode_documents(docs)
data = [
    {"id": i, "vector": vectors[i], "text": docs[i], "subject": "history"}
    for i in range(len(vectors))
]

print("Data has", len(data), "entities, each with fields: ", data[0].keys())
print("Vector dim:", len(data[0]["vector"]))
# Perform a vector search in Milvus
# search_params = {"metric_type": "L2", "params": {"nprobe": 10}}
# results = collection.search(
#     data=[query_vector], 
#     anns_field="vector",  
#     param=search_params,
#     limit=5,  # Get top 5 similar results
#     output_fields=["id", "name", "description"]
# )

# # Print the retrieved entities
# for hits in results:
#     for entity in hits:
#         print(f"ID: {entity.id}, Name: {entity.entity.get('name')}, Description: {entity.entity.get('description')}")
#added in random change