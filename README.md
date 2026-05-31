# Week 2 — HMI, Communication & Analog I/O

## Tools Used
Siemens TIA Portal V17, WinCC Runtime Advanced, PLCSIM, CODESYS V3.5

---

## Day 8 — WinCC HMI Design
- START/STOP buttons with SetBit/ResetBit events
- Motor 1 and Motor 2 status indicators
- Live object counter display
- Alarm screen with navigation
- Discrete alarm configuration

## Day 9 — PROFINET + Modbus TCP
- PROFINET network view: PLC + HMI + Remote I/O configured
- IP addressing: PLC=192.168.0.1, HMI=192.168.0.2
- Modbus TCP register concept (FC03 Holding registers)
- MB_CLIENT block parameters studied
- OPC-UA server enabled for Python integration
- Modbus port 502 — standard for all devices

## Day 10 — Analog I/O + 4-20mA Scaling
- 4mA = 0%, 20mA = 100%, 0mA = wire break fault
- Siemens raw count: 0 to 27648
- Custom scaling FC in SCL with wire break detection
- NORM_X and SCALE_X blocks used
- Temperature bar graph on HMI (Green/Yellow/Red zones)
- Simulation tested: 6912 raw = 50°C ✅

## Day 11 — PID Control using PID_Compact Block
- PID concepts: SP (Setpoint), PV (Process Value), CV (Control Output)
- P term: reacts to current error
- I term: eliminates steady state offset
- D term: reduces overshoot
- PID_Compact block configured in TIA Portal
- Input: Sensor_DB.Temperature (scaled analog value)
- Output: Sensor_DB.Heater_Output (0-100%)
- Mode 4 = Automatic operation
- Simulation tested: temperature approaching 80°C → output reduced ✅
- Process value limits: 0-200°C
- Output limits: 0-100%

## Day 12 — Safety PLC + SIL Levels
- SIL 1: basic E-stop, conveyor machines
- SIL 2: chemical/oil/gas plants (JSW Steel level)
- SIL 3: hazardous/nuclear processes
- Siemens F-CPU: dedicated fail-safe CPU
- F-OB1: safety program block, faster scan time
- Safety contacts wired NC — wire break = safe state
- Dual channel wiring for higher SIL levels
- Built Safety_Logic FC in TIA Portal:
  - E-stop + gate interlock logic
  - Manual reset required after any safety trip
  - Enable_Output only TRUE when all safe + reset done
- Simulation tested: E-stop release → output stayed FALSE until reset ✅

## Day 13 — Schneider EcoStruxure + Multi-Brand PLC

### Schneider PLC Family
- Modicon M221 → small machines
- Modicon M340 → medium process plants (JSW Steel level)
- Modicon M580 → large plants with redundancy

### Key Comparisons
| Feature | Siemens | Schneider |
|---|---|---|
| Software | TIA Portal | Control Expert |
| Protocol | PROFINET | Modbus TCP |
| HMI | WinCC | Vijeo Designer |
| DB concept | Data Block | DDT |

### Allen-Bradley Overview
- Studio 5000 software
- EtherNet/IP protocol
- Tag-based (no addresses) vs Siemens address-based
- RSLogix Micro Starter downloaded

### Multi-Brand Summary
| Brand | Software | Protocol |
|---|---|---|
| Siemens | TIA Portal | PROFINET |
| Schneider | Control Expert | Modbus TCP |
| Allen-Bradley | Studio 5000 | EtherNet/IP |
| Mitsubishi | GX Works3 | CC-Link |

## Day 14 — FBD Language + Week 2 Revision

### FBD (Function Block Diagram)
- Graphical language — blocks connected with signal lines
- AND, OR, NOT gates connected visually
- Same logic as Ladder but different representation
- Built Motor control program using FBD in CODESYS
- TON timer connected in FBD style

### Week 2 Revision Score
- Self-test: 16/20 correct
- Strong areas: HMI, Analog I/O, PID, Safety
- Areas to review: SetBit event, Modbus port 502,
  P term definition, OPC-UA purpose

---

## Week 2 Summary
- Tools used: TIA Portal V17, WinCC, CODESYS, RSLogix
- Concepts mastered: HMI design, protocols, analog
  scaling, PID control, safety logic, multi-brand awareness

## Concepts Mastered
- HMI tag binding and events
- PROFINET vs Modbus vs PROFIBUS differences
- Analog signal scaling formula
- Wire break fault detection logic
- WinCC alarm configuration
- PID control closed loop theory
- SIL levels and safety PLC architecture
- Multi-brand PLC comparison
- FBD programming language
