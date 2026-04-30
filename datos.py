import pandas as pd
import numpy as np

def get_mock_map():
    return pd.DataFrame({
        'lat': np.random.uniform(19.501, 19.506, 20),
        'lon': np.random.uniform(-99.148, -99.142, 20),
        'PM25': np.random.uniform(5, 25, 20)
    })

def get_historial_data():
    return pd.DataFrame({
        "id": range(1000, 1100),
        "fecha": pd.date_range(end=pd.Timestamp.today(), periods=100),
        "hora": pd.date_range(end=pd.Timestamp.today(), periods=100).time,
        "pm25": np.random.uniform(5, 25, 100),
        "lat": np.random.uniform(19.501, 19.506, 100),
        "lon": np.random.uniform(-99.148, -99.142, 100)
    })

def get_chart_data(periodo):
    if periodo == "Hoy":
        fechas = pd.date_range(end=pd.Timestamp.now(), periods=12, freq="H")
    elif periodo == "Esta Semana":
        fechas = pd.date_range(end=pd.Timestamp.now(), periods=7)
    else:
        fechas = pd.date_range(end=pd.Timestamp.now(), periods=30)

    return pd.DataFrame({
        "fecha": fechas,
        "pm25": np.random.uniform(8, 25, len(fechas))
    })