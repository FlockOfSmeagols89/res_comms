# Nationwide Resilience Hubs

https://github.com/FlockOfSmeagols89/res_comms/tree/main/docs

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
