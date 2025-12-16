# 🤖 AI Automated Website Generator


https://github.com/user-attachments/assets/d5796a31-37cc-446c-b6b1-0fb4f1e78ac3


An **AI-powered automated website generator** that creates **beautiful, modern, and responsive frontend websites** instantly based on a simple text prompt.

This project leverages **LangChain** with **Google Gemini (gemini-2.5-flash-lite)** to generate complete frontend code and deliver it as a downloadable ZIP file — ready to use in seconds.

---

## 🚀 Project Overview

Building a website from scratch takes time and design skills.  
This project solves that problem by allowing users to:

- Describe the type of website they want
- Click **Generate Website**
- Instantly receive a **fully functional frontend website**

The generated website includes:
- `index.html`
- `style.css`
- `script.js`

All files are neatly packaged into a **ZIP file**, which can be extracted and opened directly in the browser.

---
| Feature | Description |
|------|------------|
| Project Name | AI Automated Website Generator |
| Type | AI-Powered Frontend Code Generator |
| Input | Natural Language Website Prompt |
| Output | HTML, CSS & JavaScript (ZIP file) |
| UI Framework | Streamlit |
| AI Model | Gemini-2.5-Flash-Lite |
| LLM Orchestration | LangChain |
| API Integration | Google Gemini API |

---
## ✨ Key Features

- 🧠 **AI-Powered Website Creation**
- ⚡ Instant frontend code generation
- 🎨 Modern UI with light blue–purple theme
- 📦 Auto-generated ZIP file
- 🖥️ Fully responsive design
- 🧩 Clean separation of HTML, CSS & JavaScript
- 🚫 No frameworks (pure frontend)
- 🌐 Semantic HTML & professional UI/UX

---

## 🛠️ Tech Stack

| Technology | Usage |
|----------|------|
| **Python** | Backend logic |
| **Streamlit** | Web application UI |
| **LangChain** | LLM orchestration |
| **Google Gemini API** | Code generation |
| **HTML** | Website structure |
| **CSS** | Styling & layout |
| **JavaScript** | Interactivity |

---

## 🧠 AI Model Used

- **Model:** `gemini-2.5-flash-lite`
- **Provider:** Google Gemini
- **Integration:** LangChain + Gemini API Key

---

## 🧾 System Prompt Logic

The AI is instructed with a **strict system prompt** to:

- Generate **three separate files**
  - `.html`
  - `.css`
  - `.js`
- Use:
  - Semantic HTML
  - Flexbox / Grid
  - Modern UI principles
- Avoid:
  - Bootstrap
  - React
  - Tailwind
  - Any frontend framework

### Technical Requirements Enforced:
- Pure HTML, CSS, JavaScript only
- Responsive layout
- Clean code structure
- JavaScript-based interactivity

---

## 🧑‍💻 How It Works

1. User enters a website description (prompt)
2. Clicks **Generate Website**
3. Gemini model generates frontend code
4. Code is split into:
   - `index.html`
   - `style.css`
   - `script.js`
5. Files are zipped automatically
6. User downloads the ZIP file
7. Open `index.html` to preview the website 🎉

---

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/shubham132004/Ai-Automated-Prompt2Web.git
cd web
cd Scripts
activate
cd ..
cd project
streamlit run main.py
```

### 2️⃣ Install Dependencies
```
pip install streamlit, langchain ,langchain-google-genai , python-dotenv
```

### 3️⃣ Set Up Environment Variables

Create a .env file:

gemini=YOUR_GOOGLE_GEMINI_API_KEY

### 🔐 Environment Variable Security

To ensure security and follow best practices, the **Google Gemini API key is stored in a `.env` file**.

- The `.env` file keeps sensitive credentials **private and secure**
- API keys are **never hard-coded** into the source code
- Environment variables are loaded using `python-dotenv`

Example:
```env
gemini=YOUR_GOOGLE_GEMINI_API_KEY
```

### ▶️ Run the Application
streamlit run main.py

📥 Output Example

After generation, download the ZIP file and extract it:
```bash
website.zip
├── index.html
├── style.css
└── script.js
```

Just double-click index.html to see your website live in the browser 🚀

### 🎯 Use Cases

- Beginners learning frontend development

- Rapid website prototyping

- Hackathons & demos

- Startup landing pages

- Portfolio websites

- UI inspiration

### 🌟 Future Enhancements

- Multiple theme options

- Dark mode support

- Backend integration

- Hosting deployment option

- Image & asset generation

- Multi-page website support

### 🙌 Acknowledgements

- LangChain for LLM orchestration

- Google Gemini for powerful AI generation

- Streamlit for rapid UI development

📌 Author

- Shubham Parmar

