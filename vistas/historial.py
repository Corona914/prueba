import streamlit as st
from datetime import date
from datos import get_historial_data

def mostrar_historial():
    st.markdown('<h2 style="color:#1e293b; margin-bottom:1rem;">Historial de Mediciones</h2>', unsafe_allow_html=True)

    df = get_historial_data()

    # Tarjeta de Filtros
    with st.container():
        st.markdown('<div class="card" style="margin-bottom:1.5rem;">', unsafe_allow_html=True)
        f1, f2, f3, f4 = st.columns([2,2,2,1])
        with f1: fecha_inicio = st.date_input("Fecha Inicio", value=date.today())
        with f2: fecha_fin = st.date_input("Fecha Fin", value=date.today())
        with f3: nivel = st.selectbox("Nivel", ["Todos", "Bueno", "Moderado", "Alto"])
        with f4:
            st.write("")
            buscar = st.button("Buscar", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    if buscar:
        df = df[
            (df["fecha"].dt.date >= fecha_inicio) &
            (df["fecha"].dt.date <= fecha_fin)
        ]

    # Botón exportar
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Exportar CSV", csv, "historial_pm25.csv", "text/csv")

    # Tabla
    st.dataframe(
        df.rename(columns={
            "id": "ID", "fecha": "Fecha", "hora": "Hora",
            "pm25": "PM2.5", "lat": "Lat", "lon": "Lng"
        }),
        use_container_width=True,
        height=400
    )