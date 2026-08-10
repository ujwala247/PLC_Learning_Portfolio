# Project 3 — Batch Process Automation System

## Overview
S88-compliant batch automation system for a chemical
mixing process with recipe management, phase-based
control architecture, and full WinCC HMI.

This is the most advanced project in the portfolio —
demonstrating ISA-88 batch standard implementation,
modular phase FB design, recipe management via UDT,
and multi-screen HMI with real-time monitoring.

---

## System Description

### Process Flow
IDLE → FILL → MIX → HEAT → HOLD → DRAIN → DONE → IDLE
### Two Selectable Recipes

| Parameter | Recipe 1 Standard | Recipe 2 Concentrated |
|---|---|---|
| Fill Level | 80% | 90% |
| Mix Time | 5 minutes | 8 minutes |
| Heat Temp | 60°C | 75°C |
| Hold Time | 2 minutes | 3 minutes |

---

## Architecture — S88 Phase FB Design

### Program Blocks

| Block | Type | Language | Purpose |
|---|---|---|---|
| Fill_Phase | FB1 | SCL | Valve control + level detection |
| Mix_Phase | FB2 | SCL | Agitator + configurable timer |
| Heat_Phase | FB3 | SCL | Bang-bang temperature control |
| Drain_Phase | FB4 | SCL | Drain valve + timeout fault |
| Recipe_Manager | FC1 | SCL | Recipe parameter switching |
| Analog_Scaling | FC2 | SCL | 4-20mA temperature scaling |
| Alarm_Handler | FC3 | SCL | Alarm word bit packing |
| Main | OB1 | SCL | Master batch sequence |

### Data Blocks

| Block | Purpose |
|---|---|
| Recipe1_DB | Standard mix parameters (Recipe_UDT) |
| Recipe2_DB | Concentrated mix parameters (Recipe_UDT) |
| Batch_DB | Master status + phase tracking |
| Fill_DB | Fill_Phase instance data |
| Mix_DB | Mix_Phase instance data |
| Heat_DB | Heat_Phase instance data |
| Drain_DB | Drain_Phase instance data |

---

## Key Implementation Details

### Recipe_UDT — User Defined Type
```pascal
TYPE Recipe_UDT
    Fill_Level  : Real;   // Target fill %
    Mix_Time    : Time;   // Mixing duration
    Heat_Temp   : Real;   // Target temperature °C
    Hold_Time   : Time;   // Hold at temperature
    Recipe_Name : String; // Recipe description
END_TYPE
```

### Phase FB State Machine Pattern
Each phase uses a consistent 4-state CASE machine:
- State 0 = IDLE (waiting for Execute)
- State 1 = RUNNING (active processing)
- State 2 = DONE (phase complete)
- State 3 = FAULT (abort/timeout)

### Master OB1 Sequence
State 0 → IDLE → waits for Start_Batch
State 1 → FILL → calls Fill_Phase FB
State 2 → MIX → calls Mix_Phase FB
State 3 → HEAT → calls Heat_Phase FB
State 4 → DRAIN → calls Drain_Phase FB
State 5 → DONE → Batch_Count++ → back to IDLE

### Temperature Control
Bang-bang (ON/OFF) control:
- Below (Target - 2°C) → Heater ON (100%)
- Above Target → Heater OFF (0%)
- Tolerance band: ±2°C

### Fault Handling
- Any phase fault → Batch_State = 0 (safe IDLE)
- Fault_Code recorded: 1=Fill, 2=Mix, 3=Heat, 4=Drain
- Manual Fault_Reset required before restart
- Drain timeout fault after 5 minutes

---

## I/O List

### Digital Inputs
| Address | Tag | Description |
|---|---|---|
| I0.0 | Start_Batch | Start batch command |
| I0.1 | Stop_Batch | Emergency abort |
| I0.2 | Level_Low | Tank low sensor |
| I0.3 | Level_High | Tank high sensor |
| I0.4 | Drain_Empty | Tank empty sensor |
| I0.5 | Agitator_FB | Agitator feedback |
| I0.6 | Fault_Reset | Manual fault reset |
| I0.7 | Recipe_Select | 0=Recipe1, 1=Recipe2 |

### Digital Outputs
| Address | Tag | Description |
|---|---|---|
| Q0.0 | Valve_A | Ingredient A valve |
| Q0.1 | Valve_B | Ingredient B valve |
| Q0.2 | Agitator | Mixing motor |
| Q0.3 | Heater | Tank heater |
| Q0.4 | Drain_Valve | Product drain |
| Q0.5 | Batch_Complete | Done indicator |
| Q0.6 | Fault_Light | Fault alarm light |

### Analog I/O
| Address | Tag | Description |
|---|---|---|
| IW64 | Temp_Raw | Temperature 4-20mA input |
| QW64 | Heater_Output | Heater power 0-100% |

---

## HMI — 4 Screen Design

### Screen 1 — Batch Overview (Main)
- START / STOP / FAULT RESET buttons
- Live phase name display (FILLING/MIXING/HEATING etc.)
- 4 phase status indicators with 3-state animation:
  - Grey ⏳ = Waiting
  - Blue 🔄 = Active (flashing)
  - Green ✅ = Complete
- Live temperature display + target
- Heater power bar (Green/Yellow/Red)
- Fault display with fault code
- Batch counter (total batches completed)
- Navigation: Recipe / Trends / Alarms

### Screen 2 — Recipe Selection
- Recipe 1 panel — all parameters displayed
- Recipe 2 panel — all parameters displayed
- Active recipe highlighted Green
- One-click recipe switching
- Recipe_Select tag: FALSE=Recipe1, TRUE=Recipe2

### Screen 3 — Temperature Trend
- Live temperature (Red line)
- Target setpoint reference (Blue dashed)
- Heater output % (Orange line)
- 10-minute time window
- Shows bang-bang control behavior visually

### Screen 4 — Alarm Screen
- Alarm view with timestamp logging
- 4 configured discrete alarms:
  - Fill Phase Fault (Bit 0)
  - Mix Phase Fault (Bit 1)
  - Heat Phase Fault (Bit 2)
  - Drain Timeout Fault (Bit 3)
- Alarm word bit-packing technique

---

## Simulation Test Results

| Test | Action | Result |
|---|---|---|
| Recipe 1 batch | Start → force inputs | FILL→MIX→HEAT→DRAIN→DONE ✅ |
| Recipe 2 batch | Select R2 → Start | Heat target = 75°C ✅ |
| Fault injection | Abort mid-batch | Safe state + fault code ✅ |
| Fault reset | Press reset button | Batch ready to restart ✅ |
| Drain timeout | Block Drain_Empty | Fault after 5 min ✅ |
| Batch counter | Complete 3 batches | Count = 3 ✅ |
| Phase animations | Run full batch | Grey→Blue→Green per phase ✅ |

---

## S88 Standard Applied

| S88 Concept | Implementation |
|---|---|
| Phase | FB1-FB4 (Fill/Mix/Heat/Drain) |
| Recipe | Recipe_UDT data type |
| Recipe instance | Recipe1_DB + Recipe2_DB |
| Batch status | Batch_DB tracking all state |
| Phase states | 0=Idle, 1=Running, 2=Done, 3=Fault |
| Unit | Mixing vessel (single unit process) |
| Equipment module | Agitator, Heater, Valves |

---

## Tools Used
- Siemens TIA Portal V17
- WinCC Runtime Advanced
- PLCSIM (simulation)
- SCL (Structured Text) — all logic blocks

## Connection to Real Experience
This project formalizes the batch process concepts
seen in JSW Steel production environments, applying
ISA-88 standard architecture to a simulated mixing
process — directly applicable to pharma, food,
chemical and process industry PLC roles.

---
