import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="AI Konten UMKM", page_icon="🚀")

st.title("🚀 AI Konten Jualan UMKM 🇮🇩")
st.caption("Bikin konten jualan otomatis dalam hitungan detik")

# INPUT
produk = st.text_input("🛍️ Nama Produk")
bisnis = st.text_input("🏪 Jenis Bisnis")

tone = st.selectbox(
    "🎯 Pilih Tone Konten",
    ["Santai", "Formal", "Islami", "Hard Selling"]
)

jumlah = st.selectbox(
    "📊 Jumlah Konten",
    ["5", "10", "30"]
)

tone_map = {
    "Santai": "gunakan bahasa santai, gaul, seperti anak muda Indonesia",
    "Formal": "gunakan bahasa profesional dan rapi",
    "Islami": "gunakan bahasa sopan dengan nuansa islami (boleh selipkan kata seperti insyaAllah, barokah)",
    "Hard Selling": "gunakan gaya jualan langsung, persuasif, dan kuat CTA"
}

if st.button("🔥 Generate Konten"):

    if not produk or not bisnis:
        st.warning("Isi dulu produk & bisnis ya")
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

        with st.spinner("Lagi bikin konten... ⏳"):
            res = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[{"role": "user", "content": prompt}]
            )

        output = res.choices[0].message.content

        st.success("Konten berhasil dibuat! 🎉")

        st.text_area("📋 Hasil Konten", output, height=400)

        st.download_button(
            label="⬇️ Download Hasil",
            data=output,
            file_name="konten_umkm.txt"
        )
