# 📚 Automated Book Publication Workflow

A complete AI-powered system to automate book publication by scraping web content, rewriting with LLMs (Gemini), supporting human-in-the-loop revisions, and storing final versions using ChromaDB.

---

## 🔧 Features

- ✅ Scrapes and screenshots content from [Wikisource](https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1)
- ✅ AI Writer: Rewrites chapters using Gemini LLM
- ✅ Human-in-the-loop editing interface
- ✅ Versioning via ChromaDB
- ✅ Intelligent retrieval with RL Search Algorithm

---

## 🛠 Tech Stack

- Python
- Playwright
- Google Gemini API (Generative AI)
- ChromaDB
- Streamlit (optional interface)
- RL-based search (planned)

---
## 📦 Folder Structure

automated-book-publication-workflow/
│
├── ai_modules/
│ └── writer.py # Gemini AI rewriting logic
│
├── outputs/
│ └── chapter1_rewritten.txt # Sample output
│
├── main.py # Core script for loading, rewriting, and saving chapters
├── scraper.py # Playwright-based scraper
├── test_models.py # Lists available Gemini models
├── requirements.txt # All required packages
└── README.md # This file

----

## 🚀 How to Run

1. Install requirements:
     pip install -r requirements.txt
   
3. Add your Gemini API Key in writer.py:
    genai.configure(api_key="YOUR_API_KEY_HERE")
   
3. Run the workflow:
      python main.py

----

## Screenshots

![image](https://github.com/user-attachments/assets/ef1f6693-c975-4420-8fb3-4b56e32027ed)

![image](https://github.com/user-attachments/assets/d5394095-6d2c-40c8-9ffc-54546088cf02)

![image](https://github.com/user-attachments/assets/eb1bf4b0-24d5-4b4c-b69b-0e9512cc805b)




