import streamlit as st

st.set_page_config(
    page_title="T-Rex Tech",
    page_icon="🦖",
    layout="centered"
)

st.title("🦖 T-Rex Tech")
st.subheader("Reparación de celulares")

st.markdown("""
### 🛠️ Servicios
- Cambio de pantalla  
- Cambio de batería  
- Centro de carga  
- Limpieza y diagnóstico  
""")

st.markdown("### 📞 Contacto")

st.link_button(
    "Enviar WhatsApp",
    "https://wa.me/524641397751"
)

st.caption("Servicio local • Atención por mensaje")
