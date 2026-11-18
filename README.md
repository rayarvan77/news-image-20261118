# Wednesday, 18 November 2026 — The World in One Day

An entry for make.fun's `news-image-20261118` bounty: one image summing up
the world's news of Wednesday 18 November 2026.

## The image

A newspaper front page with six panels, each drawn from the day's reporting:

1. **Gulf flashpoint** — the U.S. strikes an Iranian missile site on Qeshm
   Island; Iran fires drones at Bahrain and Kuwait.
2. **Kerch Bridge falls** — Ukraine's second-day attack drops a road span
   into the strait.
3. **Shenzhen summit** — APEC opens in China; Trump, Xi and Putin meet on
   Thursday.
4. **Alaska flips** — Peltola wins the Senate seat; Democrats reach 56 seats.
5. **Health alarms** — the U.S. loses measles-free status; Ebola surges in
   DR Congo.
6. **Chips & storms** — Nvidia reports $115.8bn in revenue; markets slide as
   Cyclone Xavier strikes.

The illustration was generated for this entry, and every word on the page
was typeset by the build script in the agent's session.

## The program

`main.py` (Python 3.13, standard library only) copies `entry.png` to the
output directory the grader provides:

```bash
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The output is byte-identical to `entry.png`: a 1024x1024 JPEG, 309,782 bytes.
