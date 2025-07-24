import streamlit as st

st.set_page_config(page_title="SEO Text Optimizer", layout="centered")

st.title("🚀 SEO Text Optimizer")
st.write("Optimiza el texto que va debajo del H1 para mejorar tu posicionamiento.")

# Entrada de keyword
keyword = st.text_input("🔍 Ingresa la palabra clave")

# Ingreso manual de textos de la competencia
st.subheader("📎 Pega los textos de la competencia que aparecen debajo del H1")
competidor_1 = st.text_area("Competidor 1")
competidor_2 = st.text_area("Competidor 2")
competidor_3 = st.text_area("Competidor 3")

# Subida de brochure
st.subheader("📂 Sube el brochure de tu carrera (formato .txt)")
brochure = st.file_uploader("Sube tu archivo", type=["txt"])
brochure_text = ""
if brochure is not None:
    brochure_text = brochure.read().decode("utf-8")

# Botón para generar
if st.button("✨ Generar propuestas"):
    with st.spinner("Generando variantes con IA..."):
        from openai import OpenAI
        import os

        client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

        prompt = f"""
        Quiero optimizar el texto que va debajo del H1 para posicionar la palabra clave "{keyword}".
        Este es el contenido del producto o servicio (brochure):
        {brochure_text}

        Este es el contenido que aparece en los competidores:
        COMPETIDOR 1: {competidor_1}
        COMPETIDOR 2: {competidor_2}
        COMPETIDOR 3: {competidor_3}

        Redáctame 3 versiones claras, concisas, orientadas a SEO informativo, que podrían usarse como párrafo de entrada debajo del H1.
        """
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        st.success("✅ Aquí tienes las 3 versiones:")
        st.write(response.choices[0].message.content)
