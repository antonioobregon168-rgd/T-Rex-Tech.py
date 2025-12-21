import streamlit as st
import smtplib
from email.message import EmailMessage

st.set_page_config(
    page_title="T-Rex Tech",
    page_icon="🦖"
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

st.markdown("---")
st.header("📩 Solicitar reparación")

with st.form("contacto"):
    nombre = st.text_input("Nombre")
    modelo = st.text_input("Modelo del celular")
    problema = st.text_area("Describe el problema")
    enviar = st.form_submit_button("Enviar solicitud")

if enviar:
    if nombre and modelo and problema:
        try:
            email = EmailMessage()
            email["From"] = st.secrets["EMAIL"]
            email["To"] = st.secrets["EMAIL"]
            email["Subject"] = "📱 Nueva solicitud - T-Rex Tech"

            email.set_content(f"""
Nombre: {nombre}
Modelo: {modelo}
Problema:
{problema}
            """)

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(
                    st.secrets["EMAIL"],
                    st.secrets["EMAIL_PASSWORD"]
                )
                smtp.send_message(email)

            st.success("✅ Solicitud enviada correctamente")
        except Exception as e:
            st.error("❌ Error al enviar el mensaje")
    else:
        st.warning("⚠️ Completa todos los campos")

st.markdown("---")
st.link_button(
    "📲 Enviar WhatsApp",
    "https://wa.me/524641397751"
)

st.caption("Servicio local • Atención por mensaje")
