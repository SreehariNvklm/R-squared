# Architecture

![workflow](workflow.png)

## Dataset
The dataset given was in .pdf format. It contained 1,088 entries, each having an average of 5 pages per case. These cases have details like:

* High Court Judge who is ruling
* The plaintiff/plaintiffs
* The defendant/defendants
* The police station that filed the case
* The evidence submitted to the court
* The final Verdict given by the court.

## Image Conversion
As direct text extraction isn't possible, first its necessary to transform each page of the image into individual images that can be converted to text using OCR models.
These models help convert Images that contain text into a text format for extracting information.

## Text Embedding
The main idea we propose is the use of a vector database as opposed to a standard SQL database as it allows us to store text data by taking its work embedding.
This allows for a storage of 'similar' documents nearby. This means that the documents that are nearer each other are by nature similar in properties.

## Text retrieval
The user's query is converted to vector embeddings and then a similarity metric(eg: Cosine similarity) is used to find the vectors(corresponding to each stored document) that are the most similar to the user query. The top "k" most similar docments are returned/retrieved from the vector database.

## ChatBot
The retrieved text(court document) is sent to the large language model as context. The model then generates a response with respect to the user query and the passed textual document.

# Design
## PDF to Image conversion
- *Logic* : Straightforward text extraction from the pdfs not possible due to its inherent image nature. Therefore conversions to image files is necessary.
- *Used PyMuPdf* - a Python binding for the MuPdf library to facilitate lightweight, high performance conversion of Pdf files to other supported formats, here for pdf to image conversions.
```bash
import pymupdf
```
- Directories created for each pdf file -> Converted to image file(per pdf page) -> stored under respected file directories(.png).

```bash
self.doc = pymupdf.open(pdf_file)       #from src/components/pdf_ocr_extractor.py
for page_num in range(len(self.doc)):
    page = self.doc[page_num]
    pix = page.get_pixmap()
    img_path = f"output_images/{img_counter}/page_{page_num + 1}.png"
    pix.save(img_path)
```

## Text extraction from Image files
- *Logic* : The contents present in the images are to be extracted in a textual format to make the information accessable, retrievable and storable.
- *Used PyTesseract* - a Python wrapper for the open-source OCR(Optical Character Recognition) library developed by Google, Tesseract.
bash
import pytesseract
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"


- Directories created for each converted image -> PyTesseract for converting images to strings of text -> Extracted text stored under respective directories(.txt).

```bash
for image_file in glob.glob(image_folder + "/*.png"):     #from src/components/pdf_ocr_extractor.py
    text = text + " " + pytesseract.image_to_string(image_file)
with open(f"output_text/{text_counter}/text_{text_counter}.txt","w") as f:
    f.write(text)
```

## Vector Embeddings
- *Logic* : The extracted textual data are to be converted to vectore embeddings in N-dimensional space for capturing semantic meaning and relationships. Computational efficiency to be improved and for efficient data storage.
- *Used Sentence-Transformer* - a Python library built on top of Pytorch and Hugging Face Transformers, for creating sentence embeddings. Uses pretrained transformer models. 
```bash
from sentence_transformers import SentenceTransformer
```

- *We use "all-Mini-L6-v4" pretrained transformer model.* - Lightweight, high performance regarding semantic similarity, fast inference.
```bash
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
```

- Textual files retreived -> Converted to embeddings then formatted into arrays of embeddings -> each array embedding is indexed
```bash
embeddings = model.encode(all_docs)         #from src/database/db_init.py
embeddings = np.array(embeddings).astype('float32')
ids = np.array([i for i in range(len(all_docs))])
```

## Vector Database
- *Logic* : The vector embeddings of the documents are to be stored in a database to facilitate efficient retrieval, updation, deletion, and for computing semantic similarity - with respect to the user queries.
- *Used FAISS database* - (Facebook AI Similarity Search) an open-source library developed by FAIR. It is optimized to better handle high-dimensional data and accurate similarity searches, thereby making it suitable for handling large scale datasets and high-dimensional vectors such as embeddings from NLP tasks.
```bash
import faiss
```
-Built a faiss index -> created indexing for each embedding -> added to the faiss index -> saved to bin
```bash
index_id = faiss.IndexIDMap(index)
index_id.add_with_ids(embeddings, ids)
faiss.write_index(index, "R-squared/faiss_index.bin")
```

## LLM (ChatBot)
- *Logic* : A large language model is required for accepting semantically similar documents form the database (with respect to the user query) and responding with those documents as context. For implementing Retrieval Augmented Generation(RAG) upon the court documents.
- *Used gemini-2.0-flash* - Multimodel LLM developed by Google.
```bash
import google.generativeai as genai
gen_model = genai.GenerativeModel("gemini-2.0-flash")
```
- Used the model's API call for response generation -> we only make use of its text generation capabilities for our application.
```bash
#from src/database/db_query.py
response = self.gen_model.generate_content(f"Provided a case file report, ....  as such Case file report: {f}")
##refer Chat.py as well!
```

## User-Interface
- *Logic* : A simple and intuitive UI to guide the users to query from the database as well as to chat with the llm.
- *Used Streamlit* - an open-source Python library to create custom web applications.
```bash
import streamlit as st
```

- Built streamlit app to combine the modules for Faiss database, user query processing and response generation from the llm to implement a complete responsive system.
```bash
#refer to Chat.py and Verdict.py
streamlit run Verdict.py  #in terminal
```

- Added additional functionality for accepting user inputs to retrieve data from the vector database(Querying), so as to retrive and display the appropriate court document within the web application.     *ChatBot|Database querying*
```bash
from src.database.db_query import DB_Query   #from Verdict.py
res = query_obj.search_faiss(user_input,2)
container.write(res)
```

# Scalability - Possible further improvments
- *Migrating from Streamlit to Django* : Streamlit is a python library that focuses on building simple, small scale web application. Therefore migrating to React with Django(amongst other) is necessary to make the web application scalable, introducing functionalities such as user logins and auth verifications.
- *Using NER(Named Entity Recognition)* : for enforcing a layer of confidentiality and privacy. Names of individuals from the general public, involved in the court proceedings and other such sensitive information can be censored or removed from the responses.
