import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# CONFIG
st.set_page_config(
    page_title="AI Konten UMKM",
    page_icon="🚀",
    layout="wide"
)

# ===== CUSTOM CSS =====
st.markdown("""
<style>
.main {
    background-color: #0e1117;
}
.block-container {
    padding-top: 2rem;
}
h1, h2, h3 {
    color: #ffffff;
}
.stButton>button {
    background-color: #ff4b4b;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-weight: bold;
}
.stTextInput>div>div>input {
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# ===== HEADER =====
st.markdown("## 🚀 AI Konten Jualan UMKM")
st.markdown("Bikin **caption, ide konten, dan script video** dalam hitungan detik 💸")

st.markdown("---")

# ===== LAYOUT =====
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### ⚙️ Input Konten")

    produk = st.text_input("🛍️ Nama Produk")
    bisnis = st.text_input("🏪 Jenis Bisnis")

    tone = st.selectbox(
        "🎯 Tone Konten",
        ["Santai", "Formal", "Islami", "Hard Selling"]
    )

    jumlah = st.selectbox(
        "📊 Jumlah Konten",
        ["5", "10", "30"]
    )

    generate = st.button("🔥 Generate Sekarang")

# ===== TONE MAP =====
tone_map = {
    "Santai": "gunakan bahasa santai, gaul, seperti anak muda Indonesia",
    "Formal": "gunakan bahasa profesional dan rapi",
    "Islami": "gunakan bahasa sopan dengan nuansa islami",
    "Hard Selling": "gunakan gaya jualan langsung, persuasif, dan kuat CTA"
}

with col2:
    st.markdown("### 📋 Hasil Konten")

    if generate:
        if not produk or not bisnis:
            st.warning("⚠️ Isi semua field dulu ya")
        else:
            prompt = f"""
            Buat konten untuk:
            Produk: {produk}
            Bisnis: {bisnis}

            Jumlah:
            - {jumlah} caption jualan
            - {jumlah} ide konten TikTok
            - 1 script video pendek

            Gaya:
            {tone_map[tone]}

            Format:
            1. Caption
            2. Ide konten (judul + konsep)
            3. Script video (hook, isi, CTA)

            Gunakan bahasa Indonesia yang menarik dan tidak kaku.
            """

            with st.spinner("⏳ Lagi bikin konten viral..."):
                res = client.chat.completions.create(
                    model="gpt-4.1-mini",
                    messages=[{"role": "user", "content": prompt}]
                )

            output = res.choices[0].message.content

            st.success("✅ Konten siap dipakai!")

            st.text_area("Hasil", output, height=400)

            colA, colB = st.columns(2)

            with colA:
                st.download_button(
                    "⬇️ Download",
                    output,
                    file_name="konten_umkm.txt"
                )

            with colB:
                st.code(output)
