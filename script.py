import requests
import sqlite3
from datetime import datetime

# Coordenadas de São Paulo
lat = -23.5505
lon = -46.6333

url = f"https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={lat}&lon={lon}"
headers = {
    "User-Agent": "anon-script"
}

conn = sqlite3.connect("clima_sp.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clima_sp (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data_hora_coleta TEXT,
    temperatura REAL,
    umidade REAL,
    pressao REAL
)
""")


resposta = requests.get(url, headers=headers)

if resposta.status_code == 200:
    dados = resposta.json()
    tempo = dados['properties']['timeseries'][0]['data']['instant']['details']
    
  
    temperatura = tempo['air_temperature']
    umidade = tempo.get('relative_humidity', None)
    pressao = tempo['air_pressure_at_sea_level']
    data_coleta = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    cursor.execute("""
        INSERT INTO clima_sp (data_hora_coleta, temperatura, umidade, pressao)
        VALUES (?, ?, ?, ?)
    """, (data_coleta, temperatura, umidade, pressao))
    
    conn.commit()
    print("✅ Dados inseridos com sucesso!")
else:
    print(f"❌ Erro ao acessar API: {resposta.status_code}")

conn.close()
