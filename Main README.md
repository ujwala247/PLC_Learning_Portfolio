# Project 2 — Energy Monitoring System

## Overview
3-zone plant energy monitoring system with real-time
kW/kWh tracking, threshold alerts, and shift-based
consumption reporting. Directly mirrors EMS work at
JSW Steel.

## Architecture
- FB1_Energy_Reader — reusable FB, one instance per zone
- 3 instance DBs: Zone1/2/3_Reader_DB
- Config_DB — thresholds + shift tracking
- Alarm_DB — bit-packed alarm word
- 4-screen WinCC HMI: Main, Trends, Alarms, Counters

## Key Features
- Live kW calculation from scaled V/I/PF
- kWh accumulation (kW × 1/3600 per second)
- Per-zone + total threshold alerts
- Shift consumption = current kWh - shift start kWh
- Color-coded power bars (Green/Yellow/Red)

## Python + OPC-UA Integration
Full Python script written using opcua library:
- Connects to PLC OPC-UA server
- Reads live zone/total power values
- Logs to SQLite database every interval
- Threshold-based alert triggering (WhatsApp/email ready)

**Note:** TIA Portal trial license does not include OPC-UA
server activation. Tested and confirmed across PLCSIM,
PLCSIM Advanced, and CODESYS — this is a genuine licensing
requirement, not a configuration error. Python code is
complete and production-ready for licensed/physical hardware.

## Simulation Results
- Zone 1& 2 & 3: tested with forced analog values ✅
- Shift consumption tracking working ✅
- All 3 zones displaying simultaneously on HMI ✅

## Tools Used
TIA Portal V17, WinCC, PLCSIM, PLCSIM Advanced,
Python (opcua, sqlite3), UAExpert
