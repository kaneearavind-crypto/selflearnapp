# 📘 SelfLearnApp – Subject-Wise AI Study Assistant

**SelfLearnApp** is an offline academic learning assistant designed for students and professors. It allows professors to upload academic material and helps students query subject-specific content using an offline LLM for accurate and fast answers.

---

## Features

* ✅ Subject-wise academic assistant
* ✅ Upload files: PDF, DOCX, TXT, PPTX
* ✅ Offline LLM powered by Ollama (Mistral model)
* ✅ Accurate answers from uploaded material only
* ✅ Stores and retrieves information in a ChromaDB vector database

---

## Supported Subjects

* Research Methodology and IPR
* Advanced Software Testing
* Large Language Models
* Cloud Architecture and Computing
* Mini Project
* Professional Communication
* AI-Driven Cybersecurity
* Agile Software Development

---

## Installation

1. **Clone the repository**:

```bash
git clone https://github.com/yourusername/SelfLearnApp.git
cd SelfLearnApp
```

2. **Create a virtual environment and install dependencies**:

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

**Dependencies include**:

* `streamlit`
* `PyPDF2`
* `python-docx`
* `python-pptx`
* `chromadb`
* `ollama`

---

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

### Navigation

* **🏠 Home** – Overview of the app.
* **📂 Professor Upload** – Upload academic materials for each subject.
* **🔍 Ask Questions** – Query uploaded content and get answers from the offline LLM.
* **📊 Admin** – View statistics such as the total number of stored chunks.

---

### Professor Upload

1. Select a subject from the dropdown.
2. Upload PDF, DOCX, TXT, or PPTX files.
3. The app will process the files, split them into chunks, and store them in ChromaDB.

---

### Ask Questions

1. Select a subject to query.
2. Enter your question.
3. The LLM will provide an answer strictly based on the uploaded material.

> If the answer is not in the uploaded content, the assistant will respond:
> `"Not available in uploaded material."`

---

## File Handling

* **PDF** → Extracts text from pages.
* **TXT** → Reads plain text.
* **DOCX** → Extracts text from paragraphs.
* **PPTX** → Extracts text from slides.

---

## ChromaDB Vector Storage

* Stores document chunks with metadata (`subject` and `source`) for semantic search.
* Uses unique UUIDs for each chunk.
* Supports querying by subject for precise retrieval.

---

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
