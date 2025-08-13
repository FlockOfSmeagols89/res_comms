# Drill 001 — La Crosse Pilot (Thursday, October 16, 2025)

**Goal:** Verify local hub handles A/B/C traffic with quotas and logs; measure end-to-end latency and operator flow.

**Date/Time:** Thursday, October 16, 2025, **TBD local** (suggest 19:00 for after-work participation)  
**Duration:** 30 minutes on-air + 30 minutes for log collation

**Net Control (NCS):** @your-handle  
**Hubs involved:** @WI/HOLMEN/HUB1 (primary), [add others]  
**Paths:** VHF packet (primary), Dial-up BBS (fallback), optional voice coordination & mesh/LoRa

---

## Frequencies / Ports (confirm with partners)
- **VHF Packet (AX.25):** 145.050 MHz (placeholder — coordinate with local club; avoid APRS 144.390)  
- **Voice coordination (optional):** [simplex/repeater] _____.___ MHz  
- **Dial-up BBS:** (___) ___-____ (local-only if via ATA/PBX)  
- **Mesh / LoRa (optional):** AREDN SSID ______ / RNS 915.0 MHz BW 125 kHz SF 8 TX 14 dBm

> Keep ham traffic unencrypted. PGP signing for authenticity is OK.

---

## Inject plan (traffic to send)
**T+00–T+10: Priority A (ICS‑213) x3**  
- A1: “Medical supplies needed at shelter #2 in 24h”  
- A2: “Cooling center opening at Community Hall, request 20 cots”  
- A3: “Road closure at Oak & 5th; reroute advisory”

**T+10–T+20: Welfare (Priority B) x5**  
- B1–B5: “Family at [address] OK. Need [item] in 48h.”

**T+20–T+25: Bulletin (Priority C) x1**  
- C1: “Water distribution hours extended Thu–Fri 10:00–18:00.”

**T+25–T+30: Catch‑up & confirmations**

> Use headers:
```
To: @REGION/CITY/CALLSIGN or @REGION/CITY/HUBID
From: @REGION/CITY/CALLSIGN
Priority: A|B|C
Expires: 2025-10-18T23:59Z
Via: HF|VHF|POTS|MESH
Sig: (optional PGP signature block)
```
**MsgID = sha256(header+body)** (nodes drop duplicates).

---

## Success criteria
- ≥ **90%** of traffic delivered within **2 hours** end‑to‑end  
- **100%** integrity on signed messages (if used)  
- Logs exported and attached to this issue (sanitized)  
- Operator notes captured (bottlenecks, quota adjustments, RF issues)

---

## Assignments
- **Net control:**  
- **Hub operator(s):**  
- **Traffic injectors:**  
- **Logger/metrics:**  
- **Safety/ground:** (monitor weather, lightning, site safety)

---

## Pre‑drill checklist (T‑1 to T‑0)
- [ ] Confirm **quotas** in effect (A unlimited, B 2/hr, C 1/2hr)  
- [ ] Post BBS **banner** (policy + format) and verify from a test caller  
- [ ] VHF packet: verify antenna/coax, radio PTT, Direwolf config, monitor channel idle  
- [ ] Battery **SOC** ≥ 80%; DC-first rails active; UPS OK LEDs green  
- [ ] Print **ICS‑213** and **welfare** forms for manual inject backup  
- [ ] Share this issue with participants; confirm frequency/channel list

---

## NCS on‑air script (sample)
> “This is the Resilience Hub *La Crosse Pilot* drill net for Thursday, October 16, 2025. This is a **training** exercise. Priorities in effect: **A** life safety, **B** welfare, **C** bulletins. Quotas are posted. We will inject A traffic during the first 10 minutes, B traffic minutes 10–20, C traffic minutes 20–25. Please keep transmissions concise. Net control will acknowledge and route. Stand by for injects.”

---

## Post‑drill (attach to this issue)
- [ ] Export **logs** (timestamps, path, MsgID) and attach (sanitize any private data)  
- [ ] **Latency table** (per message: inject time → delivered time)  
- [ ] **After‑action notes** (what worked, what to change)  
- [ ] Open follow‑ups: frequencies, quotas, banner wording, hardware fixes  
- [ ] Schedule **Drill 002** window

---

**Refs:** `docs/operator-quick-card.md`, `docs/frequencies-template.md`, `data/templates/` (ICS‑213 & welfare), `docs/provenance.md`
