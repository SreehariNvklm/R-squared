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






# Scalability



