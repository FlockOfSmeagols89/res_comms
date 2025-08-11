# Drill 001 — 30-minute local net + 10 messages

**Objective:** Verify local hub handles A/B/C traffic with quotas and logs.

**Script:**
- T+00: Net control opens; announce priorities and quotas.
- T+05: Inject 3 Priority-A ICS-213s.
- T+10: 5 welfare (B) messages.
- T+20: 1 community bulletin (C).
- T+25: Confirm deliveries; collect latencies.
- T+30: Close; export logs; record metrics.

**Success:** ≥90% delivered under 2 hours; 100% integrity on signed msgs.
