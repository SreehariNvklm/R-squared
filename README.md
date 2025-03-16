# Team R-squared

## Valid Extraction and Retrieval of Data from Information on Court Trials(Project VERDICT)
A fully connected pipeline for people to access their court cases, to retrieve data, to ask doubts and to ask for guidance using a chatbot feature. 
## What's Project VERDICT? 
### Features
- **PDF Processing:** Convert court case PDFs into images using pymupdf and extract text using OCR.
- **Search & Query:** Index extracted data for efficient searching and querying using a vector database.
- **Chatbot Interface:** Interact with the dataset using natural language queries.

This project extracts text from court case PDFs and converts it into images. Using OCR, we then convert it to an image and then using pytesseract, we extract the text and feed it to a vector database model. This approach allows us to query search results in an efficient manner and with accuracy. 

## Installation
### Running Locally
#### **For Linux/Mac**
```bash
git clone https://github.com/Joel-VO/R-squared.git
```

```bash
python venv -m venv
source venv/bin/activate
pip install -r requirements.txt
```
```bash
streamlit run app.py
```
#### **For Windows**
```bash
git clone https://github.com/Joel-VO/R-squared.git
```

```bash
python -m venv venv 
# Terminal
path\to\venv\Scripts\activate 
# PowerShell
.\path\to\venv\Scripts\Activate 
pip install -r requirements.txt
```
```bash
streamlit run app.py
```

## Documentation and related information
* A comprehensive Documentation covering all aspects of our code can be found in [DOCUMENTATION.md](#/DOCUMENTATION.md)
* Licensed under GPL 3.0 Licensing, covered here in [LICENSE.md](#/LICENSE.md).

