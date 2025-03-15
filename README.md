# Team R-squared

## Valid Extraction and Retrieval of Data from Information on Court Trials(VERDICT)
A fully connected pipeline for people to access their court cases, to retrieve data, to ask doubts and to ask for guidance using a chatbot feature. 
## What's VERDICT? 
### Features
- **PDF Processing:** Convert court case PDFs into images using pymupdf and extract text using OCR.
- **Search & Query:** Index extracted data for efficient searching and querying.
- **Chatbot Interface:** Interact with the dataset using natural language queries.

This project extracts text from court case PDFs and converts it into images. Using OCR, we then convert it to an image and then using pytesseract, we extract the text and feed it to a vector database model. This approach allows us to query search results in an efficient manner and with accuracy. 

## Installation
#### First, run
```bash
https://github.com/Joel-VO/R-squared.git
```


### **Setup**
Clone the repository:
```bash
git clone https://github.com/yourusername/court-case-bot.git
cd court-case-bot
```
