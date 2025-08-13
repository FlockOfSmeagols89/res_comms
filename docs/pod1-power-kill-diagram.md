
# Pod‑1 Power “Kill” Diagram — Shunt‑Trip + UV/OV Relays (One‑Pager)
*Concept wiring for clean power + fast, redundant disconnects.*  
**License:** Docs CC BY‑SA 4.0

> ⚠️ **Safety first:** Mains work must be done by a qualified electrician. This is a **concept** diagram. Adapt ratings to your system (120/240 VAC split‑phase in the U.S. is assumed). Use listed components and follow NEC/local code.

---

## 1) One‑line power path (topology)

```
Utility Service
   │
[Type‑1 SPD @ Service Entrance]  ← electrician
   │
[Isolation Transformer (kVA)]
   │
[EMP/RFI Power Entry Filter]
   │
[Type‑2 SPD @ Subpanel / Pod Input]
   │
[Online UPS (double‑conversion)]
   │
[Type‑3 SPD @ Rack] ────> AC Outlets (only for gear that truly needs AC)
   │
[DC Charger] ──> LiFePO₄ Battery ──> 12/24 V DC Bus ──> Radios, Pi/mini‑PC (preferred loads)
```

---

## 2) Control logic (ASCII schematic)

**Legend:** `──` wires, `[ ]` devices, `( )` coils/contacts, `NO` normally‑open, `NC` normally‑closed.

```
               ┌───────────────────────────────────────────────────────────────┐
               │                    CONTROL POWER (Low Voltage)               │
               │   [24 VDC PSU]  (fused +)─────────────┐                      │
               │                                        ├───────┐             │
               │                                   [E‑STOP]     │             │
               │                                (NC, mushroom)  │             │
               │                                        │       │             │
               │                             ┌──────────┘       │             │
               │                             │                  │             │
               │   [UV/OV RELAY #1]         [UV/OV RELAY #2]    │             │
               │   (INPUT monitor)          (OUTPUT monitor)    │             │
               │    Alarm NO ─┐             Alarm NO ─┐         │             │
               │              └───┐                   └───┐     │             │
               │                  │                       │     │             │
               │         (Shunt‑Trip Coil)          (Contactor Coil)          │
               │           [INPUT BREAKER]            [OUTPUT CONTACTOR]      │
               │                  │                       │                   │
               └──────────────────┴───────────────────────┴───────────────────┘

POWER PATH (simplified):
  Grid → INPUT BREAKER (with shunt‑trip) → Iso Xfmr → EMP/RFI Filter → UPS → OUTPUT CONTACTOR → Loads
```

**Behavior:**  
- **E‑STOP** opens the low‑voltage loop → drops both coils **immediately** (input shunt‑trip opens; output contactor drops).  
- **UV/OV #1 trip** (bad grid): energizes **shunt‑trip coil** → opens **INPUT BREAKER** (latched open; requires manual reset).  
- **UV/OV #2 trip** (bad UPS output): de‑energizes **OUTPUT CONTACTOR** (fails safe → opens).  
- You can wire **either relay** to also drop the other side for maximum safety; shown above as independent to avoid nuisance total blackouts.

> **Why two relays?** Independent sensing upstream and downstream catches both dirty grid **and** UPS/inverter faults. A shunt‑trip is latching (stays open), while a contactor is non‑latching (re‑closes when safe).

---

## 3) Suggested setpoints (starting values — tune with your electrician)

- **UV/OV #1 (Input / Service side):**  
  - Under‑V: < 90 VAC (L‑N), Over‑V: > 135 VAC (L‑N), trip delay 0.1–0.5 s  
  - Frequency window (if supported): 57–63 Hz
- **UV/OV #2 (UPS Output):**  
  - Under‑V: < 100 VAC, Over‑V: > 130 VAC, trip delay 0.1–0.5 s

*Add brownout hysteresis so small dips don’t chatter the contactor.*

---

## 4) Parts guidance (examples — match coil voltages!)

- **Shunt‑Trip Breaker:** Main/input breaker with shunt‑trip accessory (coil often 24 VDC or 120 VAC).  
- **Output Contactor (latching preferred):** 2‑pole contactor sized for UPS output; **24 VDC coil** recommended. Add arc suppressor on coil.  
- **UV/OV Relays:** DIN‑rail protective relays with adjustable thresholds & delays (Schneider/Eaton/Carlo‑Gavazzi, etc.).  
- **24 VDC Control PSU:** DIN‑rail supply feeding both coils (size per coil inrush + relays).  
- **E‑STOP:** NC contacts, panel‑mount, clearly labeled; wire to drop both paths.  
- **Indicator stack light (optional):** Green = OK, Red = TRIPPED, Amber = BYPASS.

> **Coil voltage sanity:** If your shunt‑trip coil is 120 VAC but your control loop is 24 VDC, use an **interposing relay** or choose a 24 VDC shunt‑trip accessory for a unified low‑voltage scheme.

---

## 5) Wiring notes (do/don’t)

- **Fuse the 24 VDC control loop** near the PSU; separate fuses for each coil branch.  
- **Use ferrules** on DIN‑rail terminals; label wires; keep control and power wiring in separate ducts.  
- **Provide a BYPASS** (lockable) only if mission‑critical—clearly indicate when energized.  
- **Surge protection:** Type‑1/2/3 on AC; TVS diodes across DC coil circuits; MOVs at contactor if needed.  
- **Grounding:** Single‑point bond from RF liner and surge devices to ground bar; follow NEC for grounding electrode system.

---

## 6) Commissioning checklist (quick)

- Trip tests: push **E‑STOP** → both open; reset and verify re‑energize.  
- Simulate UV/OV (use relay test function) → confirm correct side trips.  
- Verify **manual reset** required for the shunt‑trip breaker.  
- Confirm indicator lights and logging (if monitored) record each event.  
- Document setpoints & date; affix a small **one‑line** diagram inside the pod.

---

## 7) Minimal bill of materials (concept)

- Shunt‑trip main/input breaker (coil 24 VDC preferred)  
- Output contactor, 2‑pole, coil 24 VDC, sized for UPS output current  
- Two DIN‑rail **UV/OV** protective relays (adjustable)  
- 24 VDC DIN‑rail power supply (e.g., 2–5 A) + mini blade fuses or DIN fuse holders  
- E‑STOP (NC), indicator lights or stack light  
- DIN‑rail, terminal blocks, wire duct, labels, ferrules, TVS/MOV surge parts

---

*Contributions & field photos welcome. Save this as `docs/pod1-power-kill-diagram.md` in the repo.*
