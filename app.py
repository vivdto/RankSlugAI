import streamlit as st
import re
from deep_translator import GoogleTranslator
from unidecode import unidecode

# Function to generate SEO-friendly slugs
def generate_slug(text, target_lang="en"):
    translated_text = GoogleTranslator(source="auto", target=target_lang).translate(text)
    english_text = unidecode(translated_text)
    english_text = re.sub(r'[^a-zA-Z0-9\s]', '', english_text).lower()

    stop_words = {"the", "of", "in", "and", "to", "a", "is", "for", "on", "with", "by", "at", "from", "this", "that", "an", "it", "as", "or", "if", "be", "so", "was", "were", "but", "not"}
    words = english_text.split()
    filtered_words = [word for word in words if word not in stop_words]

    slug = "-".join(filtered_words)
    slug = "-".join(slug.split("-")[:8])  # Limit to 8 words
    return slug

# Streamlit UI Config
st.set_page_config(page_title="RankSlugAI - AI SEO Slug Generator", page_icon="🚀", layout="centered")

st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Mukta:wght@400;700&display=swap');

        body {background-color: #f9f9f9; font-family: 'Merriweather', serif;}
        .main-container {max-width: 700px; margin: auto; padding: 40px; background: white; border-radius: 10px; box-shadow: 0px 4px 10px rgba(0,0,0,0.1);}
        h1 {color: #1a73e8; text-align: center; font-size: 36px; font-weight: bold; font-family: 'Merriweather', serif; margin-bottom: 20px;}
        .stTextInput input {font-family: 'Mukta', sans-serif; font-size: 16px;}
        .stButton>button {background-color: #1a73e8; color: white; border-radius: 8px; padding: 12px 24px; font-size: 18px; font-weight: bold; width: 100%; transition: 0.3s;}
        .stButton>button:hover {background-color: #0f5bbd; transform: scale(1.05);}
        .slug-box {background-color: #e8f0fe; padding: 15px; border-radius: 8px; font-size: 18px; font-weight: bold; text-align: center; color: #1a73e8; font-family: 'Merriweather', serif;}
        .copy-btn {background-color: #1a73e8; color: white; border-radius: 5px; padding: 12px 20px; font-size: 16px; width: 100%; border: none; cursor: pointer; font-family: 'Merriweather', serif; transition: 0.3s;}
        .copy-btn:hover {background-color: #0f5bbd; transform: scale(1.05);}
        .insights {background: #eef5ff; padding: 20px; border-radius: 10px; margin-top: 30px; font-family: 'Merriweather', serif;}
        .footer {text-align: center; margin-top: 40px; color: #666; font-size: 14px; font-family: 'Merriweather', serif;}
    </style>
""", unsafe_allow_html=True)

# Main Container
# st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.title("🚀 RankSlugAI — Slug Using AI")

# Image (Centered Properly)
st.image("https://www.easywp.com/wp-content/uploads/2023/09/EasyWP-7-seo-factors-slug-1-cover-1.png", use_container_width=True)

# Input Box
text_input = st.text_input("Enter Your Title (Any Language):")

if st.button("Generate SEO Slug"):
    if text_input:
        slug = generate_slug(text_input)
        st.markdown(f'<div class="slug-box" id="slug">{slug}</div>', unsafe_allow_html=True)

        # Copy to clipboard button (Using JavaScript)
        copy_script = f"""
        <script>
        function copyToClipboard() {{
            navigator.clipboard.writeText("{slug}");
            alert("✅ You have copied the slug! Now go rank your site! 🚀");
        }}
        </script>
        <button class="copy-btn" onclick="copyToClipboard()">📋 Copy to Clipboard</button>
        """
        st.markdown(copy_script, unsafe_allow_html=True)
    else:
        st.warning("⚠ Please enter a title.")

# Insights Section (No Blank Space)
# st.markdown('<div class="insights">', unsafe_allow_html=True)
st.subheader("📈 How Slug Optimization Boosts SEO Performance")
st.write("""
- **40% of users** click on URLs with clear and readable slugs.
- **Google ranks URLs** with structured slugs **15% higher** than messy ones.
- A well-optimized slug **reduces bounce rates by 12%**.
- **Short & keyword-rich slugs** increase CTR by **30% on average**.
""")
st.image("https://www.elegantthemes.com/blog/wp-content/uploads/2015/01/WordPress-Slugs-Featured-Image.png", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# Footer (No Extra Space)
st.markdown('<div class="footer">', unsafe_allow_html=True)
st.write("🔹 Made by **Vivashwat Thakur** | [Read my blogs on Medium](https://medium.com/@vivdto/)")
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)  # Closing Main Container
