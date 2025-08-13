# Operator Quick Card (Tier-2 Hub)
*Post this near the console. Keep it short.*

**Priorities & quotas (default)**
- **A — Life Safety:** Unlimited
- **B — Welfare:** 2 msgs/hour/user
- **C — Bulletin:** 1 msg/2 hours/user
*(Rolling 6-hour window; adjust during drills/outages.)*

**Message headers (minimum)**
```
To: @REGION/CITY/CALLSIGN or @REGION/CITY/HUBID
From: @REGION/CITY/CALLSIGN
Priority: A|B|C
Expires: YYYY-MM-DDTHH:MMZ
Via: HF|VHF|POTS|MESH
Sig: (optional PGP signature block)
```
**Message ID:** sha256(header+body). Nodes drop duplicates; expired messages are purged.

**ICS-213 (condensed)** → see `data/templates/ICS-213.txt`  
**Welfare check** → see `data/templates/welfare.txt`

**BBS banner should show:** current quotas, message format, code of conduct, and a link to docs.

**Operator actions**
1. Validate header & priority, reject junk.
2. Log (time, path, MsgID).
3. Route to next hop (packet/HF/POTS/mesh) or hold if path is down.
4. Confirm delivery or note expiry.
5. During congestion, enforce quotas and announce A/B-only windows if needed.

**Safety**
- Keep radios on **DC-first** power; AC only for gear that needs it.
- Watch battery voltage & temps; log duty cycle during drills.
- Lightning in area? Move coax to bulkhead protectors and monitor.
