# ═══ ENERGY MONITORING PYTHON SCRIPT ═══
# File: energy_monitor.py
# Author: Ujwala Venuturla
# Purpose: Read PLC data, store in DB, send alerts


from opcua import Client
import sqlite3
from datetime import datetime
import schedule
import time


# ── Configuration ──
PLC_IP    = "192.168.0.1"
DB_FILE   = "energy_data.db"
THRESHOLD = 90.0  # Total kW alert threshold


# ── Database setup ──
def setup_database():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS energy_log (
            id        INTEGER PRIMARY KEY,
            timestamp TEXT,
            zone1_kw  REAL,
            zone2_kw  REAL,
            zone3_kw  REAL,
            total_kw  REAL,
            zone1_kwh REAL
        )
    ''')
    conn.commit()
    conn.close()


# ── Read PLC data via OPC-UA ──
def read_plc():
    try:
        client = Client(f"opc.tcp://{PLC_IP}:4840")
        client.connect()


        z1_kw  = client.get_node(
            "ns=3;s=Zone1_Reader_DB.Active_Power").get_value()
        z2_kw  = client.get_node(
            "ns=3;s=Zone2_Reader_DB.Active_Power").get_value()
        z3_kw  = client.get_node(
            "ns=3;s=Zone3_Reader_DB.Active_Power").get_value()
        total  = client.get_node(
            "ns=3;s=Config_DB.Total_Power").get_value()
        z1_kwh = client.get_node(
            "ns=3;s=Zone1_Reader_DB.Energy_kWh").get_value()


        client.disconnect()


        # Store in database
        store_data(z1_kw, z2_kw, z3_kw, total, z1_kwh)


        # Check threshold
        if total > THRESHOLD:
            send_alert(total)


        print(f"[{datetime.now()}] Total: {total:.1f} kW")


    except Exception as e:
        print(f"PLC read error: {e}")


# ── Store data ──
def store_data(z1, z2, z3, total, z1_kwh):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO energy_log
        (timestamp, zone1_kw, zone2_kw, zone3_kw,
         total_kw, zone1_kwh)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (datetime.now().isoformat(), z1, z2, z3,
          total, z1_kwh))
    conn.commit()
    conn.close()


# ── Send alert ──
def send_alert(total_kw):
    print(f"⚠️ ALERT: High power demand {total_kw:.1f} kW!")
    # Add WhatsApp/email here — same as JSW project!


# ── Main ──
setup_database()
schedule.every(1).minutes.do(read_plc)


print("Energy Monitor started...")
while True:
    schedule.run_pending()
    time.sleep(1)