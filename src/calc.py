# src/calc.py

import csv, os

CSV_PATH = os.path.join("Data", "examples", "cases.csv")
EPS = 1e-9

def priority(E, R, D, H, lam): return 1.0 / (E + R + D + lam * H + EPS)
def virtue(C, R, E):         return (C - R) * (C / (R + E + EPS))

if not os.path.exists(CSV_PATH):
    print(f"[ERROR] not found: {CSV_PATH}")
    raise SystemExit(1)

with open(CSV_PATH, "r", encoding="utf-8-sig", newline="") as f:
    sample = f.read(1024); f.seek(0)
    dialect = csv.Sniffer().sniff(sample, delimiters=",;\t")
    rdr = csv.DictReader(
        (ln for ln in f if not ln.strip().startswith("```")),
        dialect=dialect
    )

    rows = 0
    for r in rdr:
        rows += 1
        lam = r.get("lambda") or r.get("lam") or r.get("λ")
        C, R, E, D, H, lam = map(float, (r["C"], r["R"], r["E"], r["D"], r["H"], lam))
        p = priority(E, R, D, H, lam)
        v = virtue(C, R, E)
        print(r["case_id"], "priority=", round(p, 4), "virtue=", round(v, 4))

    if rows == 0:
        print("[WARN] no data rows read. Make sure the first line of cases.csv is:")
        print("case_id,context,C,R,E,D,H,lambda")
if __name__ == "__main__":
    run()