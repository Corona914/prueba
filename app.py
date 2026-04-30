import streamlit as st

# Importamos las funciones de nuestras vistas
from vistas.dashboard import mostrar_dashboard
from vistas.historial import mostrar_historial
from vistas.graficas import mostrar_graficas

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Red Sea - Monitoreo PM2.5", layout="wide")

# --- ESTADO DE NAVEGACIÓN ---
if 'vista_actual' not in st.session_state:
    st.session_state.vista_actual = 'Dashboard'

def cambiar_vista(vista):
    st.session_state.vista_actual = vista

# --- CSS INTEGRADO ---
st.markdown("""
<style>
/* --- BASE --- */
.stApp { background-color: #f1f5f9; font-family: 'Inter', sans-serif; }
header {visibility: hidden;}

/* --- SIDEBAR --- */
[data-testid="stSidebar"] { background: linear-gradient(180deg, #0f172a, #020617); border-right: 1px solid #1e293b; }
[data-testid="stSidebar"] h1 { color: #60a5fa; font-weight: 700; }
[data-testid="stSidebar"] .stButton button {
    width: 100%; background: transparent; color: #cbd5f5; border: none;
    text-align: left; padding: 0.7rem 1rem; border-radius: 8px; transition: 0.2s;
}
[data-testid="stSidebar"] .stButton button:hover { background: #1e293b; color: white; }
[data-testid="stSidebar"] .stButton button:focus { background: linear-gradient(90deg, #2563eb, #3b82f6); color: white; }

/* --- CARDS --- */
.card {
    background: white; border-radius: 14px; padding: 1.4rem;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05); transition: 0.2s ease;
}
.card:hover { transform: translateY(-2px); box-shadow: 0 6px 18px rgba(0,0,0,0.08); }
.border-blue { border-left: 5px solid #3b82f6; }
.border-green { border-left: 5px solid #22c55e; }
.border-yellow { border-left: 5px solid #facc15; }

/* --- HEADER --- */
.header {
    display: flex; justify-content: space-between; align-items: center;
    margin-bottom: 1.5rem; background: white; padding: 1rem 1.5rem;
    border-radius: 12px; box-shadow: 0 2px 10px rgba(0,0,0,0.03);
}
.header h3 { margin: 0; color: #1e293b; font-size: 1.25rem; font-weight: 600;}
.status { color: #16a34a; font-weight: 500; font-size: 0.9rem; }

/* --- TABLA MINI --- */
.table-mini { font-size: 0.9rem; width: 100%; margin-top: 1rem; border-collapse: collapse; }
.table-mini td { padding: 0.5rem 0; border-bottom: 1px solid #f1f5f9;}

/* --- BOTONES NATIVOS --- */
.stDownloadButton button { background: #16a34a !important; color: white !important; border-radius: 8px !important; }
.stRadio > div { background: #e2e8f0; padding: 4px; border-radius: 10px; }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.title("RED SEA")
    st.button("📊 Dashboard", on_click=cambiar_vista, args=('Dashboard',))
    st.button("📋 Historial", on_click=cambiar_vista, args=('Historial',))
    st.button("📈 Gráficas", on_click=cambiar_vista, args=('Graficas',))

# --- ROUTER (Controlador de Vistas) ---
if st.session_state.vista_actual == 'Dashboard':
    mostrar_dashboard()
elif st.session_state.vista_actual == 'Historial':
    mostrar_historial()
elif st.session_state.vista_actual == 'Graficas':
    mostrar_graficas()