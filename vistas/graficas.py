import streamlit as st
from datos import get_chart_data

def mostrar_graficas():
    st.markdown('<h2 style="color:#1e293b; margin-bottom:1rem;">Análisis y Tendencias</h2>', unsafe_allow_html=True)

    periodo = st.radio(
        "Selecciona periodo",
        ["Hoy", "Esta Semana", "Este Mes"],
        horizontal=True
    )

    st.markdown('<br>', unsafe_allow_html=True)

    df_chart = get_chart_data(periodo)
    df_chart["Límite OMS"] = 15

    st.line_chart(
        df_chart.set_index("fecha"),
        height=350
    )