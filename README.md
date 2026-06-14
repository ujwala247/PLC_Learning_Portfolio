# Week 3 — Project 1 Complete + Allen-Bradley + Project 2 Start

## Tools Used
Siemens TIA Portal V17, WinCC Runtime Advanced,
PLCSIM, RSLogix Micro Starter, CODESYS V3.5

---

## Days 15-17 — Project 1: Conveyor Belt Automation ✅

### System Overview
2-Zone conveyor belt with object sorting,
counting and full HMI control.

### Architecture
- Motor_Control FB1 — latch + fault detection
- Safety_Logic FB2 — E-stop + gate + reset
- Analog_Scaling FC1 — 4-20mA belt speed
- Alarm_Handler FC2 — alarm word packing
- Counter_Logic FC3 — good/reject counting
- SCL State Machine — 6-state sequence controller

### HMI Screens (4 screens)
- Main: START/STOP/RESET + motor status + counters
- Counter: Good/Reject/Total with reset
- Trend: Belt speed + count over time
- Alarms: 5 configured alarms with timestamps

### Key Features
- Professional modular FB structure
- Safety interlock with mandatory reset
- VFD speed control via analog output
- Alarm word bit-packing technique
- State machine: IDLE→STARTING→RUNNING→SORTING→STOPPING

### Simulation Test Results
- Motor latch + fault detection ✅
- Safety reset logic ✅
- Zone 2 interlock (only starts when Zone 1 running) ✅
- Object detection and sorting ✅
- Counter accumulation ✅
- All 5 alarms triggering correctly ✅

---

## Day 18 — Allen-Bradley RSLogix

### What I Built
Motor Start/Stop + TON Timer + CTU Counter
in RSLogix Micro Starter Lite

### Key Differences vs Siemens
| Feature | Siemens | Allen-Bradley |
|---|---|---|
| Addressing | %I0.0, %Q0.0 | I:0/0, O:0/0 |
| NO contact | —[ ]— | XIC |
| NC contact | —[/]— | XNO |
| Output coil | —( )— | OTE |
| Timer file | TON block | T4:0 |
| Timer done | .Q | T4:0/DN |
| Counter file | CTU block | C5:0 |

---

## Day 19 — VFD Control + Energy Monitoring Project Start

### VFD Speed Control Added to Conveyor Project
- Speed setpoint (0-100%) → analog output (0-27648)
- Actual RPM display on HMI
- Belt speed bar with Green/Yellow/Red zones

### Energy Monitoring Project 2 — Structure Created
- FB1_Energy_Reader — reads one zone meter
- 3 instance DBs: Zone1/2/3_Reader_DB
- Config_DB with thresholds
- Zone1/2/3_DB storing kW and kWh
- Alarm_DB for threshold alerts
- OB1 compiled clean ✅ (errors:0, warnings:9)

---

## Week 3 Summary
- New skills: Professional project structure,
  State machine programming, AB basics, VFD control
