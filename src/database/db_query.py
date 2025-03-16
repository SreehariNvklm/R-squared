import faiss
from sentence_transformers import SentenceTransformer
import os
from dotenv import load_dotenv
import google.generativeai as genai
import glob

load_dotenv()

class DB_Query:
  def __init__(self):
    self.model = SentenceTransformer("all-MiniLM-L6-v2")
    self.embedding_dim = 384
    self.index_id = faiss.read_index("R-squared/faiss_index.bin")
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    self.gen_model = genai.GenerativeModel("gemini-2.0-flash")

  def search_faiss(self, query_text, top_k=3):
    """Searches FAISS for similar documents and returns detailed results."""
    query_embedding = self.model.encode([query_text]).astype("float32")

    distances, indices = self.index_id.search(query_embedding, top_k)
    files = []
    f = ""
    j = 0
    for i in glob.glob("R-squared/output_text/*/*.txt"):
      if j in indices[0][:top_k]:
        with open(i,"r",encoding='utf-8') as file:
          f = file.read()
          files.append(f)
          print(f)
      j += 1
    response = self.gen_model.generate_content(f"Provided a collection of case file report, which is publicly available. Separate them, and, Correct the spelling only if there is a mistake and report the file as such. No extra content generation is allowed. Don't add any extra line from your intelligence. Don't add like, File corrected:, Correctly spelled: or any as such Case file report: {files}")
    
    return response.text