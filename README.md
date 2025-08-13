# Nationwide Resilience Hubs

https://github.com/FlockOfSmeagols89/res_comms/tree/main/docs

[![License: Apache-2.0](https://img.shields.io/badge/Code-Apache--2.0-blue.svg)](LICENSES/APACHE-2.0.txt)

[![Docs: CC BY-SA 4.0](https://img.shields.io/badge/Docs-CC%20BY--SA%204.0-brightgreen.svg)](LICENSES/CC-BY-SA-4.0.txt)

[![Hardware: CERN OHL-W v2](https://img.shields.io/badge/Hardware-CERN%20OHL--W%20v2-orange.svg)](LICENSES/CERN-OHL-W-2.0.txt)


Created by Jamie J Freier and Contributors

*A citizen-built, open, auditable fallback for messaging when cellular/Internet fail — from neighborhood to nationwide.*

This repository contains the open **Pilot Pack** for standing up **Resilience Hubs**:
- **Tier 2** Local BBS hubs (dial-up + VHF packet + optional mesh)
- **Tier 1** Regional packet relays
- **Tier 0** HF backbone nodes (store-and-forward inter-region)

**Transparency & Provenance:** Every release includes checksums and a CHANGELOG. Configs, code, and SOPs are kept reproducible. See `LICENSE` for the multi-license scheme and `CONTRIBUTING.md` for DCO sign-off.

**Recommended citation:**
> Freier, J., *Nationwide Resilience Hubs — Pilot Pack*, 2025-08-11. CC BY-SA 4.0 / Apache-2.0 / CERN-OHL-W v2.

**Quick start (Phase-1 Local Hub):**
1. Build a small BBS on a Pi/mini-PC with an external serial modem.
2. Add a VHF packet node with Direwolf.
3. Print the BBS card and run a 30-minute drill.
4. Iterate and publish logs + learnings.

See `docs/pilot-pack.md` and `drills/drill_001.md`.



## Resilience Pod-1 (Microbunker)

Backbone-grade, small-footprint comms pod (≈6′×8′ inside) for Tier-2 hubs or a small Tier-1 relay. Designed for RF shielding, clean power, and fast, redundant “kill” logic.

**Docs**
- ▶️ **Build & Layout:** [`docs/pod1-microbunker.md`](docs/pod1-microbunker.md)
- ⚡ **Power “Kill” Diagram:** [`docs/pod1-power-kill-diagram.md`](docs/pod1-power-kill-diagram.md)

**Highlights**
- Inner **Faraday liner** (bonded seams) + **conductive RF door** with finger-stock gasket  
- Short **L-shaped entrance** (breaks line-of-sight for blast/EM fields)  
- **Fiber-only data** penetration; bonded RF bulkhead panel for antennas  
- Cascaded surge + **isolation transformer + EMP/RFI filter** + **online UPS**  
- **DC-first** power (LiFePO₄ + MPPT) for radios/compute; AC only when needed  
- Dual **UV/OV relays** + **shunt-trip input breaker** + **output contactor** + **E-STOP**

**Quick-start checklist**
1. Site & shell ready (precast/CMU or framed)  
2. Install continuous RF liner; verify door gasket continuity  
3. Grounding: single-point bond to ground rods/ring  
4. Power chain: Type-1/2/3 SPDs → isolation xfmr → EMP/RFI filter → online UPS → DC bus  
5. Penetrations: fiber data; RF bulkhead with lightning arrestors; honeycomb RF vents  
6. Commission tests: shield sanity, bonding <1 Ω, UV/OV trip tests, E-STOP, dark-power run

> Docs licensed CC BY-SA 4.0; hardware notes under CERN OHL-W v2. Contributions welcome.


