import streamlit as st
import re
from googletrans import Translator
from unidecode import unidecode

# Initialize Translator
translator = Translator()

def generate_slug(text, src_lang):
    # Translate text to English
    translated_text = translator.translate(text, src=src_lang, dest="en").text

    # Convert to ASCII (remove accents)
    english_text = unidecode(translated_text)

    # Remove special characters & convert to lowercase
    english_text = re.sub(r'[^a-zA-Z0-9\s]', '', english_text).lower()

    # Remove common stop words
    stop_words = {"the", "of", "in", "and", "to", "a", "is", "for", "on", "with", "by", "at", "from", "this", "that", "an", "it", "as", "or", "if", "be", "so", "was", "were", "but", "not"}
    words = english_text.split()
    filtered_words = [word for word in words if word not in stop_words]

    # Convert to slug format
    slug = "-".join(filtered_words)
    slug = "-".join(slug.split("-")[:8])  # Limit to 8 words

    return slug

# Streamlit UI
st.set_page_config(page_title="🔥 Get an SEO-Friendly Slug Using AI & Rank on Top! 🚀", page_icon="🚀", layout="wide")

# Custom Styling
st.markdown("""
    <style>
        .main-container {
            background-color: #f4f7fc;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        h1 {
            color: #1a73e8;
            text-align: center;
            font-size: 34px;
            font-weight: bold;
            animation: fadeIn 1.5s ease-in-out;
        }
        @keyframes fadeIn {
            0% { opacity: 0; transform: translateY(-10px); }
            100% { opacity: 1; transform: translateY(0); }
        }
        .stButton>button {
            background-color: #1a73e8;
            color: white;
            border-radius: 8px;
            padding: 14px 28px;
            border: none;
            font-size: 18px;
            font-weight: bold;
            width: 100%;
            transition: 0.3s ease-in-out;
        }
        .stButton>button:hover {
            background-color: #0f5bbd;
            transform: scale(1.05);
            box-shadow: 0px 4px 10px rgba(26, 115, 232, 0.3);
        }
        .slug-box {
            background-color: #e8f0fe;
            padding: 15px;
            border-radius: 5px;
            font-size: 20px;
            font-weight: bold;
            text-align: center;
            color: #1a73e8;
            box-shadow: 0px 3px 8px rgba(0, 0, 0, 0.1);
        }
        .insight-section {
            background-color: #ffffff;
            padding: 25px;
            border-radius: 12px;
            margin-top: 30px;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        .footer {
            text-align: center;
            font-size: 14px;
            margin-top: 30px;
            color: #666;
        }
        .img-container {
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            margin-bottom: 20px;
        }
        .img-container img {
            max-width: 70%;
            height: auto;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }
        @media (max-width: 768px) {
            .img-container img {
                max-width: 90%;
            }
        }
    </style>
""", unsafe_allow_html=True)

# Load Images
header_image_url = "https://www.easywp.com/wp-content/uploads/2023/09/EasyWP-7-seo-factors-slug-1-cover-1.png"
seo_insights_image_url = "https://www.elegantthemes.com/blog/wp-content/uploads/2015/01/WordPress-Slugs-Featured-Image.png"

# Header with Illustration
st.markdown('<div class="img-container">', unsafe_allow_html=True)
st.image(header_image_url, use_column_width=False, caption="SEO Slug Generator")
st.markdown('</div>', unsafe_allow_html=True)

st.title("🔥 Get an SEO-Friendly Slug Using AI & Rank on Top! 🚀")

# Language Selection
languages = {
    "Hindi": "hi",
    "English": "en",
    "Marathi": "mr",
    "Nepali": "ne",
    "Kannada": "kn"
}
selected_language = st.selectbox("🌎 Select Language:", list(languages.keys()))

# User Input
st.markdown('<div class="main-container">', unsafe_allow_html=True)
text_input = st.text_input("✍️ Enter Title in Selected Language:")
if st.button("🔍 Generate SEO Slug"):
    if text_input:
        slug = generate_slug(text_input, languages[selected_language])
        st.markdown(f'<div class="slug-box">✅ SEO Slug: `{slug}`</div>', unsafe_allow_html=True)
    else:
        st.warning("⚠ Please enter a title.")
st.markdown('</div>', unsafe_allow_html=True)

# Insights Section
st.markdown('<div class="insight-section">', unsafe_allow_html=True)
st.subheader("📊 Why SEO-Friendly Slugs Matter?")

st.markdown('<div class="img-container">', unsafe_allow_html=True)
st.image(seo_insights_image_url, use_column_width=False, caption="SEO Insights")
st.markdown('</div>', unsafe_allow_html=True)

st.write("""
- **🔹 Higher Click-Through Rate (CTR)** → URLs with relevant keywords get **30% more clicks**.
- **🔹 Google Ranking Boost** → SEO-friendly URLs rank **45% higher** in search results.
- **🔹 Better User Experience** → Structured URLs reduce bounce rates by **20%**.
- **🔹 Improved Social Media Sharing** → Descriptive slugs get **50% more shares**.
- **🔹 Mobile Optimization** → Short URLs improve performance for **58% of users**.
""")

# Footer
st.markdown("""
    <hr>
    <p class="footer">🚀 Made by <b>Vivashwat Thakur</b> | <a href="https://medium.com/@vivdto/" target="_blank">Read my blogs on Medium</a></p>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
