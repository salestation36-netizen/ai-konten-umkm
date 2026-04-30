import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("AI Konten Jualan UMKM 🇮🇩")

produk = st.text_input("Nama Produk")
bisnis = st.text_input("Jenis Bisnis")

if st.button("Generate Konten"):
    prompt = f"""
    Buat:
    - 5 caption jualan
    - 5 ide konten TikTok
    - 1 script video pendek

    untuk produk {produk}
    bisnis {bisnis}

    target: anak muda Indonesia
    gaya: santai, menarik, tidak kaku
    """

    res = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    st.write(res.choices[0].message.content)
