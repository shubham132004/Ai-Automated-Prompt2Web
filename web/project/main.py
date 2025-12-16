# import streamlit as st
# import langchain
# from langchain_google_genai import GoogleGenerativeAI , ChatGoogleGenerativeAI
# from dotenv import load_dotenv
# import zipfile

# load_dotenv()

# import os 
# os.environ["GOOGLE_API_KEY"] = os.getenv("gemini")

# st.set_page_config(page_title = "Ai Website Generator" , page_icon = "🤧")

# st.title("AI AUTOMATED WEBSITE CREATION")

# prompt = st.text_area("write here about your website")

# if st.button("Generate"):
#     message = [("system" , """you are an expert in web development creating professional websites .
#                 So create html , css , java script code for creating a frontend based 
#                 website based on the user prompt . And make it colorfull 
                
#                 the output should be in the below format:
                
#                 --html--
#                 [html code]
#                 --html--
                
#                 --css--
#                 [css code]
#                 --css--
                
#                 --js--
#                 [js code]
#                 --js--
#                 """)]
#     message.append(("user" , prompt))
    
#     model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash-lite")
    
#     response = model.invoke(message)
    
#     # with open("file.txt" , "w") as file:
#     #     file.write(response.content)
#     with open("index.html" , "w") as file:
#         file.write(response.content.split("--html--")[1])
        
#     with open("style.css" , "w") as file:
#         file.write(response.content.split("--css--")[1])
        
#     with open("script.js" , "w") as file:
#         file.write(response.content.split("--js--")[1])
        
        
    
#     with zipfile.ZipFile("website.zip" , "w") as zip:
#         zip.write("index.html")
#         zip.write("style.css")
#         zip.write("script.js")
        
        
#     st.download_button("click to download" , 
#                           data = open("website.zip" , "rb") , 
#                           file_name = "website.zip")
#     st.write("success")



import streamlit as st
import os
import zipfile
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# ============================================================
# ENVIRONMENT SETUP
# ============================================================
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("gemini")

# ============================================================
# STREAMLIT PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="AI Automated Website Generator",
    page_icon="🌐",
    layout="centered"
)

# ============================================================
# STREAMLIT UI STYLING (LIGHT BLUE–PURPLE THEME)
# ============================================================
st.markdown("""
<style>
    /* App Background */
    .stApp {
        background: linear-gradient(135deg, #eef2ff, #e0e7ff, #f5f3ff);
        background-attachment: fixed;
    }

    .main {
        padding: 2rem;
    }

    h1 {
        text-align: center;
        color: #1e1b4b;
        font-weight: 700;
    }

    p {
        color: #334155;
        text-align: center;
    }

    /* Text Area */
    .stTextArea textarea {
        font-size: 16px;
        border-radius: 14px;
        padding: 16px;
        background-color: #ffffff;
        color: #1e293b;
        border: 1px solid #c7d2fe;
    }

    /* Button */
    .stButton button {
        background: linear-gradient(135deg, #6366f1, #8b5cf6);
        color: #ffffff;
        font-size: 16px;
        font-weight: 600;
        border-radius: 14px;
        padding: 12px 28px;
        border: none;
        transition: all 0.35s ease;
        box-shadow: 0 8px 20px rgba(99, 102, 241, 0.35);
    }

    .stButton button:hover {
        transform: translateY(-2px) scale(1.04);
        box-shadow: 0 14px 30px rgba(139, 92, 246, 0.45);
        background: linear-gradient(135deg, #8b5cf6, #6366f1);
    }

    /* Success Message */
    .stAlert-success {
        background: #ecfeff;
        color: #065f46;
        border-radius: 12px;
        border-left: 6px solid #6366f1;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# APP TITLE & INPUT
# ============================================================
st.title("🤖 AI Automated Website Creation")
st.write("Describe your website idea and get a **beautiful, modern frontend** instantly.")

prompt = st.text_area(
    "📝 Describe your website",
    placeholder="Example: A modern landing page for an AI startup with hero section, features, testimonials, and contact form..."
)

# ============================================================
# GENERATE WEBSITE
# ============================================================
if st.button("✨ Generate Website"):

    if not prompt.strip():
        st.warning("Please enter a website description.")
        st.stop()

    with st.spinner("Generating a stunning website..."):

        messages = [
            (
                "system",
                """
You are a senior UI/UX designer and expert frontend web developer.

Your task is to generate a **modern, visually stunning, and fully responsive website** based on the user's prompt.

### Design Requirements:
- Light bluish–purplish color palette
- Modern UI/UX principles
- Clean layout with proper spacing
- Soft gradients & subtle shadows
- Smooth hover effects and animations
- Fully responsive design
- Google Fonts usage
- Card-based sections
- Professional typography

### Technical Requirements:
- Pure HTML, CSS, JavaScript only
- No frameworks (no Bootstrap, React, Tailwind)
- Semantic HTML
- Flexbox/Grid layout
- JavaScript for interactivity

### Output Format (STRICT):

--html--
[HTML code]
--html--

--css--
[CSS code]
--css--

--js--
[JavaScript code]
--js--
"""
            ),
            ("user", prompt)
        ]

        model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
        response = model.invoke(messages)
        content = response.content

        # ====================================================
        # FILE GENERATION
        # ====================================================
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(content.split("--html--")[1])

        with open("style.css", "w", encoding="utf-8") as f:
            f.write(content.split("--css--")[1])

        with open("script.js", "w", encoding="utf-8") as f:
            f.write(content.split("--js--")[1])

        # ====================================================
        # ZIP FILE CREATION
        # ====================================================
        zip_path = "website.zip"
        with zipfile.ZipFile(zip_path, "w") as zipf:
            zipf.write("index.html")
            zipf.write("style.css")
            zipf.write("script.js")

        # ====================================================
        # DOWNLOAD BUTTON
        # ====================================================
        st.success("🎉 Website generated successfully!")
        st.download_button(
            label="⬇️ Download Website (ZIP)",
            data=open(zip_path, "rb"),
            file_name="website.zip",
            mime="application/zip"
        )
