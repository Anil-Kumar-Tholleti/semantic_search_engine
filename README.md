# 🧠 Semantic Search Engine for PDF Documents

This is a simple, in-memory **semantic search engine** for extracting and querying information from multiple PDF files.
Built using **Python**, **Sentence Transformers**, and **FAISS**, it allows users to enter natural language queries and
retrieve the most semantically relevant text chunks across multiple documents.

---

## 🚀 Features

- ✅ Parses and extracts text from one or more PDFs
- ✅ Splits content into manageable text chunks
- ✅ Converts text chunks into vector embeddings using pretrained transformer models
- ✅ Stores vectors in an in-memory FAISS index for fast similarity search
- ✅ Accepts runtime user queries and returns top N matching results
- ✅ Outputs: matching text, source file name, and cosine similarity score

---

## 📂 Folder Structure

semantic_search_engine/
├── main.py
├── requirements.txt
├── .gitignore
├── pdfs/ # Place your PDF files here
└── utils/
├── pdf_parser.py
├── embedding_generator.py
└── search_engine.py

---

## 🛠️ Tech Stack & Libraries

| Purpose              | Tool / Library              |
|----------------------|-----------------------------|
| PDF Parsing          | `PyPDF2`                    |
| Text Embeddings      | `sentence-transformers`     |
| Vector Search        | `faiss-cpu`                 |
| Language             | Python 3.8+                 |

---

## 📥 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/your-username/semantic-search-engine.git
cd semantic-search-engine
2. Create virtual environment (optional but recommended)
python -m venv env
source env/bin/activate    # On Windows: env\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Add PDFs
Place your .pdf files inside the /pdfs/ folder.

▶️ Run the App
python main.py
You’ll be prompted to enter a search query like:
Enter your search query: artificial intelligence in healthcare
The app will display the top matching text chunks from the PDF documents based on semantic similarity.

📤 Sample Output
yaml
Copy
Edit
📌 Top Results:

🔹 Result 1
📄 File: healthcare_ai.pdf
🧾 Text: AI is transforming healthcare by enabling predictive diagnostics...
📊 Similarity Score: 0.0921
🧪 Testing
You can generate test PDFs using tools like:

Microsoft Word → Save as PDF

PDFescape


❌ What Not to Commit
Your .gitignore will already prevent these:

bash
Copy
Edit
env/
__pycache__/
*.pyc
*.log
*.pdf
✅ This keeps your GitHub repo clean and professional.

📜 License
This project is open-source and available under the MIT License.
