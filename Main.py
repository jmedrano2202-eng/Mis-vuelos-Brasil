import streamlit as st

# Configuración estética
st.set_page_config(page_title="Consiguelo - Tasas Fijas", page_icon="✈️")

# Estilo personalizado simple
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #007bff; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Consiguelo: Buscador de Oportunidades")
st.subheader("Brasil Nacional e Internacional")

# Base de conocimiento de Tasas Fijas
TASAS = {
    "Nacional Brasil (GOL via AAdvantage)": 7500,
    "Brasil -> USA (LATAM Pass Partners)": 60000,
    "Brasil -> Europa (Iberia/British - Avios)": 21250,
    "Brasil -> Sudamérica (AAdvantage/GOL)": 10000
}

col1, col2 = st.columns(2)

with col1:
    ruta = st.selectbox("Selecciona la Región", list(TASAS.keys()))
    precio_dinero = st.number_input("Precio actual en Reales (R$)", min_value=0, value=500)

with col2:
    tasa_fija = TASAS[ruta]
    st.metric(label="Costo en Millas (Fijo)", value=f"{tasa_fija:,}")

# Lógica de Inteligencia de Viaje
# Valor de referencia: 1000 millas = R$ 70 (promedio alto)
valor_millas_reales = (tasa_fija / 1000) * 70 

st.divider()

if precio_dinero > valor_millas_reales:
    st.success(f"✅ ¡USA LA TASA FIJA! El vuelo en dinero (R${precio_dinero}) es más caro que el valor de tus millas (~R${valor_millas_reales:.2f}).")
else:
    st.warning(f"❌ PAGA EN DINERO. Las millas valen más que el precio actual del ticket.")

# Sección de ayuda para conseguir la disponibilidad
with st.expander("¿Cómo reservo estas tasas?"):
    if "AAdvantage" in ruta:
        st.write("1. Entra a aa.com\n2. Marca 'Redeem Miles'.\n3. Busca vuelos operados por GOL.")
    elif "Iberia" in ruta:
        st.write("1. Usa el buscador de Avios de Iberia Plus.\n2. Busca fechas 'Off-peak' para la tasa de 21,250.")
    else:
        st.write("Consulta el portal de socios del programa correspondiente.")

st.info("Próxima actualización: Conexión en tiempo real con APIs de disponibilidad.")
