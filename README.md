![Python](https://img.shields.io/badge/Python-3.10-blue)
![Groq](https://img.shields.io/badge/LLM-Groq-purple)
![Llama](https://img.shields.io/badge/Model-Llama_3.3_70B-green)
![Prompt Engineering](https://img.shields.io/badge/Prompt-Engineering-orange)
![Pydantic](https://img.shields.io/badge/Structured-Outputs-red)

# 🎥 AI YouTube Video Summarizer

An AI-powered YouTube Video Summarizer built using **Groq API** and **Llama 3.3** that automatically extracts a video's transcript and generates a structured summary, key insights, and actionable takeaways.

This project demonstrates how modern LLM-powered applications process external data, engineer prompts, generate structured outputs, and validate responses using **Pydantic**.

---

## 🚀 Features

- 🎥 Accepts any YouTube video URL
- 📝 Automatically extracts video transcripts
- 🤖 Uses Groq API with Llama 3.3 for summarization
- 📄 Generates concise summaries
- 💡 Extracts key insights
- ✅ Identifies actionable takeaways
- 🧠 Uses Prompt Engineering for better responses
- 📦 Returns structured outputs using Pydantic
- 🔐 Secure API key management using environment variables

---

## 🏗️ Architecture

```text
User enters YouTube URL
            │
            ▼
Extract Video ID
            │
            ▼
Fetch Transcript
            │
            ▼
Prompt Engineering
            │
            ▼
Groq API (Llama 3.3)
            │
            ▼
JSON Response
            │
            ▼
Pydantic Validation
            │
            ▼
Summary
Key Insights
Action Items
```

---

## 📂 Project Structure

```text
youtube-video-summarizer/
│
├── app.py                 # Main application
├── transcript.py          # Transcript extraction logic
├── llm.py                 # Groq API integration
├── prompts.py             # Prompt templates
├── models.py              # Pydantic models
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python |
| LLM | Groq API |
| Model | Llama 3.3 70B Versatile |
| Prompting | Prompt Engineering |
| Validation | Pydantic |
| Transcript Extraction | youtube-transcript-api |
| Environment Variables | python-dotenv |

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/youtube-video-summarizer.git

cd youtube-video-summarizer
```

---

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

#### Windows

```bash
.venv\Scripts\activate
```

#### Mac/Linux

```bash
source .venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Setup

Create a `.env` file inside the project root.

```env
GROQ_API_KEY=your_groq_api_key
```

You can obtain your API key from the Groq Console.

---

## ▶️ Running the Project

Run the application.

```bash
python app.py
```

Enter a YouTube URL when prompted.

Example:

```text
Enter YouTube URL:
https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

---

## 💡 How It Works

1. User provides a YouTube video URL.
2. The application extracts the video ID.
3. The transcript is fetched using `youtube-transcript-api`.
4. A carefully engineered prompt is constructed.
5. The transcript is sent to Groq's Llama 3.3 model.
6. The model returns structured JSON.
7. Pydantic validates the response.
8. The application displays:
   - Summary
   - Key Insights
   - Action Items

---

## 🧠 Key Concepts Learned

### 1. API Integration

Connecting Python applications with external AI services.

### 2. Prompt Engineering

Designing prompts that produce reliable and structured outputs.

### 3. Structured Outputs

Generating machine-readable JSON responses from LLMs.

### 4. Pydantic

Validating structured AI outputs before using them.

### 5. Modular Application Design

Separating responsibilities into independent modules for better maintainability.

---

## 🚀 Future Improvements

- 🎨 Rich CLI interface
- 🌐 Streamlit web application
- ⚡ FastAPI REST API
- 📝 Markdown export
- 📄 PDF summary generation
- 🌍 Multi-language transcript support
- 🕒 Timestamp-aware summaries
- 📚 Long-video chunking support
- 🧠 Native Groq Structured Outputs
- 💾 Summary caching

---

## ⚠️ Limitations

- Videos without transcripts cannot be summarized.
- Very long transcripts may exceed the model context window.
- Supports publicly available YouTube videos only.
- Internet connection is required.

---

## 📚 Learning Outcomes

After building this project, you understand:

- Working with external APIs
- Prompt Engineering fundamentals
- Groq API integration
- LLM-powered application architecture
- Structured outputs using JSON
- Pydantic validation
- Environment variable management
- Modular Python project organization

---

## 🤝 Contributing

Contributions are welcome!

Potential improvements include:

- Better prompt optimization
- Improved error handling
- Additional export formats
- Enhanced UI
- Multi-model support
- Better transcript preprocessing

---

## ⭐ Acknowledgements

- Groq for ultra-fast LLM inference
- Meta for the Llama models
- youtube-transcript-api for transcript extraction
- Pydantic for data validation

---

## 👨‍💻 Author

Built as a learning project while exploring **Generative AI**, **Prompt Engineering**, **LLM Applications**, and **AI Engineering**.

