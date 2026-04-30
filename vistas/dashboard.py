import streamlit as st
from datos import get_mock_map

def mostrar_dashboard():
    # Header estilizado
    st.markdown("""
    <div class="header">
        <h3>Panel de Visualización de Datos</h3>
        <div>
            <span class="status">● Nodo Móvil Conectado</span>
            &nbsp;&nbsp;|&nbsp;&nbsp;
            <span style="color:#64748b;">Ciclopista IPN</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Tarjetas KPI
    c1, c2, c3 = st.columns(3)
    c1.markdown("""
    <div class="card border-blue">
        <p style="color:#64748b; margin:0; font-weight:500;">Concentración Actual PM2.5</p>
        <h2 style="margin-top:0.5rem; color:#1e293b;">12.5 <span style="font-size:0.9rem; color:#64748b;">µg/m³</span></h2>
    </div>
    """, unsafe_allow_html=True)

    c2.markdown("""
    <div class="card border-green">
        <p style="color:#64748b; margin:0; font-weight:500;">Promedio del Recorrido</p>
        <h2 style="margin-top:0.5rem; color:#1e293b;">10.2 <span style="font-size:0.9rem; color:#64748b;">µg/m³</span></h2>
    </div>
    """, unsafe_allow_html=True)

    c3.markdown("""
    <div class="card border-yellow">
        <p style="color:#64748b; margin:0; font-weight:500;">Estado de la Calidad del Aire</p>
        <h2 style="margin-top:0.5rem; color:#ca8a04;">Moderada</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Sección Mapa e Historial Rápido
    col_mapa, col_tabla = st.columns([2,1])

    with col_mapa:
        st.markdown("""
        <div style="background: white; border-radius: 14px 14px 0 0; padding: 1.2rem 1.4rem; border-bottom: 1px solid #f1f5f9; display:flex; justify-content:space-between; align-items:center;">
            <b style="color:#1e293b; font-size:1.1rem;">Ruta Ciclopista Zacatenco</b>
            <span style="color:#2563eb; font-size:0.9rem; cursor:pointer; font-weight:500;">Ver pantalla completa</span>
        </div>
        """, unsafe_allow_html=True)
        st.map(get_mock_map(), height=300)

    with col_tabla:
        st.markdown("""
        <div class="card" style="height: 100%;">
            <b style="color:#1e293b; font-size:1.1rem;">Últimos Registros</b>
            <table class="table-mini">
                <tr><td style="color:#64748b;">14:25:00</td><td style="color:#ca8a04; text-align:right; font-weight:bold;">12.5</td></tr>
                <tr><td style="color:#64748b;">14:24:50</td><td style="color:#16a34a; text-align:right; font-weight:bold;">9.8</td></tr>
                <tr><td style="color:#64748b;">14:24:40</td><td style="color:#16a34a; text-align:right; font-weight:bold;">8.5</td></tr>
                <tr style="border-bottom: none;"><td style="color:#64748b;">14:24:30</td><td style="color:#16a34a; text-align:right; font-weight:bold;">9.1</td></tr>
            </table>
            <br>
            <div style="text-align:center; background:#f8fafc; padding:0.6rem; border-radius:8px; color:#475569; font-weight:500; cursor:pointer; transition:0.2s;" onmouseover="this.style.background='#f1f5f9'" onmouseout="this.style.background='#f8fafc'">
                Ver Historial Completo
            </div>
        </div>
        """, unsafe_allow_html=True)