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
