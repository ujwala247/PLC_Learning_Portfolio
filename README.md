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

## Concepts Mastered
- HMI tag binding and events
- PROFINET vs Modbus vs PROFIBUS differences
- Analog signal scaling formula
- Wire break fault detection logic
- WinCC alarm configuration
